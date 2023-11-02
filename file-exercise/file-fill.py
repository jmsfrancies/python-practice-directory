
#file fill program that requires the total number of items to add, 
#the name of each item, and their cost.


def main ():
	with open("item-list.txt", "w") as fname:
		fname.write(("{0} {1}\n").format("Item Name", "Item Cost"))
		how_many_items = int(input("How many items are you adding?  "))
		for i in range(how_many_items):
			i = str(input("Name of the item:  "))
			j = round(float(input("Cost of the item:  ")),2)	
			fname.write(("%s   %s")%(str(i),str(j)))
			fname.write("\n")
	fname.close()
main()	
