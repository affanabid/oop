# from abc import ABC, abstractmethod

# # Abstract class representing a Shape
# class Shape(ABC):
#     def __init__(self, name):
#         self.name = name
    
#     @abstractmethod
#     def area(self):
#         pass

# # Concrete classes extending the Shape class
# class Circle(Shape):
#     def __init__(self, name, radius):
#         super().__init__(name)
#         self.radius = radius
    
#     def area(self):
#         return 3.14 * self.radius * self.radius

# class Rectangle(Shape):
#     def __init__(self, name, width, height):
#         super().__init__(name)
#         self.width = width
#         self.height = height
    
#     def area(self):
#         return self.width * self.height

# # Usage of the Shape hierarchy
# circle = Circle("Circle", 5)
# rectangle = Rectangle("Rectangle", 4, 6)

# print(f"Area of {circle.name}: {circle.area()}")       # Output: Area of Circle: 78.5
# print(f"Area of {rectangle.name}: {rectangle.area()}") # Output: Area of Rectangle: 24

try:
    # Code that may raise an exception
    x = int(input("Enter a number: "))
    result = 10 / x
    print("Result:", result)

except ValueError:
    print("Please enter a valid number.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

except Exception as e:  # Catching any other exception
    print("An error occurred:", e)

finally:
    print("Execution completed.")  # This block executes whether an exception occurred or not
