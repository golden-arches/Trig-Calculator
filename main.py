import tkinter as tk
from math import *


def evaluate(event):
    res.configure(text="Result: " + str(eval(entry.get())))


def distance(x1, x2, y1, y2):
    return sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))


def circumference(radius):
    return 3.14 * 2 * radius


def cir(radius):
    return 3.14 * 2 * radius


def areaSphere(radius):
    return 4 * 3.14 * (radius ** 2)


def volumeSphere(radius):
    return 4 / 3 * 3.14 * (radius ** 3)


def areaSquare(w, h):
    return w * h


def midpoint(x1, x2, y1, y2):
    return (str(((x2 + x1) / 2)) + ", " + str(((y2 + y1) / 2)))

def areaTriangle(base, height):
    return (0.5* (base * height))

def paramSquare(side1, side2, side3, side4):
    return side1 + side2 +side3 + side4

def pathaTherom(a,b):
    answer = a**2 + b**2
    return sqrt(answer)

def areaCircle(radius):
    return 3.14 * radius**2

def rectangularPrisimArea(length, width, height):
    return length * width * height

def cubeArea(side):
    return 6 * side*2


functions = ["distance(x1,x2,y1,y2)",
             "circumference(radius) (or cir(radius))",
             "areaSphere(radius)",
             "volumeSphere(radius)",
             "areaSquare(width, height)",
             "midpoint(x1,x2,y1,y1)",
             "areaTriangle(base, height)",
             "paramSquare(side1, side2, side3, side4) (parameterSquare)",
             "pathaTherom(a, b) (pathagareanTherom)",
             "areaCircle(radius)",
             "rectangularPrisimArea(length, width, height)",
             "cubeArea(side)"]

window = tk.Tk()

window.geometry("640x860")

window.iconbitmap('window.ico')
window.title('Trig Calcuator')

tk.Label(window, text="Your Expression:", font=('Helvetica', 18, 'bold')).pack()

entry = tk.Entry(window, width=40)
entry.bind("<Return>", evaluate)
entry.pack()

res = tk.Label(window, font=('Helvetica', 11, 'bold'))
res.pack()
tk.Label(text="\n").pack()
for b in functions:
    tk.Label(text=b + "\n").pack()
window.mainloop()
