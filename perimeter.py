#calculate the perimeter of a rectangle 
#perimeter=2(length+width)
def rectangle_perimeter(l,w):
    return (2*(l+w))

l= int(input("Enter length: "))
w= int(input("Enter width: "))
p= rectangle_perimeter(l,w)

print("The perimeter is: ", p)