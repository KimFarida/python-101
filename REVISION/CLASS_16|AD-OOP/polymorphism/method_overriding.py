class Shape:
    def area(self):
        pass

    def describe(self):
        print("This is a shape")


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def describe(self):
        print(f"Rectangle with width {self.width} and height {self.height}")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def describe(self):
        print(f"Circle with radius {self.radius}")


# Polymorphic function
def print_shape_info(shape):
    shape.describe()
    print(f"Area: {shape.area()}")


# Usage
shapes = [Rectangle(5, 3), Circle(4)]
for shape in shapes:
    print_shape_info(shape)