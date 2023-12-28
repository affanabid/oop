from abc import ABC, abstractmethod
import tkinter as tk

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def draw(self, canvas):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def draw(self, canvas):
        canvas.create_rectangle(50, 50, 50 + self.width, 50 + self.height, outline='black')

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def draw(self, canvas):
        canvas.create_oval(50, 50, 50 + self.radius * 2, 50 + self.radius * 2, outline='black')

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

class Oval(Circle):
    def __init__(self, horizontal_radius, vertical_radius):
        self.horizontal_radius = horizontal_radius
        self.vertical_radius = vertical_radius

    def area(self):
        return 3.14 * self.horizontal_radius * self.vertical_radius

    def draw(self, canvas):
        canvas.create_oval(50, 50, 50 + self.horizontal_radius * 2, 50 + self.vertical_radius * 2, outline='black')


def draw_rectangle(root, canvas):
    root.title("Rectangle")
    rect = Rectangle(100, 50)
    rect.draw(canvas)
    root.mainloop()

def draw_circle(root, canvas):
    root.title("Circle")
    circle = Circle(50)
    circle.draw(canvas)
    root.mainloop()

def draw_square(root, canvas):
    root.title("Rectangle")
    square = Square(50)
    square.draw(canvas)
    root.mainloop()

def draw_oval(root, canvas):
    root.title("Oval")
    oval = Oval(70, 40)
    oval.draw(canvas)
    root.mainloop()

root = tk.Tk()
canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()
draw_rectangle(root, canvas)
draw_circle(root, canvas)
draw_square(root, canvas)
draw_oval(root, canvas)