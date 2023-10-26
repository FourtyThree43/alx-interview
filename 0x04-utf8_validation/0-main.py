#!/usr/bin/python3
"""
Main file for testing
"""

validUTF8 = __import__('0-validate_utf8').validUTF8
decodeUTF8 = __import__('0-validate_utf8').decodedUTF8

data = [65]
print(f"Valid UTF-8: {validUTF8(data)} \tDecoded UTF-8: [{decodeUTF8(data)}]")

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(f"Valid UTF-8: {validUTF8(data)} \tDecoded UTF-8: [{decodeUTF8(data)}]")

data = [229, 65, 127, 256]
print(f"Valid UTF-8: {validUTF8(data)} \tDecoded UTF-8: [{decodeUTF8(data)}]")

data = ["65"]
print(f"Valid UTF-8: {validUTF8(data)} \tDecoded UTF-8: [{decodeUTF8(data)}]")

data = []
print(f"Valid UTF-8: {validUTF8(data)} \tDecoded UTF-8: [{decodeUTF8(data)}]")
