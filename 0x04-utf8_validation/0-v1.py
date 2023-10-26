#!/usr/bin/python3
""" UTF-8 validation module.
"""


def validUTF8(data: list[int]) -> bool:
    # Check if all elements in the list are integers and within the range 0-255
    if not all(isinstance(num, int) and 0 <= num <= 255 for num in data):
        raise ValueError(
            "All elements in the list must be integers in the range 0-255")

    num_elements = len(data)
    index = 0

    while index < num_elements:
        # If the number is less than 128 (binary 10000000), it's a single-byte character
        if data[index] < 0b10000000:
            index += 1
        # If the number starts with binary 10, it's not a valid starting byte
        elif data[index] < 0b11000000:
            return False
        else:
            # Determine the number of bytes in the character
            if data[index] < 0b11100000:
                num_bytes = 2
            elif data[index] < 0b11110000:
                num_bytes = 3
            elif data[index] < 0b11111000:
                num_bytes = 4
            else:
                return False

            # Check if there are enough bytes left in the list for this character
            if index + num_bytes > num_elements:
                return False

            # Check that each of the following bytes starts with binary 10
            for j in range(1, num_bytes):
                if data[index + j] >> 6 != 0b10:
                    return False

            index += num_bytes

    return True
