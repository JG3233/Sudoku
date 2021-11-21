# Sudoku

>Usage: python3 main.py [difficulty]   
>
>difficulties: e, m, h

A sudoku game with a solver that utilizes a backtracking algorithm. Use main to play the game. The solver is in sudoku.py

## The Guts

The printed board is gathered via an API call to the Sugoku Heroku app. They come in 3 flavors: easy, medium, and hard. The player can select which difficulty they prefer via the argument. Once the player is ready for the answer, simply tap any key and check your solution!

### Solver

The solving technique this program uses is a recursive backtracking algorithm. It iterates through the possible solutions, but doesn't start over if no solution is found. Instead, it backtracks and tries a different number instead of the one it placed last. The result is a far more efficent finding of a solution. 

Players may notice a longer delay with increasing difficulty. This is due to the algorithm needing to backtrack farther or more often, but it is still very efficient and far quicker than the naive solution.

### GUI

As noted, the inspiration came from a Tech with Tim project as an introduction to pygame. I wanted to write
an application that was algorithmically interesting and also allowed me to experiment with game-playing, so this was a good compromise. I used Tim's base GUI and modified from there to make improvements and learn pygame. As Tim also mentions in his video the GUI was somewhat of an afterthought, so this made for a great starting point.

### Alterations

A list of changes and updates to the original project:

>Author: Jacob Gilhaus  
>Based on a Tech with Tim project.
