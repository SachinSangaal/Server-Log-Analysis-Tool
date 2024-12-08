from collections import defaultdict
from log_utils import LogUtils

class LogAnalyzer:
    def __init__(self, log_lines):
        self.log_lines = log_lines

    def count_requests_by_ip(self):
        """Count the number of requests made by each IP."""
        ip_counts = defaultdict(int)
        for line in self.log_lines:
            ip = LogUtils.extract_ip(line)
            if ip:
                ip_counts[ip] += 1
        return dict(ip_counts)

    def find_most_frequent_endpoint(self):
        """Find the most frequently accessed endpoint."""
        endpoint_counts = defaultdict(int)
        for line in self.log_lines:
            endpoint = LogUtils.extract_endpoint(line)
            if endpoint:
                endpoint_counts[endpoint] += 1
        most_accessed = max(endpoint_counts.items(), key=lambda x: x[1], default=(None, 0))
        return most_accessed

    def detect_suspicious_activity(self, threshold):
        """Detect suspicious IPs with too many failed login attempts."""
        failed_attempts = defaultdict(int)
        for line in self.log_lines:
            if LogUtils.is_failed_login(line):
                ip = LogUtils.extract_ip(line)
                if ip:
                    failed_attempts[ip] += 1
        return {ip: count for ip, count in failed_attempts.items() if count > threshold}

    def display_results(self, ip_requests, most_accessed_endpoint, suspicious_ips):
        """Display the analysis results."""
        print("\nIP Address Request Counts:")
        for ip, count in ip_requests.items():
            print(f"{ip:<20} {count}")

        endpoint, count = most_accessed_endpoint
        print("\nMost Frequently Accessed Endpoint:")
        print(f"{endpoint or 'None'} (Accessed {count} times)")

        print("\nSuspicious Activity Detected:")
        for ip, count in suspicious_ips.items():
            print(f"{ip:<20} {count}")
