#!/usr/bin/python3
""" Module that determines if all the boxes can be opened"""
from typing import List
from collections import deque


def canUnlockAll_BFS(boxes: List[List[int]]) -> bool:
    """
    Determine if all boxes can be opened.

    Args:
    boxes (List[List[int]]): A list of lists where each inner list represents a
                             box and contains integers representing keys.

    Returns:
    bool: True if all boxes can be opened, else False.

    BFS Implementation (using Queue):
        - Time Complexity: O(n), where n is the total number of keys across all
          boxes.
        - Space Complexity: O(n), where n is the total num of keys across all
          boxes.
        - Data Structure Used: Queue (represented by a deque in Python)
    """
    if not boxes or len(boxes) == 0:
        return False
    if len(boxes) == 1:
        return True

    opened_boxes = set([0])
    keys_found = deque(boxes[0])

    while keys_found:
        new_key = keys_found.popleft()
        if new_key not in opened_boxes:
            opened_boxes.add(new_key)
            keys_found.extend(boxes[new_key])

    return len(opened_boxes) == len(boxes)


def canUnlockAll_DFS(boxes: List[List[int]]) -> bool:
    """
    Determine if all boxes can be opened.

    Args:
    boxes (List[List[int]]): A list of lists where each inner list represents a
                             box and contains integers representing keys.

    Returns:
    bool: True if all boxes can be opened, else False.

    DFS Implementation (using Stack):
        - Time Complexity: O(n), where n is the total number of keys across all
          boxes.
        - Space Complexity: O(n), where n is the total num of keys across all
          boxes.
        - Data Structure Used: Stack (represented by a set in Python)
    """
    if not boxes or len(boxes) == 0:
        return False
    if len(boxes) == 1:
        return True

    opened_boxes = set([0])
    keys_found = set([key for key in boxes[0]])

    while keys_found:
        new_key = keys_found.pop()
        if new_key not in opened_boxes:
            opened_boxes.add(new_key)
            keys_found.update(boxes[new_key])

    return len(opened_boxes) == len(boxes)


def canUnlockAll(boxes):
    num_boxes = len(boxes)
    unlocked_boxes = set([0])  # Start with the first box unlocked
    keys_found = set(boxes[0])  # Keys found in the first box

    while True:
        added_new_unlocked_box = False
        for box_idx in range(num_boxes):
            if box_idx in unlocked_boxes:
                for key in boxes[box_idx]:
                    if key not in unlocked_boxes:
                        unlocked_boxes.add(key)
                        added_new_unlocked_box = True

        # Check if any of the newly unlocked boxes contain keys
        # that were not in keys_found initially
        keys_found.update(unlocked_boxes)

        if not added_new_unlocked_box:
            break

    return len(keys_found) == num_boxes
