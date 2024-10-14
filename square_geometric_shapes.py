def squares():

    print("Введите название геометричееской фигуры, площадь которой хотите найти (название в верхнем регистре)")
    shaep = input()

    while 1:
        if shaep == "Квадрат":
            print("Введите сторону квадрата")
            side = int(input())
            square = side * side
            print("Площадь квадрата со стороной", side , "см =", square, "см^2")
            break
        elif shaep == "Треугольник":
            print("Введите значение длинны высоты треугольника")
            height = int(input())
            print("Введите значение длинны стороны, к которой проведена высота")
            side = int(input())
            square =  (height * side)  // 2
            print("Площадь треугольника, с высотой", height ,"см и стороной", side, "см =", square, "см")
            break
        elif shaep == "Прямоугольник":
            print("Введите значение длинны стороны a прямоугольника")
            a = int(input())
            print("Введите значение длинны стороны b прямоугольника")
            b = int(input())
            square = a * b
            print("Площадь прямоугольника со сторонами", a ,"см и", b ,"см =",square , "см")
            break
        else:
            print("Запрос не распознан, попробуйте ещё раз")
            shaep = input()

squares()