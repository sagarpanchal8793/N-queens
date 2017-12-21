#!/usr/bin/env python
# nrooks.py : Solve the N-Rooks problem!
# D. Crandall, 2016
# Updated by Zehua Zhang, 2017
#
# The N-rooks problem is: Given an empty NxN chessboard, place N rooks on the board so that no rooks
# can take any other, i.e. such that no two rooks share the same row or column.

import sys
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
    if type_of_input == "nqueen":
    	return "\n".join([ " ".join([ "Q" if board[row][col] == 1 else "X" if col == y and row == x else "_" for col in range(N) ]) for row in range (N)])    
    else:
	return "\n".join([ " ".join([ "R" if board[row][col] == 1 else "X" if col == y and row == x else "_" for col in range(N) ]) for row in range (N)])

# Add a piece to the board at the given position, and return a new board (doesn't change original)
def add_piece(board, row, col):
        return board[0:row] + [board[row][0:col] + [1,] + board[row][col+1:]] + board[row+1:]

# Get list of successors of given board state
def successors(board):
    return [ add_piece(board, r, c) for r in range(0, N) for c in range(0,N)]

# The below function will give the list of successors for the given board state, along with this it will check whether a row or column already has a queen
# or not, if yes it wont allow to add a new queen or rook and the given location. Also it checks if the row and column where it is going to place the
# queen / rook is unavailable or not, if yes then it won't place it over there and will continue the loop. Moreover it also checks that the current
# position already holds a queen or rook, if it holds then it won't allow to add anything at that position. If all of the above mentioned conditions
# are false then it will finally add a piece which will be our valid successor for the given state.

def successors2(board):
    add_piece_list = [] #created to store all the valid successors of the current state.

    if type_of_input == "nqueen":   #successor code for n-queens
        for row in range(N):
            for col in range(N):
                if sum(board[row]) >= 1: 
                    continue
                elif count_on_col(board, col) >= 1:
                    continue
                elif row == x and col == y:
                    continue
                elif board[row][col] == 1:
                    continue
                elif is_diagonal(board, row, col):
                    continue
                else:
                    add_piece_list.append(board[0:row] + [board[row][0:col] + [1,] + board[row][col+1:]] + board[row+1:])

    else:                           #successor code for n-rooks
        for row in range(N):
            for col in range(N):
                if sum(board[row]) >=1:
                    continue
                elif count_on_col(board, col) >= 1:
                    continue
                elif row == x and col == y:
                    continue
                elif board[row][col] == 1:
                    continue
                else:
                    add_piece_list.append(board[0:row] + [board[row][0:col] + [1,] + board[row][col+1:]] + board[row+1:])
                    
    return (add_piece_list)

# This function will check only the diagonal values whether is there any queen placed or not. If a queen is placed, it wont allow to put a new queen
# in the same diagonal for the given row and col value of the board. It will also check whether the row and column values are not going out of index.
def is_diagonal(board,row,col):
    for i in range(N):
        if (row-i >= 0 and col-i >= 0 and board[row-i][col-i] == 1) or (row-i >= 0 and col+i < N and \
        board[row-i][col+i] == 1) or (row+i < N and col-i >= 0 and board[row+i][col-i] == 1) or (row+i < N and col+i < N and \
        board[row+i][col+i] == 1):
            return True           
                        
# check if board is a goal state
def  is_goal(board):
    return count_pieces(board) == N #and \
        #all( [ count_on_row(board, r) <= 1 for r in range(0, N) ] ) and \
        #all( [ count_on_col(board, c) <= 1 for c in range(0, N) ] )

# Solve n-rooks / n-queens!
def solve(initial_board):
    fringe = [initial_board]
    
    while len(fringe) > 0:
        for s in successors2(fringe.pop()):
            if is_goal(s):
                return(s)
            fringe.append(s)
    return False

# This takes the input of whether to run the code for n-queens or n-rooks.
type_of_input = sys.argv[1]
# This is N, the size of the board. It is passed through command line arguments
N = int(sys.argv[2])
# This are the x and y co-ordinates those are to be made unavailable for placing the pieces
x = int(sys.argv[3])
y = int(sys.argv[4])

# As in python, the matrix starts from 0,0, we have to reduce the input for co-ordinates by 1 so as to make the correct position unavailable. 
x -=1
y -=1

# The board is stored as a list-of-lists. Each inner list is a row of the board.
# A zero in a given square indicates no piece, and a 1 indicates a piece.
initial_board = [[0]*N for i in range(N)]

print ("Starting from initial board:\n" + printable_board(initial_board) + "\n\nLooking for solution...\n")

solution = solve(initial_board)
print (printable_board(solution) if solution else "Sorry, no solution found. :(")
