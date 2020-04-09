import math
#Here we prompt the user for input
print("Enter the radius of the sphere:", end = ' ')

#We read that input cast it to a float and store it in radius
radius = float(input())

#These are the equations to find the volume and area, stored respectively
volume = (4/3)*math.pi*pow(radius,3)
area = 4*math.pi*pow(radius,2)

#We then print the output in the correct format
print("The volume is: ",volume)
print("The surface area is: ", area)