![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Status](https://img.shields.io/badge/Status-Stable-brightgreen)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Contributions](https://img.shields.io/badge/Contributions-Welcome-orange)

# Email Intelligence Checker

A lightweight Python tool that analyzes email addresses for common issues including:
- Syntax validation
- Domain extraction
- Domain availability lookup
- Instant classification (e.g., free provider, corporate domain)

This tool does *not* send any data, connect to inboxes, or perform external scanning beyond optional DNS checks. Suitable for security beginners, recruiters, and developers who want quick email insights.

---

## Features
- Validates email format
- Extracts and checks domain existence
- Categorizes domain type (Gmail, Outlook, Yahoo, custom domains)
- Clean command-line interface

---


## Usage
Run the script and enter any email to analyze:

```bash
python EMAIL_VALIDATOR.py

The tool will request the email address and provide an instant breakdown.

Enter email: example@gmail.com

VALID ✔
Domain: gmail.com
Domain Available: Yes
Provider Type: Public / Free Email Service

Requirements
	•	Python 3.8+
	•	Install dependencies:

License

MIT License
Feel free to modify and improve the tool.

