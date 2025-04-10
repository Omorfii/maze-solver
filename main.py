from window import Window
from point import Line, Point, Cell
from maze import Maze

win = Window(800, 600)

#maze = Maze(50, 50, 7, 5, 100, 100, win, True)
#maze = Maze(50, 50, 14, 10, 50, 50, win)
maze = Maze(50, 50, 28, 20, 25, 25, win)
#maze = Maze(50, 50, 40, 30, 20, 20, win)

maze.solve()

win.wait_for_close()