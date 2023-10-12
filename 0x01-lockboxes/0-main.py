#!/usr/bin/python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll_IDDFS

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))

boxes = []

keys = []
for n in range(1, 1000):
    keys = []
    for m in range(1, 1000):
        keys.append(m)
    boxes.append(keys)

print(canUnlockAll(boxes))
