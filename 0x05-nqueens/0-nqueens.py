#!/usr/bin/python3
""" Module 🎲 0x05. N Queens
"""
import sys


def nqueens(n: int):
    """ solve N Queen problem
    """
    pass


def main():
    """ Main
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    nqueens(N)


if __name__ == "__main__":
    main()
