import math

a = float(input('Enter a: '))
b = float(input('Enter b: '))
c = float(input('Enter c: '))

D = math.sqrt(b**2-4*a*c)

root1 = (-b + D)/(2*a)
root2 = (-b - D)/(2*a)

print('We are solving equation ax^2 + bx + c = 0') 
print('with coeffs a = {0} b = {1} c = {2}' .format(a,b,c))
print('({0})x^2 + ({1})x + ({2}) = 0' .format(a,b,c))
print('The First root =', root1)
print('The Second root =', root2)
