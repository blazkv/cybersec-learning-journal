import os
import sys
import time
import logging
import re
import argparse
import shutil
from datetime import datetime

# Configure logging to file 'analyzer.log', appending entries with timestamp and level
logging.basicConfig(
    filename='analyzer.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def get_args():
    """Parse command-line arguments for the log analyzer."""
    parser = argparse.ArgumentParser(description="Continuous Log Analyzer")
    parser.add_argument(
        '--file',
        required=True,
        help="Path to the log file to monitor"
    )
    parser.add_argument(
        '--pattern',
        required=False,
        default=None,
        help="Regex pattern to filter lines (default: process all lines)"
    )
    parser.add_argument(
        '--interval',
        type=float,
        default=1.0,
        help="Polling interval in seconds when waiting for new lines (default: 1.0)"
    )
    parser.add_argument(
        '--verbose',
        action='store_true',
        help="Enable verbose console output for debugging"
    )
    return parser.parse_args()

def validate_file(filepath: str) -> None:
    """
    Ensure the specified log file exists, is a file (not directory), and is readable.
    Exit program if any validation fails.
    """
    if not os.path.exists(filepath):
        logging.error(f"File does not exist: {filepath}")
        print(f"ERROR: The file does not exist: {filepath}")
        sys.exit(1)

    if not os.path.isfile(filepath):
        logging.error(f"Path is not a file: {filepath}")
        print(f"ERROR: The path is not a file: {filepath}")
        sys.exit(1)

    if not os.access(filepath, os.R_OK):
        logging.error(f"File is not readable: {filepath}")
        print(f"ERROR: The file is not readable: {filepath}")
        sys.exit(1)

    logging.info(f"File validated: {filepath}")

# Regex pattern to parse detailed log line components:
# Expected format: "YYYY-MM-DD HH:MM:SS LEVEL User:<user> IP:<ip> <message>"
log_pattern = re.compile(
    r'(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\s+'
    r'(?P<level>\w+)\s+'
    r'User:\s(?P<user>\S+)\s+'
    r'IP:\s(?P<ip>\d{1,3}(?:\.\d{1,3}){3})\s+'
    r'(?P<message>.+)'
)

def process_line(line: str, verbose: bool):
    """
    Parse and process a single log line.
    Prints and logs alert if level is ERROR or message indicates a failed login.
    """
    clean_line = line.strip().replace('\x00', '')  # Remove null chars if present
    if not clean_line:
        return

    match = log_pattern.match(clean_line)
    if not match:
        if verbose:
            print(f"Unrecognized line format: {clean_line}")
        return

    data = match.groupdict()

    if verbose:
        print(f"Parsed data: {data}")

    # Alert on error-level logs or failed login attempts
    if data['level'] == 'ERROR' or 'Failed login' in data['message']:
        alert_msg = (f"ALERT: {data['timestamp']} - {data['level']} for user "
                     f"{data['user']} from IP {data['ip']}: {data['message']}")
        print(alert_msg)
        logging.warning(alert_msg)

    # Log processed line
    logging.info(f"Processed line: {clean_line}")

def tail_log_file(filepath: str, pattern: re.Pattern, interval: float, verbose: bool) -> None:
    """
    Continuously read new lines appended to the log file.
    Applies user pattern filter if provided, and handles log rotation/truncation.
    """
    try:
        with open(filepath, 'r', encoding='utf-8', errors='replace') as file:
            file.seek(0, os.SEEK_END)  # Start at file end to tail new entries
            logging.info(f"Started monitoring {filepath}")

            while True:
                line = file.readline()

                if not line:
                    # Check if file truncated or rotated (size smaller than current position)
                    current_pos = file.tell()
                    file_size = os.path.getsize(filepath)
                    if current_pos > file_size:
                        logging.info("File truncated or rotated; seeking to start.")
                        file.seek(0)
                    else:
                        time.sleep(interval)
                    continue

                # If user provided a pattern, skip lines that do NOT match it
                if pattern and not pattern.search(line):
                    continue

                # Warn about possible encoding issues
                if '�' in line:
                    logging.warning(f"Encoding issue detected in line: {line.strip()}")

                # Process the line (parse, alert, log)
                process_line(line, verbose)

    except UnicodeDecodeError as e:
        logging.error(f"Encoding error while reading {filepath}: {e}")
        print("ERROR: The file has invalid encoding.")
        sys.exit(1)
    except FileNotFoundError:
        logging.error(f"File not found during monitoring: {filepath}")
        print(f"ERROR: File was deleted or moved: {filepath}")
        sys.exit(1)
    except KeyboardInterrupt:
        logging.info("Log monitoring stopped by user.")
        print("\nStopped monitoring.")
        sys.exit(0)
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        print(f"ERROR: Unexpected error: {e}")
        sys.exit(1)

def count_file_lines(filepath: str) -> int:
    """
    Count total lines in a given file efficiently.
    """
    count = 0
    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
        for _ in f:
            count += 1
    return count

def backup_and_trim_log(log_path: str, max_lines: int = 100_000) -> None:
    """
    Check if the analyzer log exceeds max_lines.
    Prompt user for backup, create backup if requested,
    then trim oldest lines to keep file within size limit.
    """
    line_count = count_file_lines(log_path)
    if line_count <= max_lines:
        return  # No trimming needed

    print(f"\nWARNING: Log file '{log_path}' has {line_count} lines, exceeding {max_lines}.")
    response = input("Would you like to create a backup before trimming? (y/n): ").strip().lower()
    if response == 'y':
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = f"{log_path}.{timestamp}.bak"
        shutil.copy2(log_path, backup_path)
        print(f"Backup created at {backup_path}")
        logging.info(f"Backup of log created at {backup_path}")
    else:
        print("No backup created. Proceeding with trimming.")
        logging.info("User declined log backup before trimming.")

    # Read all lines and keep only the last max_lines lines
    with open(log_path, 'r', encoding='utf-8', errors='replace') as f:
        lines = f.readlines()

    trimmed_lines = lines[-max_lines:]

    # Write trimmed lines back to the log file
    with open(log_path, 'w', encoding='utf-8') as f:
        f.writelines(trimmed_lines)

    print(f"Log trimmed to last {max_lines} lines.")
    logging.info(f"Log file trimmed to last {max_lines} lines due to size limit.")

def main() -> None:
    """
    Main entry point: parse args, validate input file, manage analyzer log size,
    compile user pattern if provided, then start tailing the log file.
    """
    args = get_args()
    validate_file(args.file)

    # Manage the size of our own log file before starting
    backup_and_trim_log('analyzer.log')

    pattern = None
    if args.pattern:
        try:
            pattern = re.compile(args.pattern)
            logging.info(f"Using user regex pattern filter: {args.pattern}")
        except re.error as e:
            logging.error(f"Invalid regex pattern provided: {e}")
            print(f"ERROR: Invalid regex pattern: {e}")
            sys.exit(1)

    # Start monitoring the log file with optional filtering and verbosity
    tail_log_file(args.file, pattern, args.interval, args.verbose)

if __name__ == "__main__":
    main()
