#!/usr/bin/python3
""" UTF-8 Validation
"""
from typing import List, Optional


def validUTF8(data: List[int]) -> bool:
    """ Check is a list of integers is valid UTF-8 encoded data
        Return: True if data is valid UTF-8 encoded, else return False
    """
    if not all(isinstance(i, int) for i in data):
        return False
    if not all(0 <= i < 256 for i in data):
        return False
    try:
        decoded = bytes(data).decode('utf-8')
        if list(decoded.encode('utf-8')) != data:
            return False
        return True
    except (OverflowError, TypeError, UnicodeDecodeError, ValueError,
            IndexError):
        return False


def decodedUTF8(data: List[int]) -> Optional[str]:
    """ Decode a list of integers to UTF-8
        Return: decoded string
    """
    try:
        return bytes(data).decode('utf-8')
    except (OverflowError, TypeError, UnicodeDecodeError, ValueError):
        return None
