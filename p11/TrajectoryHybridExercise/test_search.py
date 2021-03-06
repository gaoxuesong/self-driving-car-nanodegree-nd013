#!/usr/bin/env python

from hybrid_breadth_first import search, reconstruct_path, show_path

X = 1
_ = 0

MAZE = [
    [_,X,X,_,_,_,_,_,_,_,X,X,_,_,_,_,],
    [_,X,X,_,_,_,_,_,_,X,X,_,_,_,_,_,],
    [_,X,X,_,_,_,_,_,X,X,_,_,_,_,_,_,],
    [_,X,X,_,_,_,_,X,X,_,_,_,X,X,X,_,],
    [_,X,X,_,_,_,X,X,_,_,_,X,X,X,_,_,],
    [_,X,X,_,_,X,X,_,_,_,X,X,X,_,_,_,],
    [_,X,X,_,X,X,_,_,_,X,X,X,_,_,_,_,],
    [_,X,X,X,X,_,_,_,X,X,X,_,_,_,_,_,],
    [_,X,X,X,_,_,_,X,X,X,_,_,_,_,_,_,],
    [_,X,X,_,_,_,X,X,X,_,_,X,X,X,X,X,],
    [_,X,_,_,_,X,X,X,_,_,X,X,X,X,X,X,],
    [_,_,_,_,X,X,X,_,_,X,X,X,X,X,X,X,],
    [_,_,_,X,X,X,_,_,X,X,X,X,X,X,X,X,],
    [_,_,X,X,X,_,_,X,X,X,X,X,X,X,X,X,],
    [_,X,X,X,_,_,_,_,_,_,_,_,_,_,_,_,],
    [X,X,X,_,_,_,_,_,_,_,_,_,_,_,_,_,],
]

EMPTY = [[_ for i in range(16)] for j in range(16)]

heuristic = [[max(16-y, 16-x) for x in range(16)] for y in range(16)]
heuristic = EMPTY

GRID = MAZE # change to MAZE for testing

START = (0.0,0.0,0.0)
GOAL = (len(GRID)-1, len(GRID[0])-1)
GOAL = (0, len(GRID[0])-1)

def main():
	
	for i in range(len(heuristic)):
		print(heuristic[i])

	print("\nFinding path through grid:")
	s = ""
	for row in GRID :
		row_s = ""
		for c in row:
			if c == 0:
				row_s += "  "
			else:
				row_s += "##"
		row_s += '\n'
		s += row_s
	print(s)
	
	closed, came_from, final = search(GRID, START, GOAL, heuristic)
	
	path = reconstruct_path(came_from, GOAL, START, final)
	
	show_path(path, START, GOAL)


if __name__ == "__main__":
	main()