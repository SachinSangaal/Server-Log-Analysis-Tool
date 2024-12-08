import os
import sys
from log_parser import LogParser
from log_analyzer import LogAnalyzer
from output_handler import OutputHandler
from config import LOG_FILE_PATH, OUTPUT_FILE_PATH, SUSPICIOUS_IP_THRESHOLD

def main():
    # Initialize the parser and parse the log file
    parser = LogParser(LOG_FILE_PATH)
    log_lines = parser.parse()

    if not log_lines:
        print("No logs found or failed to read logs.")
        return

    # Initialize the analyzer with parsed log lines
    analyzer = LogAnalyzer(log_lines)

    # Analyze the logs
    ip_requests = analyzer.count_requests_by_ip()
    most_accessed = analyzer.find_most_frequent_endpoint()
    suspicious_ips = analyzer.detect_suspicious_activity(SUSPICIOUS_IP_THRESHOLD)

    # Display results
    analyzer.display_results(ip_requests, most_accessed, suspicious_ips)

    # Save results to output file
    output_handler = OutputHandler(OUTPUT_FILE_PATH)
    output_handler.save_results(ip_requests, most_accessed, suspicious_ips)

if __name__ == "__main__":
    main()
