import requests

response = requests.get('https://sugoku.herokuapp.com/board?difficulty=easy')
board = response.json()['board']

default_board = [
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

print_board(board)