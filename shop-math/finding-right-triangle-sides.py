# This is for right side triangles and finding the 
# size lengths of the hypotenuse, opposite, and adjacent.

from decimal import *

#Function to determine the opposite.
def determining_the_opposite(hypotenuse, adjacent):
	opposite = Decimal(((hypotenuse ** 2)-(adjacent ** 2)))
	print("The opposite is: {:.3f}".format(opposite.sqrt()))

#Function to determine the adjacent.	
def determining_the_adjacent(hypotenuse, opposite):
	adjacent = Decimal(((hypotenuse ** 2)-(opposite ** 2)))
	print("The adjacent is: {:.3f}".format(adjacent.sqrt()))

#Function to determine the hypotenuse.	
def determining_the_hypotenuse(adjacent, opposite):
	hypotenuse = Decimal(((adjacent ** 2) + (opposite ** 2)))
	print("The hypotenuse is: {:.3f}".format(hypotenuse.sqrt()))



#Function that provides options on calculating the opposite, adjacent, and hypotenuse.
def main():
	calculate = str(input("Enter (a) for opposite, (b) for adjacent, and (c) for hypotenuse: "))
	if calculate in "aA":
		hypotenuse = float(input("Enter the length of the hypotenuse: "))
		adjacent = float(input("Enter the length of the adjacent: "))
		determining_the_opposite(hypotenuse, adjacent)
	if calculate in "bB":
		hypotenuse = float(input("Enter the length of the hypotenuse: ")) 
		opposite = float(input("Enter the length of the opposite: "))
		determining_the_adjacent(hypotenuse, opposite)
	if calculate in "cC":
		adjacent = float(input("Enter the length of the adjacent: "))
		opposite = float(input("Enter the length of the opposite: "))
		determining_the_hypotenuse(adjacent, opposite)
				
main()
