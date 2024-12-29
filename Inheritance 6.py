from typing import final
import math
class ShapeArea:
    def calculate_area_rectangle(self, length, width):
        return length * width

    def calculate_area_square(self, side):
        return side * side

    def calculate_area_circle(self, radius):
        return math.pi * radius * radius

@final
class ShapePerimeter(ShapeArea):
    def calculate_perimeter_rectangle(self, length, width):
        return 2 * (length + width)

    def calculate_perimeter_square(self, side):
        return 4 * side

    def calculate_circumference_circle(self, radius):
        return 2 * math.pi * radius
class DisplayResults(ShapePerimeter):
    def display_results(self, length, width, side, radius):
        area_rectangle = self.calculate_area_rectangle(length, width)
        area_square = self.calculate_area_square(side)
        area_circle = self.calculate_area_circle(radius)
        perimeter_rectangle = self.calculate_perimeter_rectangle(length, width)
        perimeter_square = self.calculate_perimeter_square(side)
        circumference_circle = self.calculate_circumference_circle(radius)
        print(f"Rectangle: Length = {length}, Width = {width}")
        print(f"Area of Rectangle: {area_rectangle}")
        print(f"Perimeter of Rectangle: {perimeter_rectangle}")
        print()

        print(f"Square: Side = {side}")
        print(f"Area of Square: {area_square}")
        print(f"Perimeter of Square: {perimeter_square}")
        print()

        print(f"Circle: Radius = {radius}")
        print(f"Area of Circle: {area_circle}")
        print(f"Circumference of Circle: {circumference_circle}")
length = 5
width = 3
side = 4
radius = 7
shape = DisplayResults()
shape.display_results(length, width, side, radius)