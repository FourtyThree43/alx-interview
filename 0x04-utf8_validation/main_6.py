#!/usr/bin/python3
"""
Main for testing
"""

validUTF8_Passed = __import__('99-validate_utf8').validUTF8
validUTF8 = __import__('0-validate_utf8').validUTF8
decodeUTF8 = __import__('0-validate_utf8').decodedUTF8

data = [467, 133, 108]

print("----")

print(validUTF8_Passed(data))
print(validUTF8(data))
print(decodeUTF8(data))

print("----")
