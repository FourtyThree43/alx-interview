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
    if not all(i >= 0 for i in data):
        return False
    try:
        bytes(data).decode('utf-8')
        return True
    except (OverflowError, TypeError, UnicodeDecodeError, ValueError):
        return False


def decodedUTF8(data: List[int]) -> Optional[str]:
    """ Decode a list of integers to UTF-8
        Return: decoded string
    """
    try:
        return bytes(data).decode('utf-8')
    except (ValueError, UnicodeDecodeError, TypeError):
        return None
