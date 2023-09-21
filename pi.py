#test code but its wrong
import pi

def square(x):
    return x*x 
r = int (input("enter radius: "))
h = int (input("enter height: "))
v = (pi*(square(r))*h)

print(v)