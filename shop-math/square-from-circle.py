#
#
### This is the program to determine the maximum square size from a rounded billet.
#
#

def main():
	circle_or_square = int(input("Do you need to calculate the square size or circle diameter (1/2): "))
	if circle_or_square == 1:
		circle_diameter = float(input("Please enter the circle's diameter: "))
		square_side_length = round((circle_diameter * .7071),3)
		print("A circle with a {0} diameter can produce a square with the side length of {1}".format(circle_diameter, square_side_length))
	if circle_or_square == 2:
		square_side = float(input("Please enter the square side's size: "))
		circle_diameter = round((square_side / .7071),3)
		print("A square with a {0} side length requires a circle with a diameter of {1}".format(square_side,circle_diameter))
		
		
main()
