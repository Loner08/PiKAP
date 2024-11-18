from lab_python_oop.rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, side_length, color_name):
        super().__init__(side_length, side_length, color_name)

    @classmethod
    def name(cls):
        return "Квадрат"
    
    def __repr__(self):
        return "Фигура: {}, Цвет: {}, Длина стороны: {}, Площадь: {:.2f}".format(
            self.name(), self.color.color_name, self.width, self.area()
        )
