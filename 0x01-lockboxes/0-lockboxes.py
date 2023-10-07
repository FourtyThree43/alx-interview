#!/usr/bin/python3
"""
Module for the canUnlockAll function.
"""
from typing import List
from collections import deque


def canUnlockAll(boxes: List[List[int]]) -> bool:
    """
    Determines if all the boxes can be opened.

    Args:
        boxes (list of lists): A list of lists representing the boxes and keys.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    num_boxes = len(boxes)
    unlocked_boxes = set([0])

    queue = deque([0])

    while queue:
        box = queue.popleft()

        for key in boxes[box]:
            if key not in unlocked_boxes and key < num_boxes:
                unlocked_boxes.add(key)
                queue.append(key)

    return len(unlocked_boxes) == num_boxes
