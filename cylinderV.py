#calculate the volume of a cylinder 
#volume = pi*(r)^2*h
def cylinder_volume():
    return (pi*(square(r))*h)

def square(x):
    return x*x 

r = int (input("enter radius: "))
h = int (input("enter height: "))
pi= 22/7
v = cylinder_volume()

print(v)
