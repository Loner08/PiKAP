from lab_python_oop.figure import Figure
from lab_python_oop.color import Color

class Rectangle(Figure):
    def __init__(self, width, height, color_name):
        self.width = width
        self.height = height
        self.color = Color(color_name)

    @classmethod
    def name(cls):
        return "Прямоугольник"

    def area(self):
        return self.width * self.height

    def __repr__(self):
        return "Фигура: {}, Цвет: {}, Ширина: {}, Высота: {}, Площадь: {:.2f}".format(
            self.name(), self.color.color_name, self.width, self.height, self.area()
        )
