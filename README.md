# Lockpick

Lockpick is a Python script for brute-forcing forms on web pages. It scans the specified URL for forms, identifies all input fields, and allows the user to provide values or files for brute-forcing. It supports verbose output to show detailed information about each attempt.

## Features

- Identifies and processes all input fields in forms.
- Allows the user to provide single values or files containing multiple values for each input field.
- Supports GET and POST methods for form submission.
- Verbose mode for detailed output of each brute-force attempt.

## Requirements

- Python 3.x
- `requests` library
- `beautifulsoup4` library

## Installation

1. Clone the repository or download the script.
2. Install the required Python libraries:

```sh
pip install requests beautifulsoup4
```

## Usage

Run the script with the `-u` flag to specify the URL and optionally the `-v` flag for verbose output:

```sh
python3 lockpick.py -u <URL> [-v]
```

### Example

```sh
python3 lockpick.py -u https://example.com/login.php -v
```

### Arguments

- `-u`, `--url`: The URL of the form to brute-force (required).
- `-v`, `--verbose`: Enable verbose output (optional).

## How It Works

1. The script scans the specified URL for forms.
2. For each form, it identifies the action, method, and input fields.
3. It prompts the user to provide values or file paths for each input field.
4. If a file path is provided, the script reads the values from the file.
5. The script attempts to submit the form using the provided values or values from the file.
6. In verbose mode, it prints detailed information about each attempt, including the response status code and a portion of the response text.

## Example Output

```sh
┌──(slim㉿kali)-[~/Documents/Projects/lockpick]
└─$ python3 lockpick.py -u https://example.com/login.php -v

░▒▓█▓▒░      ░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓███████▓▒░░▒▓███████▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓███████▓▒░  
░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓████████▓▒░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░ 

Form 1
Action: code/login_code.php
Method: POST
Enter the value for email: user@example.com
Enter the path for the password list file: /usr/share/wordlists/rockyou.txt
Trying with data: {'email': 'user@example.com', 'password': 'password1'}
Response status code: 200
Response text: <!DOCTYPE html>...
Form submission failed with data: {'email': 'user@example.com', 'password': 'password1'}
Trying with data: {'email': 'user@example.com', 'password': 'password2'}
Response status code: 200
Response text: <!DOCTYPE html>...
Form submission failed with data: {'email': 'user@example.com', 'password': 'password2'}
...
```

## License

This project is licensed under the MIT License.
```

This `README.md` file provides a comprehensive overview of the Lockpick tool, including its features, installation instructions, usage, and examples.# Lockpick
