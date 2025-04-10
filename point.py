class Point:

    def __init__(self, x=0, y=0):
        self.x =  x 
        self.y =  y

class Line:

    def __init__(self, first_point, second_point):
        self.first_point = first_point
        self.second_point = second_point

    def draw(self, canvas, color):
        canvas.create_line(
    self.first_point.x, self.first_point.y, self.second_point.x, self.second_point.y, fill=color, width=2
)


class Cell:

    def __init__(self, first_point, second_point, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = first_point.x
        self._x2 = second_point.x
        self._y1 = first_point.y
        self._y2 = second_point.y
        self._win = win
        self._visited = False

    def draw(self, color):      
        point1 = Point(self._x1, self._y1)
        point2 = Point(self._x2, self._y1)
        point3 = Point(self._x2, self._y2)
        point4 = Point(self._x1, self._y2)

        line1 = Line(point1, point2)
        line2 = Line(point2, point3)
        line3 = Line(point3, point4)
        line4 = Line(point4, point1)

        if self._win:
            if self.has_top_wall:
                self._win.draw_line(line1, color)
            #else:
             #   self._win.draw_line(line1, "white")
            if self.has_right_wall:
                self._win.draw_line(line2, color)
            #else:
            #    self._win.draw_line(line2, "white")
            if self.has_bottom_wall:
                self._win.draw_line(line3, color)
            #else:
            #    self._win.draw_line(line3, "white")
            if self.has_left_wall:
                self._win.draw_line(line4, color)
            #else:
            #    self._win.draw_line(line4, "white")

    def draw_move(self, to_cell, undo=False):
        point1 = Point((self._x1 + self._x2) // 2, (self._y1 + self._y2) // 2)
        point2 = Point((to_cell._x1 + to_cell._x2) // 2, (to_cell._y1 + to_cell._y2) // 2)

        line = Line(point1, point2)

        if self._win:
            if not undo:
                self._win.draw_line(line, "red")
            else:
                self._win.draw_line(line, "gray")
