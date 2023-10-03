# alx-interview

## 0x01. lockboxes

## Lockboxes Problem

## Problem Description

You have `n` number of locked boxes in front of you. Each box is numbered sequentially from `0` to `n - 1` and each box may contain keys to the other boxes. The task is to write a method that determines if all the boxes can be opened.

## Assumptions

- A key with the same number as a box opens that box.
- All keys will be positive integers.
- There can be keys that do not have boxes.
- The first box `boxes[0]` is unlocked.

## Solution

The problem can be solved using various search algorithms. Here are some of them:

1. **Breadth-First Search (BFS)**
2. **Depth-First Search (DFS)**
3. **Iterative Deepening Depth First Search (IDDFS)**
4. **Dijkstra's Algorithm**
5. **A* Search Algorithm**

## Time Complexity

1. **Breadth-First Search (BFS)**: The time complexity is O(n), where n is the number of boxes. This is because each box and key is processed once.

2. **Depth-First Search (DFS)**: The time complexity is also O(n) for the same reason as BFS.

3. **Iterative Deepening Depth First Search (IDDFS)**: The time complexity is O(n), but it may require more time than BFS and DFS because it processes some nodes multiple times.

4. **Dijkstra's Algorithm**: The time complexity is O((n + m) log n), where n is the number of boxes and m is the total number of keys. This is because it uses a priority queue and processes each edge in the graph once.

5. **A* Search Algorithm**: The time complexity depends on the heuristic used. In the worst case, it can be O(n!), but with a good heuristic, it can be much faster.

In this case, since we only need to know whether it's possible to open all boxes or not, BFS or DFS would be sufficient and efficient choices.

And remember, as Donald Knuth said, “Premature optimization is the root of all evil.” It’s often more important to have a correct and understandable solution than an optimized but complex one. Happy coding! 😊

                          +-+-+-+-+-+-+-+-+-+-+-+-+-+
                          |F|o|u|r|t|y|T|h|r|e|e|4|3|
                          +-+-+-+-+-+-+-+-+-+-+-+-+-+
                                                         
                         _|            _|  _|  _|_|_|    
                       _|_|  _|    _|  _|  _|        _|  
                         _|    _|_|    _|_|_|_|  _|_|    
                         _|  _|    _|      _|        _|  
                         _|  _|    _|      _|  _|_|_|    
                                                         
                                                         
## ❝ Quote ❞

"When the only tool you have is a hammer, you tend to treat everything as if
it were a nail."
		-- Abraham Maslow
