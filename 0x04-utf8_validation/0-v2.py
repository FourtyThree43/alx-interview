#!/usr/bin/python3
""" UTF-8 validation module.
"""


def validUTF8(data: list[int]) -> bool:
    """Checks if a list of integers are valid UTF-8 codepoints."""
    n = len(data)
    i = 0
    while i < n:
        if not isinstance(data[i], int) or data[i] < 0 or data[i] > 255:
            return False

        if data[i] < 0b10000000:  # 1-byte character
            i += 1
        else:
            if data[i] < 0b11000000:  # Not a valid starting byte
                return False
            elif data[i] < 0b11100000:  # 2-byte character
                span = 2
            elif data[i] < 0b11110000:  # 3-byte character
                span = 3
            elif data[i] < 0b11111000:  # 4-byte character
                span = 4
            else:
                return False

            if i + span > n:  # Not enough bytes left for this character
                return False

            for j in range(1,
                           span):  # Check following bytes start with binary 10
                if data[i + j] >> 6 != 0b10:
                    return False

            i += span

    return True
