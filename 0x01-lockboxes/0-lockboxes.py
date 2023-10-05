#!/usr/bin/python3
"""
Module for the canUnlockAll function.
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
        boxes (list of lists): A list of lists representing the boxes and their keys.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """

    # Initialize a set to keep track of visited boxes and keys seen
    visited = set()
    keys_seen = set()

    # Start with box 0, which is already unlocked
    stack = [0]
    visited.add(0)

    while stack:
        current_box = stack.pop()
        for key in boxes[current_box]:
            if key not in visited:
                stack.append(key)
                visited.add(key)
            keys_seen.add(key)

    return len(visited) == len(boxes) and len(keys_seen) == len(boxes)
