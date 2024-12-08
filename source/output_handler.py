import os
import csv

class OutputHandler:
    def __init__(self, output_file):
        self.output_file = output_file

    def save_results(self, ip_requests, most_accessed_endpoint, suspicious_ips):
        """Save the analysis results to a CSV file."""
        try:
            os.makedirs(os.path.dirname(self.output_file), exist_ok=True)
            with open(self.output_file, 'w', newline='') as csv_file:
                writer = csv.writer(csv_file)

                # Save IP request counts
                writer.writerow(["IP Address", "Request Count"])
                for ip, count in ip_requests.items():
                    writer.writerow([ip, count])
                writer.writerow([])

                # Save most accessed endpoint
                writer.writerow(["Most Accessed Endpoint", "Access Count"])
                endpoint, count = most_accessed_endpoint
                writer.writerow([endpoint, count])
                writer.writerow([])

                # Save suspicious activity
                writer.writerow(["Suspicious IP", "Failed Attempts"])
                for ip, count in suspicious_ips.items():
                    writer.writerow([ip, count])

            print(f"Results saved to '{self.output_file}'")
        
        except PermissionError as e:
            print(f"Error: Permission denied while writing to file '{self.output_file}' - {e}")

        except FileNotFoundError as e:
            print(f"Error: The directory for the file '{self.output_file}' does not exist - {e}")

        except IsADirectoryError as e:
            print(f"Error: Expected file but found a directory '{self.output_file}' - {e}")

        except IOError as e:
            print(f"Error: General I/O error occurred while writing to file '{self.output_file}' - {e}")

        except Exception as e:
            print(f"Error: An unexpected error occurred while saving results - {e}")
