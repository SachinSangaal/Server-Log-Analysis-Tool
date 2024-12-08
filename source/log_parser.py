from log_utils import LogUtils

class LogParser:
    def __init__(self, file_path):
        self.file_path = file_path

    def parse(self):
        """Parse the log file and return all the lines."""
        try:
            with open(self.file_path, 'r') as file:
                return file.readlines()
        except FileNotFoundError:
            print(f"Error: File '{self.file_path}' not found.")
        except PermissionError:
            print(f"Error: Permission denied for file '{self.file_path}'.")
        except IsADirectoryError:
            print(f"Error: Expected a file but found a directory at '{self.file_path}'.")
        except Exception as e:
            print(f"Error: {e}")
        return []

    def _extract_ip(self, line):
        """Extracts IP from a log line using LogUtils."""
        return LogUtils.extract_ip(line)

    def _extract_endpoint(self, line):
        """Extracts the endpoint from a log line using LogUtils."""
        return LogUtils.extract_endpoint(line)
    
