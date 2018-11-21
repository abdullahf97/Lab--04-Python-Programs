print("Abdullah Farooq(18B-104-CS-A)")
print("Program Exercise 1")

#Code for calculation of the quadratic equation
a = eval(input('Enter the value of a: '))
b = eval(input('Enter the value of b: '))
c = eval(input('Enter the value of c: '))
demo = 2*a
if demo == 0:
    print('The equation cannot solve due to the zero division')
else:
    import math
    x1 = (-b+math.sqrt((b**2)-(4*a*c)))/(demo)
    x2 = (-b-math.sqrt((b**2)-(4*a*c)))/(demo)
    print('The two solutions are: ',x1,x2)
