#Run on ENGR servers or run using python version 2.7.5
#To run type "python jackson_wright_hw1.py", and enter a number when prompted

#Function gets the input from the user and doesn't stop until a valid integer is entered
def getInput():
	userIn = 0
	while(True):
		try:
			#First check to see if its a number
			#Multiplies by 1000 to see if its a decimal
			userIn = int(input("Enter the year to check: ") * 100000)
		except:
			print("Invalid input please try again")

		else:
			#Divides by 1000.0 to get the origional input 
			new = userIn / 100000.0
			
			#If input not divisible by 1 then its a decimal so return error
			#Also has to be a positive year
			if new % 1 == 0 and new > 0:
				return int(new)
			else:
				print("Invalid input plesae try again")


	return

def main():
	
	year = getInput()

	if(year % 4 == 0):
		if(year % 100 == 0):
			if(year % 400 == 0):
				print(str(year) + " is a leap year")

			else:
				print(str(year) + " is not a leap year")

		else:
			print(str(year) + " is a leap year")
	else:
		print(str(year) + " is not a leap year")



main()
