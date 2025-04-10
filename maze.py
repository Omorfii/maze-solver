from point import Point, Cell
import time
import random

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
        if seed:
            random.seed(1)
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
                cell.draw("purple")
                self.animate()
                current_starting_point = Point(current_starting_point.x + self.cell_size_x, current_starting_point.y)
            starting_point = Point(starting_point.x, starting_point.y + self.cell_size_y)
        self.break_entrance_and_exit()
        self.break_walls_r(0, 0)
        self.reset_cells_visited()
        

    def break_entrance_and_exit(self):
        entrance_cell = self._cells[0][0]
        entrance_cell.has_top_wall = False
        entrance_cell.draw("purple")

        exit_cell = self._cells[self.num_cols-1][self.num_rows-1]
        exit_cell.has_bottom_wall = False 
        exit_cell.draw("purple")

    def break_walls_r(self, i, j):
        current = self._cells[i][j]
        current.visited = True
        while True:
            to_visit = {}
            # Check above
            if 0 <= i-1 < len(self._cells) and self._cells[i-1][j].visited == False:
                to_visit["above"] = (i-1, j)
            # Check below
            if 0 <= i+1 < len(self._cells) and self._cells[i+1][j].visited == False:
                to_visit["below"] = (i+1, j)
            # Check left
            if 0 <= j-1 < len(self._cells[0]) and self._cells[i][j-1].visited == False:
                to_visit["left"] = (i, j-1)
            # Check right
            if 0 <= j+1 < len(self._cells[0]) and self._cells[i][j+1].visited == False:
                to_visit["right"] = (i, j+1)
            
            if not to_visit:
                return
            
            direction = random.choice(list(to_visit.keys()))
            ni, nj = to_visit[direction]

            cell_to_go = self._cells[ni][nj]

            if direction == "above":
                current.has_top_wall = False
                current.draw("purple")
                cell_to_go.has_bottom_wall = False
                cell_to_go.draw("purple")
            if direction == "below":
                current.has_bottom_wall = False
                current.draw("purple")
                cell_to_go.has_top_wall = False
                cell_to_go.draw("purple")
            if direction == "left":
                current.has_left_wall = False
                current.draw("purple")
                cell_to_go.has_right_wall = False
                cell_to_go.draw("purple")
            if direction == "right":
                current.has_right_wall = False
                current.draw("purple")
                cell_to_go.has_left_wall = False
                cell_to_go.draw("purple")
            
            self.animate()

            self.break_walls_r(ni, nj)

    def reset_cells_visited(self):
        for i in self._cells:
            for j in i:
                j.visited = False

    def solve(self):
        return self.solve_r(i=0, j=0)

    def solve_r(self, i, j):
        self.animate()
        current = self._cells[i][j]
        current.visited = True
        if current == self._cells[self.num_cols-1][self.num_rows-1]:
            return True
        
        #check above
        if 0 <= i-1 < len(self._cells) and self._cells[i-1][j].visited == False and self._cells[i-1][j].has_bottom_wall == False:
            self._cells[i][j].draw_move(self._cells[i-1][j])
            recursion =  self.solve_r(i-1, j)
            if recursion:
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i-1][j], True)
        # Check below
        if 0 <= i+1 < len(self._cells) and self._cells[i+1][j].visited == False and self._cells[i+1][j].has_top_wall == False:
            self._cells[i][j].draw_move(self._cells[i+1][j])
            recursion =  self.solve_r(i+1, j)
            if recursion:
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i+1][j], True)
        # Check left
        if 0 <= j-1 < len(self._cells[0]) and self._cells[i][j-1].visited == False and self._cells[i][j-1].has_right_wall == False:
            self._cells[i][j].draw_move(self._cells[i][j-1])
            recursion =  self.solve_r(i, j-1)
            if recursion:
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j-1], True)        

        # Check right
        if 0 <= j+1 < len(self._cells[0]) and self._cells[i][j+1].visited == False and self._cells[i][j+1].has_left_wall == False:
            self._cells[i][j].draw_move(self._cells[i][j+1])
            recursion =  self.solve_r(i, j+1)
            if recursion:
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j+1], True)

        return False        



    def animate(self):
        if self.win:
            self.win.redraw()
            time.sleep(0.0005)

    