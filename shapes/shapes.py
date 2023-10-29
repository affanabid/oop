import math

class Shape(object):
    # Represents a basic shape with a name, outline status, and background color.
    def __init__(self, name, has_outline, background_color, x_coordinate=0, y_coordinate=0):
        """
        Initializes a Shape object with the given parameters.
        
        Args:
            name (str): The name of the shape.
            has_outline (bool): Indicates whether the shape has an outline.
            background_color (str): The background color of the shape.
        """
        self.name = name
        self.has_outline = has_outline
        self.background_color = background_color
        self.x_cor = x_coordinate
        self.y_cor = y_coordinate

    def __str__(self):
        # Returns a string representation of the shape.
        return f"Name: {self.name}, Has Outline: {self.has_outline}, Background Color: {self.background_color}, Position: ({self.x_cor}, {self.y_cor})"


class Square(Shape):
    """
    Represents a square shape, inheriting from the Shape class.
    """
    def __init__(self, name, has_outline, background_color, side_length, x_coordinate=0, y_coordinate=0):
        """
        Initializes a Square object with the given parameters.
        
        Args:
            name (str): The name of the square.
            has_outline (bool): Indicates whether the square has an outline.
            background_color (str): The background color of the square.
            side_length (float): The length of one side of the square.
        """
        super().__init__(name, has_outline, background_color, x_coordinate, y_coordinate)
        self.side_length = side_length

    def __str__(self):
        # Returns a string representation of the square.
        return f"{super().__str__()}, Side Length: {self.side_length}, Area: {self.area()}"

    def area(self):
        # Calculates and returns the area of the square.
        return self.side_length ** 2


class Rectangle(Square):
    # Represents a rectangle shape, inheriting from the Square class.
    def __init__(self, name, has_outline, background_color, length, width, x_coordinate=0, y_coordinate=0):
        """
        Initializes a Rectangle object with the given parameters.
        
        Args:
            name (str): The name of the rectangle.
            has_outline (bool): Indicates whether the rectangle has an outline.
            background_color (str): The background color of the rectangle.
            length (float): The length of the rectangle.
            width (float): The width of the rectangle.
        """
        super().__init__(name, has_outline, background_color, length, x_coordinate, y_coordinate)
        self.width = width

    def __str__(self):
        # Returns a string representation of the rectangle.        
        return f"{super().__str__()}, Width: {self.width}, Area: {self.area()}"

    def area(self):
        # Calculates and returns the area of the rectangle.
        return self.side_length * self.width
    

class Circle(Shape):
    # Represents a circle shape, inheriting from the Shape class.
    
    def __init__(self, name, has_outline, background_color, radius, x_coordinate=0, y_coordinate=0):
        """
        Initializes a Circle object with the given parameters.
        
        Args:
            name (str): The name of the circle.
            has_outline (bool): Indicates whether the circle has an outline.
            background_color (str): The background color of the circle.
            radius (float): The radius of the circle.
        """
        super().__init__(name, has_outline, background_color, x_coordinate, y_coordinate)
        self.radius = radius

    def __str__(self):
        
        # Returns a string representation of the circle.
        
        return f"{super().__str__()}, Radius: {self.radius}, Area: {self.area()}"

    def area(self):
        #Calculates and returns the area of the circle.
        return round(math.pi * self.radius ** 2, 4)
    
class Triangle(Shape):
    
    # Represents a triangle shape, inheriting from the Shape class.
    
    def __init__(self, name, has_outline, background_color, base, height, x_coordinate=0, y_coordinate=0):
        """
        Initializes a Triangle object with the given parameters.
        
        Args:
            name (str): The name of the triangle.
            has_outline (bool): Indicates whether the triangle has an outline.
            background_color (str): The background color of the triangle.
            base (float): The length of the base of the triangle.
            height (float): The height of the triangle.
        """
        super().__init__(name, has_outline, background_color, x_coordinate, y_coordinate)
        self.base = base
        self.height = height

    def __str__(self):
        # Returns a string representation of the triangle.
        return f"{super().__str__()}, Base: {self.base}, Height: {self.height}, Area: {self.area()}"

    def area(self):
        # Calculates and returns the area of the triangle.
        area = 0.5 * self.base * self.height
        return area
    
class Ellipse(Shape):
    # Represents an ellipse shape, inheriting from the Shape class.
    def __init__(self, name, has_outline, background_color, major_axis, minor_axis, x_coordinate=0, y_coordinate=0):
        """
        Initializes an Ellipse object with the given parameters.
        
        Args:
            name (str): The name of the ellipse.
            has_outline (bool): Indicates whether the ellipse has an outline.
            background_color (str): The background color of the ellipse.
            major_axis (float): Length of the major axis.
            minor_axis (float): Length of the minor axis.
            x_coordinate (float): X-coordinate of the center (default is 0).
            y_coordinate (float): Y-coordinate of the center (default is 0).
        """
        super().__init__(name, has_outline, background_color, x_coordinate, y_coordinate)
        self.major_axis = major_axis
        self.minor_axis = minor_axis

    def __str__(self):
        # Returns a string representation of the ellipse.
        return f"{super().__str__()}, Major Axis: {self.major_axis}, Minor Axis: {self.minor_axis}"

    def area(self):
        # Calculates and returns the area of the ellipse.
        return math.pi * self.major_axis * self.minor_axis
    
class Canvas:
    def __init__(self):
        self.shapes = []

    def add_shape(self, shape):
        self.shapes.append(shape)

    def display_shapes(self):
        for shape in self.shapes:
            print(shape)

def main():
    canvas = Canvas()

    # Creating instances of shapes with specific positions
    s = Shape('shape', True, 'yellow', 10, 20)
    sqr1 = Square('square1', False, 'golden', 5, 1, 2)
    sqr2 = Square('square2', True, 'white', 4, 1, 2)
    sqr3 = Square('square3', True, 'grey', 2, 1, 2)
    rtg1 = Rectangle('rectangle1', True, 'green', 3, 4, 5, 10)
    rtg2 = Rectangle('rectangle2', True, 'blue', 2, 4, 15, 20)
    rtg3 = Rectangle('rectangle3', True, 'purple', 3, 5, 45, 30)
    rtg4 = Rectangle('rectangle4', True, 'yellow', 4, 8, 25, 5)
    cir1 = Circle('circle', True, 'red', 3, 2, 4)
    cir2 = Circle('circle', False, 'yellow', 3, 2, 4)
    tri = Triangle('triangle', True, 'blue', 4, 6, 8, 2)
    ellipse = Ellipse('ellipse', True, 'silver', 6, 3, 15, 25)

    # Adding shapes to the canvas
    canvas.add_shape(s)
    canvas.add_shape(sqr1)
    canvas.add_shape(sqr2)
    canvas.add_shape(sqr3)
    canvas.add_shape(rtg1)
    canvas.add_shape(rtg2)
    canvas.add_shape(rtg3)
    canvas.add_shape(rtg4)
    canvas.add_shape(cir1)
    canvas.add_shape(cir2)
    canvas.add_shape(tri)
    canvas.add_shape(ellipse)

    # Displaying shapes on the canvas
    canvas.display_shapes()

if __name__ == "__main__":
    main()
