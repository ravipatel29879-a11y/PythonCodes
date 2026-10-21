import math

STUDENT_ID = 32

class Figure:
    def area(self):
        return 0

class Circle(Figure):
    def __init__(self, circle_radius):
        self.circle_radius = circle_radius

    def area(self):
        return math.pi * (self.circle_radius ** 2)

class Rectangle(Figure):
    def __init__(self, rect_length, rect_width):
        self.rect_length = rect_length
        self.rect_width = rect_width

    def area(self):
        return self.rect_length * self.rect_width

# Radius personalisation: student_id % 4 + 2
radius_value = STUDENT_ID % 4 + 2

figure_list = [
    Circle(radius_value),
    Rectangle(6, 8),
    Circle(5),
    Rectangle(4, 9)
]

print(f"Custom Circle Radius: {radius_value}\n")

for index, figure in enumerate(figure_list, 1):
    print(
        f"Figure {index} ({type(figure).__name__}) Area: {figure.area():.2f}"
    )