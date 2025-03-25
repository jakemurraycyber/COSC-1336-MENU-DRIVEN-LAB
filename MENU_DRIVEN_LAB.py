##########################################################
#                                                        #
#   This is a menu-driven program converts temperatures  #
#	between celsius and fahrenheit.                      #
#                                                        #
#   Author:  Jake Murray                                 #
#                                                        #
#   Date:    March 21, 2025                              #
#                                                        #
#   Version: 1.0.0                                       #
#                                                        #
##########################################################

# Formulas for reference
# CELSIUS_TO_FAHRENHEIT = cTemp * 1.8 + DELTA
# FAHRENHEIT_TO_CELSIUS = (fTemp - DELTA) * (5/9)

# Global Constant
DELTA = 32

# Main Loop
def main():
	welcomeMsg = "Welcome to your very own temperature converter!"
	print(welcomeMsg)
	displayMenu()
	

	# Main decision loop, with error exception for invalid input
	while True:
		try:
			menuSelection = int(input("\nPlease make a selection from the menu:\t"))
			if menuSelection == 1:
				convertCelsiusToFahrenheit()
			elif menuSelection == 2:
				convertFahrenheitToCelsius()
			elif menuSelection == 3:
				print('Goodbye')
				break
			else:
				print("That is not a valid option. Please try again...")
			displayMenu()
		except ValueError:
			print("What you entered was invalid. Please try again.")
			displayMenu()

# Menu display function
def displayMenu():
	print("\nSelect 1 to convert celsius to fahrenheit.")
	print("Select 2 to convert fahrenheit to celsius.")
	print("Select 3 to exit the program.\n")

# Function for celsius to fahrenheit, with error exception for invalid input
def convertCelsiusToFahrenheit():
    print('You chose to convert a temperature in Celsius to Fahrenheit.')
    while True:
        try:
            cTemp = float(input("Please enter the temperature in Celsius:\n> "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    temp = cTemp * 1.8 + DELTA
    print(f"{cTemp:.1f} degrees Celsius is {temp:.1f} degrees Fahrenheit.")

# Function for fahrenheit to celsius, with error exception for invalid input
def convertFahrenheitToCelsius():
    print('You chose to convert a temperature in Fahrenheit to Celsius.')
    while True:
        try:
            fTemp = float(input("Please enter the temperature in Fahrenheit:\n> "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    temp = (fTemp - DELTA) * (5/9)
    print(f"{fTemp:.1f} degrees Fahrenheit is {temp:.1f} degrees Celsius.")
	
if __name__ == '__main__':
	main()
