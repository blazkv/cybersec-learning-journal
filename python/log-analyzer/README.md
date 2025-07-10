# Continuous Log Analyzer

## 📌 Context

This Python tool **monitors a log file in real time**, parses each new line with regex, and triggers alerts for `ERROR` levels or failed login attempts. It uses `argparse` for CLI options, handles log rotation and encoding issues, and writes events to a separate `analyzer.log`.

If you don’t already have a log file to test, you can use the included [`generate_logs.py`](generate_logs.py) script to generate fake log lines matching the expected format.

---

## 📁 Files

- [`app.py`](app.py) — Main Python script
- [`generate_logs.py`](generate_logs.py) — Helper script to generate fake logs if you don’t have real ones
- All requirements are built into Python — no external packages needed

---

## 🚀 How to Use

### 1. **(Optional) Generate test logs**
If you don’t have an existing log file, run:
`python generate_logs.py`
This will create `test.log` in the same folder and continuously append fake log lines.

### 2. **Run the analyzer**
`python app.py --file test.log`
Or point it to any other log file you want to monitor.

### 3. **Options**

* `--file` (required): Path to the log file to monitor
* `--pattern`: Regex pattern to filter log lines (optional)
* `--interval`: Polling interval in seconds (default: `1.0`)
* `--verbose`: Enable verbose console output for debugging

### 4. **Example**
Monitor `test.log` with verbose output:
`python app.py --file test.log --verbose`

### 5. **Stop monitoring**
Press `Ctrl+C` to stop safely.

---

🔙 Back to [Python Projects Overview](../README.md)

🔙 Back to [Miscellaneous Overview](README.md)
