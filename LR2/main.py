from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square

def main():
    N = 5  # Подставьте значение N согласно вашему варианту

    rectangle = Rectangle(N, N, "синий")
    circle = Circle(N, "зеленый")
    square = Square(N, "красный")

    print(str(rectangle))
    print(str(circle))
    print(str(square))

if __name__ == "__main__":
    main()
