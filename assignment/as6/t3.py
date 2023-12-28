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

def draw_shapes():
    root = tk.Tk()
    root.title("Shapes")
    canvas = tk.Canvas(root, width=300, height=300)
    canvas.pack()

    shapes = [Rectangle(100, 50), Circle(50), Square(80), Oval(70, 40)]

    for idx, shape in enumerate(shapes, start=1):
        shape.draw(canvas)
        print(f"Area of Shape {idx}: {shape.area()}")

    root.mainloop()

draw_shapes()