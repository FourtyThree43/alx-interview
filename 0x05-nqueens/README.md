# alx-interview

* [🎲 0x05. N Queens](#-0x05.-n-queens)
* [📖 Project Overview](#-project-overview)
* [🎯 Learning Objectives](#-learning-objectives)
* [🧩 Algorithm](#-algorithm)
* [🛠️ Environment](#️-environment)
* [📚 Tasks](#-tasks)
* [📚 References](#-references)
* [Author](#-author)
* [❝ Quote ❞](#-quote-)

## 🎲 0x05. N Queens

### 📖 Project Overview

This project is about solving the **N queens problem** using Python. The N queens puzzle is a fascinating and complex challenge that involves placing N non-attacking queens on an N×N chessboard. This problem is named after the strongest female chess player of all time, **Judit Polgár**.

### 🎯 Learning Objectives

- Understand the concept of backtracking in algorithms
- Learn how to solve the N queens problem
- Improve problem-solving skills with Python

### 🧩 Algorithm

The algorithm used to solve this problem is based on `backtracking`. It starts by placing queens one by one in different columns, starting from the leftmost column. When placing a queen in a column, it checks for clashes with already placed queens. If a clash is found, it backtracks and tries the next row in the current column.

### 🛠️ Environment

* Languages: Python3.4.3
* OS: Ubuntu 20.04 LTS
* Style guidelines: [PEP 8 style (version 1.7.x)](https://pep8.readthedocs.io/en/release-1.7.x/intro.html) \|| [Google Style Python Docstrings](http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html)

## 📚 Tasks

### 0️⃣ N queens

Write a program that solves the N queens problem.

#### Usage: nqueens N

- If the user called the program with the wrong number of arguments, print `Usage: nqueens N`, followed by a new line, and exit with the status 1
- where N must be an integer greater or equal to 4
- If N is not an integer, print `N must be a number`, followed by a new line, and exit with the status 1
- If N is smaller than 4, print `N must be at least 4`, followed by a new line, and exit with the status 1
- The program should print every possible solution to the problem
- One solution per line
- Format: see example
- You don’t have to print the solutions in a specific order
- You are only allowed to import the sys module

## 📚 References

- Queen - [Wikipedia](https://en.wikipedia.org/wiki/Queen_(chess))
- Queens Puzzle - [Wikipedia](https://en.wikipedia.org/wiki/Eight_queens_puzzle)
- Backtracking - [Wikipedia](https://en.wikipedia.org/wiki/Backtracking)



## Author


                          +-+-+-+-+-+-+-+-+-+-+-+-+-+
                          |F|o|u|r|t|y|T|h|r|e|e|4|3|
                          +-+-+-+-+-+-+-+-+-+-+-+-+-+
                                                         
                         _|            _|  _|  _|_|_|    
                       _|_|  _|    _|  _|  _|        _|  
                         _|    _|_|    _|_|_|_|  _|_|    
                         _|  _|    _|      _|        _|  
                         _|  _|    _|      _|  _|_|_|    
                                                         
                                                         
## ❝ Quote ❞

```
Microsoft Acquires Nothing 

REDMOND, WA -- In an unprecedented move, Microsoft refrained from acquiring any
rival companies for a full week. "I can't believe it," one industry analyst
noted. "This is the first time in years that I haven't read any headlines about
Microsoft acquiring something." 

The lack of Microsoft assimilation this week left a vacuum in computer industry
publications. "Microsoft acquisition stories make up 10% of our headlines," an
editor at Ziff-Slavis said. "We had to scramble to fill this void. We ran some
controversial Jessie Burst columns instead, hoping that we could recoup ad
revenue from people reading all the flames in the Talk Back forums. Jessie
Burst forums account for 15% of our total ad revenue."
```