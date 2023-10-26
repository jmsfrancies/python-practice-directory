"""
This program will determine the cubic feet per minute of an electric heater.
"""

def main():
	watts = int(input("What is the wattage rating of your heater: "))
	temperature_difference = float(input("What is the temperature difference: "))
	btus = (watts * 3.41)
	cfm = round((btus)/(temperature_difference *1.08),2)
	print("The cubic feet per minute of a {0:,} btus \nelectric furnace with a {1} degrees Fahrenheit \ndifference is: {2:,}".format(btus,temperature_difference,cfm))

main()
