import math
from lab_python_oop.figure import Figure
from lab_python_oop.color import Color

class Circle(Figure):
    def __init__(self, radius, color_name):
        self.radius = radius
        self.color = Color(color_name)

    @classmethod
    def name(cls):
        return "Круг"

    def area(self):
        return math.pi * (self.radius ** 2)

    def __repr__(self):
        return "Фигура: {}, Цвет: {}, Радиус: {}, Площадь: {:.2f}".format(
            self.name(), self.color.color_name, self.radius, self.area()
        )
