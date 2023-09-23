#impotr math package to use math.pi for the value of PI 
#volume = pi*(r)^2*h
import math
def cylinder_volume():
    return (math.pi*(pow(r,2))*h)

def square(x):
    return x*x 

r = int (input("enter radius: "))
h = int (input("enter height: "))
#calculate the volume of a cylinder 
v = cylinder_volume()

print("The volume of the cylinder is: ", v)
