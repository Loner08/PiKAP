import sys
import math

def get_coef(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Некорректное значение. Попробуйте снова.")

def reshen(a, b, c):
    discrim = b ** 2 - 4 * a * c
    print(f"Дискриминант: {discrim}")
    
    if discrim > 0:
        y1 = (-b + math.sqrt(discrim)) / (2 * a)
        y2 = (-b - math.sqrt(discrim)) / (2 * a)
        print(f"Два действительных корня для y: y1 = {y1}, y2 = {y2}")
        if y1 >= 0:
            x1 = math.sqrt(y1)
            x2 = -math.sqrt(y1)
            print(f"Корни для x при y1: x1 = {x1}, x2 = {x2}")
        if y2 >= 0:
            x3 = math.sqrt(y2)
            x4 = -math.sqrt(y2)
            print(f"Корни для x при y2: x3 = {x3}, x4 = {x4}")
    elif discriminant == 0:
        y = -b / (2 * a)
        print(f"Один действительный корень для y: y = {y}")
        if y >= 0:
            x1 = math.sqrt(y)
            x2 = -math.sqrt(y)
            print(f"Корни для x: x1 = {x1}, x2 = {x2}")
        else:
            print("Действительных корней для x нет.")
    else:
        print("Действительных корней для уравнения нет.")

def get_coefs():
    if len(sys.argv) == 4:
        try:
            a = float(sys.argv[1])
            b = float(sys.argv[2])
            c = float(sys.argv[3])
        except ValueError:
            print("Некорректные значения в командной строке. Введите коэффициенты вручную.")
            a = get_coef("Введите коэффициент A: ")
            b = get_coef("Введите коэффициент B: ")
            c = get_coef("Введите коэффициент C: ")
    else:
        a = get_coef("Введите коэффициент A: ")
        b = get_coef("Введите коэффициент B: ")
        c = get_coef("Введите коэффициент C: ")
    
    return a, b, c

def main():
    print("Решение биквадратного уравнения: Ax^4 + Bx^2 + C = 0")
    
    a, b, c = get_coefs()

    if a == 0:
        print("Коэффициент A не может быть равен 0 (это не биквадратное уравнение).")
    else:
        reshen(a, b, c)

if __name__ == "__main__":
    main()
