#!/usr/bin/env python3
"""
Email Validator v1.1
- Asks user for ONE email interactively
- Validates syntax
- Validates domain (simple DNS A lookup)
- Prints clean, professional results
"""

import re
import socket

EMAIL_REGEX = re.compile(
    r"^(?P<local>[^@\s]{1,64})@(?P<domain>[A-Za-z0-9.-]+\.[A-Za-z]{2,})$"
)

def validate_syntax(email: str) -> bool:
    match = EMAIL_REGEX.match(email.strip())
    if not match:
        return False
    local = match.group("local")
    if len(local) > 64:
        return False
    if local.startswith(".") or local.endswith("."):
        return False
    if ".." in local:
        return False
    return True

def domain_exists(domain: str) -> bool:
    try:
        socket.gethostbyname(domain)
        return True
    except Exception:
        return False

def main():
    print("=== Email Validator v1.1 ===")
    email = input("Enter email to validate: ").strip()

    if not email:
        print("No email entered.")
        return

    syntax_ok = validate_syntax(email)

    if not syntax_ok:
        print(f"{email} -> INVALID (Bad syntax)")
        return

    domain = EMAIL_REGEX.match(email).group("domain")
    domain_ok = domain_exists(domain)

    if domain_ok:
        print(f"{email} -> VALID")
        print(f"Syntax: OK | Domain: {domain} (resolves ✓)")
    else:
        print(f"{email} -> INVALID")
        print(f"Syntax: OK | Domain: {domain} (does NOT resolve ✗)")

if __name__ == "__main__":
    main()