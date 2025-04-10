from point import Point, Cell
import time

class Maze:

    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win=None,
            seed=None,
        ):

        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.seed = seed
        self.create_cells()
        

    def create_cells(self):
        self._cells = []
        starting_point = Point(self.x1, self.y1)
        for i in range(self.num_cols):
            self._cells.append([])
            current_starting_point = starting_point
            for j in range(self.num_rows):
                point2 = Point(current_starting_point.x + self.cell_size_x, current_starting_point.y + self.cell_size_y)
                cell = Cell(current_starting_point, point2, self.win)
                self._cells[i].append(cell)
                self.break_entrance_and_exit(i, j)
                cell.draw("purple")
                self.animate()
                current_starting_point = Point(current_starting_point.x + self.cell_size_x, current_starting_point.y)
            starting_point = Point(starting_point.x, starting_point.y + self.cell_size_y)

    def break_entrance_and_exit(self,i, j):
        if i == 0 and j == 0:
            self._cells[i][j].has_left_wall = False
        if i == self.num_cols - 1 and j == self.num_rows - 1:
            self._cells[i][j].has_right_wall = False

    def animate(self):
        if self.win:
            self.win.redraw()
            time.sleep(0.05)

