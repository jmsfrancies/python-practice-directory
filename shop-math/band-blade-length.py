#
#
### Program to determine band saw blade length
#
#

def main():
	diameter = float(input("Please enter the diameter of a wheel: "))
	center_distance = float(input("Please enter the center distance between both wheels: "))
	#pi is represented by 3.142
	band_length = round((2*center_distance)+(3.142 * diameter),3)
	print(band_length)
main()
