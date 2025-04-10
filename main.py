from window import Window
from point import Line, Point, Cell
from maze import Maze

win = Window(800, 600)

maze = Maze(50, 50, 7, 5, 100, 100, win)
#maze2 = Maze(50, 50, 14, 10, 50, 50, win)

win.wait_for_close()