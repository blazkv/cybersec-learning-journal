# Password Strength Checker & Generator

This small project helped me refresh my Python basics and get more comfortable with Python-specific tools: working with external packages like `pyperclip`, using modules like `string` and `secrets`, and setting up a simple `venv` to keep everything organized. My goal is to gradually build a toolkit of small, useful scripts that improve both my coding fluency and my security mindset.

```python
import string
import secrets
import pyperclip

# -------------------------------
# Function to check password strength
# -------------------------------
def check_password_strength():
    print('\n--- Password Strength Checker ---\n')

    # Ask user for their password
    password = input('Enter your password > ')

    length = len(password)
    score = 0
    feedback = []

    # Check if password length is between 12 and 20
    if 12 <= length <= 20:
        print('\nYour password is long enough.')
        score += 1  # add 1 point for good length
    else:
        print('\nYour password is too short.')
        return  # exit the function early if length is too short

    # Check for presence of uppercase, lowercase, digits, and symbols
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_symbol = any(char in string.punctuation for char in password)

    # Add points and feedback based on what the password includes
    if has_upper:
        score += 1
    else:
        feedback.append('uppercase letter')

    if has_lower:
        score += 1
    else:
        feedback.append('lowercase letter')

    if has_digit:
        score += 1
    else:
        feedback.append('digit')

    if has_symbol:
        score += 1
    else:
        feedback.append('symbol')

    # Final score and suggestions
    print(f'\nPassword length: {length}')
    print(f'Score: {score}/5')

    if score == 5:
        print('Strong password!')
    elif score >= 3:
        print('Moderate password. Consider adding: ' + ', '.join(feedback))
    else:
        print('Weak password. Missing: ' + ', '.join(feedback))


# -------------------------------
# Function to generate a strong password
# -------------------------------
def generate_password():
    print('\n--- Password Generator ---\n')

    # Keep asking for length until it's valid
    while True:
        length = int(input('Enter password length (min 12, max 20) > '))
        if 12 <= length <= 20:
            break
        else:
            print('Password length must be between 12 and 20.\n')

    # Character sets
    letters = string.ascii_letters  # a-z + A-Z
    digits = string.digits          # 0-9
    symbols = string.punctuation    # !@#$%^&*() etc.
    all_chars = letters + digits + symbols

    # Start password with at least one of each type
    password = [
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.ascii_uppercase),
        secrets.choice(digits),
        secrets.choice(symbols)
    ]

    # Fill the rest of the password randomly
    for _ in range(length - 4):
        password.append(secrets.choice(all_chars))

    # Shuffle so the first 4 are not always in the same order
    secrets.SystemRandom().shuffle(password)

    # Join list to make the final password string
    final_password = ''.join(password)

    print(f'\nGenerated password: {final_password}')

    # Copy the password to clipboard
    pyperclip.copy(final_password)
    print('Password copied to clipboard!')


# -------------------------------
# Main Program Menu
# -------------------------------
print('\n--- Password Strength Checker & Password Generator ---\n')

while True:
    print('What would you like to do?')
    print('1. Check Password Strength')
    print('2. Generate a Password')
    print('Type "quit" to exit the app.\n')

    # Get user choice
    service = input('> ').strip().lower()

    # Call appropriate function based on choice
    if service in ['password strength checker', '1']:
        check_password_strength()
        break
    elif service in ['generate a password', '2']:
        generate_password()
        break
    elif service == 'quit':
        print('\nYou quit the app.\n')
        break
    else:
        print('\nInvalid choice. Please try again.\n')```
