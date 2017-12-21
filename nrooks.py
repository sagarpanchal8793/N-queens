#!/usr/bin/env python
# nrooks.py : Solve the N-Rooks problem!
# D. Crandall, 2016
# Updated by Zehua Zhang, 2017
#
# The N-rooks problem is: Given an empty NxN chessboard, place N rooks on the board so that no rooks
# can take any other, i.e. such that no two rooks share the same row or column.

import sys
import time

# Count # of pieces in given row
def count_on_row(board, row):
    return sum( board[row] ) 

# Count # of pieces in given column
def count_on_col(board, col):
    return sum( [ row[col] for row in board ] )

# Count total # of pieces on board
def count_pieces(board):
    return sum([ sum(row) for row in board ] )

# Return a string with the board rendered in a human-friendly format
def printable_board(board):
    return "\n".join([ " ".join([ "R" if col else "_" for col in row ]) for row in board])

# Add a piece to the board at the given position, and return a new board (doesn't change original)
def add_piece(board, row, col):
    return board[0:row] + [board[row][0:col] + [1,] + board[row][col+1:]] + board[row+1:]

# Get list of successors of given board state
def successors(board):
    return [ add_piece(board, r, c) for r in range(0, N) for c in range(0,N) ]

# The below successor function is added so as to optimize the performance of the code. In both the cases of BFS or DFS the code will pass through this function as for both the
# methods it will return a list of successors for the current state, Also before generating successors it is checking some of the contraints.
def successors2(board):
    add_piece_list = []
    
    for row in range(N):
        for col in range(N):
            if sum(board[row]) >= 1:
                continue
            elif count_on_col(board, col) >= 1:
                continue
            elif board[row][col] == 1:
                continue
            else:
                add_piece_list.append(board[0:row] + [board[row][0:col] + [1,] + board[row][col+1:]] + board[row+1:])
                
    return (add_piece_list)


# check if board is a goal state
def is_goal(board):
    return count_pieces(board) == N


# Solve n-rooks using DFS!
def solve_using_dfs(initial_board):
    fringe = [initial_board]
    
    while len(fringe) > 0:
        for s in successors2(fringe.pop()):
            if is_goal(s):
                return(s)
            fringe.append(s)
    return False

# Solve n-rooks using BFS!
def solve_using_bfs(initial_board):
    fringe = [initial_board]
    
    while len(fringe) > 0:
        for s in successors2(fringe.pop(0)): 		#https://stackoverflow.com/questions/4426663/how-do-i-remove-the-first-item-from-a-python-list
            if is_goal(s):
                return(s)
            fringe.append(s)
    return False


# This is N, the size of the board. It is passed through command line arguments.
N = int(sys.argv[1])

# The board is stored as a list-of-lists. Each inner list is a row of the board.
# A zero in a given square indicates no piece, and a 1 indicates a piece.
initial_board = [[0]*N for i in range (N)]

print ("Starting from initial board:\n" + printable_board(initial_board) + "\n\nLooking for solution...\n")
solution = solve_using_dfs(initial_board)
print (printable_board(solution) if solution else "Sorry, no solution found. :(")
