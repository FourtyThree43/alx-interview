#!/usr/bin/python3
"""
Module for the canUnlockAll function.
"""
from typing import List
from collections import deque


def canUnlockAll(boxes: List[List[int]]) -> bool:
    """
    Breadth-First Search (BFS) algorithm is used to determine if all the boxes
    can be opened.

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


def canUnlockAll_DFS(boxes: List[List[int]]) -> bool:
    """
    Depth-First Search (DFS) algorithm is used to determine if all the boxes
    can be opened.

    Args:
        boxes (list of lists): A list of lists representing the boxes and keys.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    num_boxes = len(boxes)
    unlocked_boxes = set([0])

    stack = [0]

    while stack:
        box = stack.pop()

        for key in boxes[box]:
            if key not in unlocked_boxes and key < num_boxes:
                unlocked_boxes.add(key)
                stack.append(key)

    return len(unlocked_boxes) == num_boxes


def canUnlockAll_IDDFS(boxes: List[List[int]]) -> bool:
    """
    Iterative Deepening Depth First Search (IDDFS) algorithm is used to
    determines if all the boxes can be opened.

    Args:
        boxes (list of lists): A list of lists representing the boxes and keys.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    num_boxes = len(boxes)

    for depth in range(num_boxes):
        unlocked_boxes = set([0])
        stack = [(0, 0)]

        while stack:
            box, box_depth = stack.pop()

            if box_depth > depth:
                continue

            for key in boxes[box]:
                if key not in unlocked_boxes and key < num_boxes:
                    unlocked_boxes.add(key)
                    stack.append((key, box_depth + 1))

        if len(unlocked_boxes) == num_boxes:
            return True

    return False
