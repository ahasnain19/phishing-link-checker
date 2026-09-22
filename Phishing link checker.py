import re
from urllib.parse import urlparse

print("================================")
print("       Phishing Link Checker")
print("================================")

url = input("Enter a URL to check: ").strip()

# Add HTTPS if the user did not include a protocol
if not url.startswith(("http://", "https://")):
    url = "https://" + url

parsed_url = urlparse(url)
domain = parsed_url.netloc.lower()
path = parsed_url.path.lower()

score = 0
warnings = []

# Check whether HTTPS is being used
if parsed_url.scheme == "https":
    print("\nHTTPS: Yes ✓")
else:
    print("\nHTTPS: No ✗")
    score += 2
    warnings.append("The website does not use HTTPS.")

# Check for an IP address instead of a domain name
ip_pattern = r"^(?:\d{1,3}\.){3}\d{1,3}$"

if re.match(ip_pattern, domain.split(":")[0]):
    print("IP address: Yes ✗")
    score += 2
    warnings.append("The link uses an IP address instead of a domain name.")
else:
    print("IP address: No ✓")

# Check URL length
if len(url) > 100:
    print("Long URL: Yes ✗")
    score += 1
    warnings.append("The URL is unusually long.")
else:
    print("Long URL: No ✓")

# Check for suspicious characters
if "@" in url:
    print("@ symbol: Yes ✗")
    score += 2
    warnings.append("The URL contains an @ symbol.")
else:
    print("@ symbol: No ✓")

# Check for excessive subdomains
subdomains = domain.split(".")

if len(subdomains) > 3:
    print("Multiple subdomains: Yes ✗")
    score += 1
    warnings.append("The URL contains multiple subdomains.")
else:
    print("Multiple subdomains: No ✓")

# Check for suspicious words
suspicious_words = [
    "login",
    "verify",
    "verification",
    "account",
    "secure",
    "update",
    "password",
    "bank",
    "confirm",
    "signin"
]

found_words = []

for word in suspicious_words:
    if word in url.lower():
        found_words.append(word)

if found_words:
    print("Suspicious keywords: Yes ✗")
    score += 1
    warnings.append(
        "The URL contains suspicious keywords: "
        + ", ".join(found_words)
    )
else:
    print("Suspicious keywords: No ✓")

# Check for excessive hyphens
if domain.count("-") >= 2:
    print("Multiple hyphens: Yes ✗")
    score += 1
    warnings.append("The domain contains multiple hyphens.")
else:
    print("Multiple hyphens: No ✓")

# Display risk level
print("\nRisk Assessment")
print("----------------------------")

if score <= 1:
    risk = "LOW"
elif score <= 3:
    risk = "MEDIUM"
else:
    risk = "HIGH"

print(f"Risk Level: {risk}")

# Display warnings
if warnings:
    print("\nWarnings")
    print("----------------------------")

    for warning in warnings:
        print(f"- {warning}")
else:
    print("\nNo obvious warning signs were detected ✓")

print("\nImportant: This tool does not guarantee that a website is safe.")
print("It only checks for common phishing indicators.")
