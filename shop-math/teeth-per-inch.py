#
#
### Program that determines the teeth per inch based on material.
#
#
from math import ceil


#Function that divides 3 by the material thickness. 
def teeth_per_inch (material_thickness):
	tpi = ceil((3/material_thickness))
	print("{0} teeth per inch is required for {1} thick material.\n".format(tpi, material_thickness))

#Function that requires the thickness of the material, the condition is whether or not the measurement is imperial or metric.
def main():
	measure = input("is the measurement in imperial (1) or metric (2): ")
	if int(measure) == 2:
		material_thickness = float(input("Please enter the thickness of the material in metric: "))
		teeth_per_inch(material_thickness)
	if int(measure) == 1:
		top_fraction = int(input("Please enter the numerator or top number: "))
		bottom_fraction = int(input("Please enter the denominator or bottom number: "))
		material_thickness = top_fraction/bottom_fraction
		teeth_per_inch(material_thickness)
		
main()
