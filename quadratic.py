import math

a = float(input('Введите a: '))
b = float(input('Введите b: '))
c = float(input('Введите c: '))

D = math.sqrt(b**2-4*a*c)

root1 = (-b + D)/(2*a)
root2 = (-b - D)/(2*a)

print('Решаем уравнение ax^2 + bx + c = 0 с коэффициентами a = {0} b = {1} c = {2}' .format(a,b,c))
print('({0})x^2 + ({1})x + ({2}) = 0' .format(a,b,c))
print('Первый корень =', root1)
print('Второй корень =', root2)
