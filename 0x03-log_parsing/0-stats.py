#!/usr/bin/python3
from collections import defaultdict
from typing import Tuple, List, Dict
import re
import sys
import time

STATUS_CODES = (200, 301, 400, 401, 403, 404, 405, 500)


def print_statistics(file_sizes: List[int], status_codes: Dict[int,
                                                               int]) -> None:
    """
    Prints the statistics of file sizes and status codes.

    Args:
        file_sizes (List[int]): List of file sizes.
        status_codes (Dict[int, int]): Dictionary of status codes and
        their counts.
    """
    total_size = sum(file_sizes)
    print(f"File size: {total_size}")
    for status_code in sorted(status_codes.keys()):
        print(f"{status_code}: {status_codes[status_code]}")


def parse_log_line(line: str) -> Tuple[int, int] | Tuple[None, None]:
    """
    Parses a log line and returns the status code and file size.

    Args:
        line (str): The log line to parse.

    Returns:
        Tuple[int, int]: The status code and file size.
        If no match is found, returns None for both.
    """
    log_pattern = r'(\d+\.\d+\.\d+\.\d+) - \[([^\]]+)\] "GET .*" (\d+) (\d+)'
    match = re.match(log_pattern, line.strip())
    if match:
        _, _, status_code, size = match.groups()
        return int(status_code), int(size)

    return None, None


def process_log_lines() -> None:
    """
    Processes log lines from stdin. Prints statistics every 10 lines
    and at the end.
    """
    line_count = 0
    file_sizes = []
    status_codes = defaultdict(int)  # type: ignore[var-annotated]

    try:
        for line in sys.stdin:
            status_code, file_size = parse_log_line(line)
            if status_code and file_size:
                file_sizes.append(file_size)

                if status_code in STATUS_CODES:
                    status_codes[status_code] += 1

                line_count += 1

                if line_count % 10 == 0:
                    print_statistics(file_sizes, status_codes)
    except KeyboardInterrupt:
        pass
    finally:
        print_statistics(file_sizes, status_codes)
        time.sleep(5)


if __name__ == "__main__":
    process_log_lines()
