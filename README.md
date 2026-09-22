# Phishing Link Checker

A simple Python cybersecurity tool that checks URLs for common phishing indicators.

## Features

* Checks whether the URL uses HTTPS
* Detects IP addresses used instead of domain names
* Checks for unusually long URLs
* Detects suspicious `@` symbols
* Checks for multiple subdomains
* Detects suspicious keywords
* Checks for multiple hyphens in the domain
* Provides a risk level
* Shows warnings when suspicious indicators are found

## Requirements

* Python 3

No external libraries are required.

## How to Run

1. Download `phishing_link_checker.py`
2. Make sure Python 3 is installed
3. Open a terminal in the folder containing the file
4. Run:

```bash
python phishing_link_checker.py
```

5. Enter a URL when prompted.

## Example

You can test the program with this harmless example:

```text
http://secure-login-verify-example.com/account/update?user=123456789
```

The program should identify several warning signs and give the URL a risk level.

## Example Output

```text
================================
       Phishing Link Checker
================================

HTTPS: No ✗
IP address: No ✓
Long URL: Yes ✗
@ symbol: No ✓
Multiple subdomains: No ✓
Suspicious keywords: Yes ✗
Multiple hyphens: Yes ✗

Risk Assessment
----------------------------
Risk Level: HIGH
```

## Technologies

* Python
* Regular expressions
* URL parsing

## What I Learned

* How URLs are structured
* How to analyse URLs using Python
* How regular expressions work
* How to identify common phishing indicators
* How to create a simple risk scoring system

## Important

This tool does not guarantee that a website is safe or malicious.

It checks for common phishing indicators. Legitimate websites might trigger some checks, while phishing websites might avoid them.
