#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""This script reads stdin line by line and computes metrics """

from typing import Dict, List


def log_is_valid(tokens: List[str]) -> bool:
    """
    Check if a log is valid.

    Args:
        log (str): The log to check.

    Returns:
        bool: True if the log is valid, False otherwise.
    """
    from datetime import datetime

    if len(tokens) != 9:
        return False
    ip = tokens[0].split(".")
    if len(ip) != 4:
        return False
    if not all([i.isdigit() and int(i) in range(1, 256) for i in ip]):
        return False
    if tokens[1] != "-":
        return False
    time = " ".join(tokens[2:4])
    if not time.startswith("[") and time.endswith("]"):
        return False
    try:
        datetime.strptime(time[1:-2], "%Y-%m-%d %H:%M:%S.%f")
    except ValueError:
        return False
    if tokens[4:7] != ['"GET', "/projects/260", 'HTTP/1.1"']:
        return False
    if tokens[7] not in ("200", "301", "400", "401", "403", "404", "405",
                         "500"):
        return False
    if not tokens[8].isdigit():
        return False
    return True


def print_stats(file_size: int, codes_dict: Dict) -> None:
    """Print log statistics """
    print("File size:", file_size)
    for code, count in codes_dict.items():
        if count:
            print("{}: {}".format(code, count))


def main() -> None:
    """Entry point """
    import sys

    line_no, file_size = 0, 0
    codes_dict = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0
    }
    try:
        for log in sys.stdin:
            if line_no and line_no % 10 == 0:
                print_stats(file_size, codes_dict)
            line_no += 1
            tokens = log.split()
            if log_is_valid(tokens):
                file_size += int(tokens[8])
                codes_dict[tokens[7]] += 1
            else:
                continue
    except KeyboardInterrupt:
        print_stats(file_size, codes_dict)
        # exit(1)


if __name__ == "__main__":
    main()