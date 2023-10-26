#
#Function that writes the quote to the quick practice text file.
#
def write_to_file():
	fname = open("quick-practice.txt", "w")
	quote = str(input("Please enter a phrase to write to the quick practice text file: "))
	fname.write(quote)
	fname.close()


def main():
#file to search for the vowel count
	fname = open("quick-practice.txt", "r")
#total is the variable that performs the incremental count- 
#for each vowel within the quote string
	total = 0

# for loop that performs the search for each vowel
	for i in fname.read():
		if i in "aeiouAEIOU":
			total = total + 1
			print("Vowel: {0} Count: {1}".format(i,total))
	print("Total Vowels Are: %d"%(total))
	fname.close()

#
#function calls
#
write_to_file()
main()



