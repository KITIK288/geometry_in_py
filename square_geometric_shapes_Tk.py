import tkinter as tk
from tkinter import messagebox


def calculate_area():
    shape = shape_entry.get()

    if shape == "Квадрат":
        side = int(side_entry.get())
        square = side * side
        messagebox.showinfo("Результат", f"Площадь квадрата со стороной {side} см = {square} см²")

    elif shape == "Треугольник":
        height = int(height_entry.get())
        side = int(side_entry.get())
        square = (height * side) // 2
        messagebox.showinfo("Результат",
                            f"Площадь треугольника с высотой {height} см и стороной {side} см = {square} см²")

    elif shape == "Прямоугольник":
        a = int(side_entry.get())
        b = int(height_entry.get())
        square = a * b
        messagebox.showinfo("Результат", f"Площадь прямоугольника со сторонами {a} см и {b} см = {square} см²")

    else:
        messagebox.showerror("Ошибка", "Запрос не распознан, попробуйте ещё раз")


root = tk.Tk()
root.title("Расчет площади")

tk.Label(root, text="Введите название геометрической фигуры (Квадрат, Треугольник, Прямоугольник):").pack()
shape_entry = tk.Entry(root)
shape_entry.pack()

tk.Label(root, text="Введите длину стороны (или высоты):").pack()
side_entry = tk.Entry(root)
side_entry.pack()

tk.Label(root, text="Введите длину второй стороны (если необходимо):").pack()
height_entry = tk.Entry(root)
height_entry.pack()

calculate_button = tk.Button(root, text="Рассчитать площадь", command=calculate_area)
calculate_button.pack()

root.mainloop()
