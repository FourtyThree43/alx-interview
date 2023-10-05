#!/usr/bin/python3
""" Module that determines if all the boxes can be opened"""
# from typing import List
# from collections import deque

# def canUnlockAll(boxes: List[List[int]]) -> bool:
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


def canUnlockAll(boxes):
    # Initialize a list to keep track of visited boxes
    visited = [False] * len(boxes)

    # Start with box 0, which is already unlocked
    stack = [0]
    visited[0] = True

    while stack:
        current_box = stack.pop()
        for key in boxes[current_box]:
            if not visited[key]:
                stack.append(key)
                visited[key] = True

    # If all boxes are visited, return True; otherwise, return False
    return all(visited)
