import re

class LogUtils:
    @staticmethod
    def extract_ip(line):
        """Extracts IP from a log line."""
        first_part = line.split(' ', 1)[0]
        return first_part if LogUtils.is_valid_ip(first_part) else None

    @staticmethod
    def extract_endpoint(line):
        """Extracts the endpoint from a log line."""
        parts = re.split(r'"[A-Z]+\s', line)
        return parts[1].split(' ')[0] if len(parts) > 1 else None

    @staticmethod
    def is_valid_ip(ip):
        """Validate if a string is a valid IP address."""
        parts = ip.split('.')
        if len(parts) != 4:
            return False
        return all(part.isdigit() and 0 <= int(part) <= 255 for part in parts)

    @staticmethod
    def is_failed_login(line):
        """Check if the line indicates a failed login attempt."""
        failed_indicators = [
            "401", "403", "Invalid credentials", "Failed login",
            "Unauthorized", "Access denied", "Too many failed attempts",
            "Bad credentials", "Account locked", "expired"
        ]
        return any(indicator.lower() in line.lower() for indicator in failed_indicators)
