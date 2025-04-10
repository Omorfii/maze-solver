from tkinter import Tk, BOTH, Canvas

class Window: 

    def __init__(self, width, height, background_color="black"):
        self.__width = width
        self.__height = height
        self.__root = Tk()
        self.__root.title("Maze solver")

        screen_width = self.__root.winfo_screenwidth()
        screen_height = self.__root.winfo_screenheight()
        x_position = int((screen_width - self.__width) / 2)
        y_position = int((screen_height - self.__height) / 2)

        self.__root.geometry(f"{self.__width}x{self.__height}+{x_position}+{y_position}")

        self.__canvas = Canvas(self.__root, width=self.__width, height=self.__height, bg=background_color)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.running_window = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update()
        self.__root.update_idletasks()

    def wait_for_close(self):
        self.running_window = True
        while self.running_window:
            self.redraw()

    def close(self):
        self.running_window = False

    def draw_line(self, line, fill_color):
        line.draw(self.__canvas, fill_color)