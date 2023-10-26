#!/usr/bin/python3
"""
Main file for testing
"""

validUTF8 = __import__('0-validate_utf8').validUTF8
decodeUTF8 = __import__('0-validate_utf8').decodedUTF8

# Test case for valid UTF-8 encoding
data = [65]
print(f"Valid UTF-8: {validUTF8(data)} \tDecoded UTF-8: [{decodeUTF8(data)}]")

# Test case for valid UTF-8 encoding
data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(f"Valid UTF-8: {validUTF8(data)} \tDecoded UTF-8: [{decodeUTF8(data)}]")

# Test case for ValueError (256 is not a valid byte value)
data = [229, 65, 127, 256]
print(f"Valid UTF-8: {validUTF8(data)} \tDecoded UTF-8: [{decodeUTF8(data)}]")

# Test case for TypeError (input data is not an integer)
data = ["65"]
print(f"Valid UTF-8: {validUTF8(data)} \tDecoded UTF-8: [{decodeUTF8(data)}]")

# Test case for OverflowError (input integer is too large)
# This integer is too large to convert to Python's internal bytes representation
data = [2**31]
print(f"Valid UTF-8: {validUTF8(data)} \tDecoded UTF-8: [{decodeUTF8(data)}]")

# Test case for empty input data
data = []
print(f"Valid UTF-8: {validUTF8(data)} \tDecoded UTF-8: [{decodeUTF8(data)}]")

data = [-260]
print(f"Valid UTF-8: {validUTF8(data)} \tDecoded UTF-8: [{decodeUTF8(data)}]")
