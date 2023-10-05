#!/usr/bin/python3
""" Module that determines if all the boxes can be opened"""
from typing import List
from collections import deque


def canUnlockAll(boxes: List[List[int]]) -> bool:
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


# def canUnlockAll_DFS(boxes: List[List[int]]) -> bool:
#     """
#     Determine if all boxes can be opened.

#     Args:
#     boxes (List[List[int]]): A list of lists where each inner list represents a
#                              box and contains integers representing keys.

#     Returns:
#     bool: True if all boxes can be opened, else False.

#     DFS Implementation (using Stack):
#         - Time Complexity: O(n), where n is the total number of keys across all
#           boxes.
#         - Space Complexity: O(n), where n is the total num of keys across all
#           boxes.
#         - Data Structure Used: Stack (represented by a set in Python)
#     """
#     if not boxes or len(boxes) == 0:
#         return False
#     if len(boxes) == 1:
#         return True

#     opened_boxes = set([0])
#     keys_found = set([key for key in boxes[0]])

#     while keys_found:
#         new_key = keys_found.pop()
#         if new_key not in opened_boxes:
#             opened_boxes.add(new_key)
#             keys_found.update(boxes[new_key])

#     return len(opened_boxes) == len(boxes)


# def canUnlockAll(boxes):
#     num_boxes = len(boxes)
#     unlocked_boxes = set()
#     keys_seen = set()

#     queue = deque([0])

#     while queue:
#         box = queue.popleft()
#         unlocked_boxes.add(box)

#         for key in boxes[box]:
#             keys_seen.add(key)

#             if key not in unlocked_boxes and key < num_boxes:
#                 queue.append(key)

#     return len(unlocked_boxes) == num_boxes