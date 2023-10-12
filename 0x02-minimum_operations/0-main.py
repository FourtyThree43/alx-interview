#!/usr/bin/python3
"""
Main file for testing
"""

minOperations = __import__('0-minoperations').minOperations_v2

n = 265394817
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 731642859
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
