#Run on ENGR servers or run using python version 2.7.5
#To run type "python jackson_wright_hw1.py", and enter a number when prompted

def main():
	year = input("Enter the year to check (Integer): ")
	
	if(year % 4 == 0):
		if(year % 100 == 0):
			if(year % 400 == 0):
				print(str(year) + " is a leap year")

			else:
				print(str(year) + " is not a leap year")

		else:
			print(str(year) + " is a leap year")



main()
