'''
Напишите программу, которая принимает на вход координаты двух точек
и находит расстояние между ними в 2D пространстве.
Пример:
- A (3,6); B (2,1) -> 5,09
- A (7,-5); B (1,-1) -> 7,21
'''
x1 = float(input("Введите координату точки A по оси абсцисс X: "))
y1 = float(input("Введите координату точки A по оси ординат Y: "))
x2 = float(input("Введите координату точки B по оси абсцисс X: "))
y2 = float(input("Введите координату точки B по оси ординат Y: "))
import math
c = round (math.sqrt((x1-x2)**2 + (y1-y2)**2), 2)
print(f'Расстояние на координатной плоскости между точками A({x1}, {y1}) и B({x2}, {y2}) = {c}')