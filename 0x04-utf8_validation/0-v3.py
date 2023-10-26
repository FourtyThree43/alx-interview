#!/usr/bin/python3
""" UTF-8 validation module.
"""


def validUTF8(data: list[int]) -> bool:
    """ Checks if a list of integers are valid UTF-8 encoded characters.
    """
    num_bytes_in_sequence = 0

    # Masks for checking the first byte of a sequence
    masks = [0b10000000, 0b11100000, 0b11110000, 0b11111000]
    # Bit patterns for the first byte of a sequence
    patterns = [0b00000000, 0b11000000, 0b11100000, 0b11110000]

    for byte in data:
        if not isinstance(byte, int):
            return False

        # If this byte is a part of an existing UTF-8 sequence
        if num_bytes_in_sequence > 0:
            # Then it should be a continuation byte, that starts with `10`
            if byte >> 6 != 0b10:
                return False
            num_bytes_in_sequence -= 1
        else:
            # This byte is the start of a new UTF-8 sequence
            for i in range(len(masks)):
                if (byte & masks[i]) == patterns[i]:
                    num_bytes_in_sequence = i
                    break

            # No valid UTF-8 sequence identifier found
            if num_bytes_in_sequence == 0 and byte >= 0b10000000:
                return False

    # If we're still expecting bytes in a sequence then the data is invalid
    return num_bytes_in_sequence == 0
