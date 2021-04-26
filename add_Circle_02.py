from add_Circle import Rectangle
from add_Circle import Square
from add_Circle import Circle

rec1 = Rectangle(3, 4)
rec2 = Rectangle(12, 5)

# print("Выводим прямоугольник:")
# print(rec1.get_area())
# print(rec2.get_area())

square_1 = Square(5)
square_2 = Square(10)

# print("")
# print("Выводим квадрат:")
# print(square_1.get_area_square(), square_2.get_area_square())

circle_1 = Circle(2)
circle_2 = Circle(7)
# print("Выводим круг:")
# print(circle_1.get_area_circle(), circle_2.get_area_circle())


figures = [rec1, rec2, square_1, square_2, circle_1, circle_2]

for figure in figures:
    if isinstance(figure, Square):
        print("Выводим квадрат: ")
        print(figure.get_area_square())
    elif isinstance(figure, Circle):
        print("Выводим круг: ")
        print(figure.get_area_circle())
    else:
        print("Выводим прямоугольник: ")
        print(figure.get_area())