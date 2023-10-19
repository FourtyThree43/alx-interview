def parse_log_line(line: str) -> tuple | None:
    """ Parses a log line and returns a tuple of the form:
    (<IP Address>, <date>, <status code>, <file size>)
    or None if the line does not match the expected format.
    """
    parts = line.split()
    if len(parts) == 4:
        ip_address, date, status_code, file_size = parts
        try:
            return ip_address, date, int(status_code), int(file_size)
        except ValueError:
            return None
    else:
        return None


def compute_metrics(parsed_data_list: list):
    """ Computes various metrics from the given parsed data """
    total_file_size = 0
    status_code_count = {}

    for parsed_data in parsed_data_list:
        if parsed_data is not None:
            _, _, status_code, file_size = parsed_data
            total_file_size += file_size
            if status_code in [200, 301, 400, 401, 403, 404, 405, 500]:
                status_code_count[status_code] = status_code_count.get(
                    status_code, 0) + 1

    print(f"Total file size: {total_file_size}")
    for code, count in status_code_count.items():
        print(f"{code}: {count}")


# Sample log lines
log_lines = [
    "192.168.1.1 2023-10-19 200 1024",
    "192.168.1.2 2023-10-19 404 512",
    "invalid log line",
    "192.168.1.3 2023-10-19 500 2048",
]

# Parse log lines and compute metrics
parsed_data_list = [parse_log_line(line) for line in log_lines]
compute_metrics(parsed_data_list)
