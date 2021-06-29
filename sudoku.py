# sudoku.py | Jacob Gilhaus
#
# Backtracking Sudoku solver
# Influenced by Tech with Tim

import requests
import argparse

parser = argparse.ArgumentParser(description='Solve backtracking Suduko with a provided difficulty setting.')
parser.add_argument('difficulty', metavar='DIF', type=int, help='1:easy | 2:medium | 3:hard')
args = parser.parse_args()

if args.difficulty == 1:
    response = requests.get('https://sugoku.herokuapp.com/board?difficulty=easy')
    board = response.json()['board']
elif args.difficulty == 2:
    response = requests.get('https://sugoku.herokuapp.com/board?difficulty=medium')
    board = response.json()['board']
elif args.difficulty == 3:
    response = requests.get('https://sugoku.herokuapp.com/board?difficulty=hard')
    board = response.json()['board']

playing_board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

for x in range(0,9):
    for y in range(0,9):
        playing_board[x][y] = board[x][y]

def solve(b):
    nxt = find_empty(b)
    if not nxt:
        return True
    else:
        r, c = nxt

    for i in range(1,10):
        if valid(b, i, (r,c)):
            b[r][c] = i

            if solve(b):
                return True

            b[r][c] = 0

    return False
            
def valid(b, num, square):
    # check the row
    for c in range(len(b[0])):
        if b[square[0]][c] == num and square[1] != c:
            return False

    # check the column
    for r in range(len(b)):
        if b[r][square[1]] == num and square[0] != r:
            return False

    xsquare = square[1] // 3
    ysquare = square[0] // 3

    # check the subsquare
    for r in range(ysquare*3, ysquare*3+3):
        for c in range(xsquare*3, xsquare*3+3):
            if b[r][c] == num and (r,c) != square:
                return False

    return True

def print_board(b):
    for x in range(len(b[0])):
        if x % 3 == 0 and x != 0:
            print('----------------------')

        for y in range(len(b[1])):
            if y % 3 == 0 and y != 0:
                print('| ', end='')

            if y == 8:
                print(b[x][y])
            else:
                print(str(b[x][y]) + ' ', end='')

def find_empty(b):
    for x in range(len(b[0])):
        for y in range(len(b[1])):
            if b[x][y] == 0:
                return (x,y)
        
    return None

print("Initial\n")
print_board(playing_board)
solve(playing_board)
print('\n- - - - - - - - - - -')
print('Solved\n')
print_board(playing_board)