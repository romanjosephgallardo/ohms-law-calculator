''' Instructions:
1.	Ask the user what they want to calculate: Voltage, Current, or Resistance.
2.	Based on their choice, prompt the user to input the appropriate values.
3.	Use Ohm's Law to calculate the missing variable and display the result.
4.	Handle cases where division by zero might occur.
'''

# pseudocode

# Ask the user what they want to calculate: Voltage, Current, or Resistance
print("Ohm's Law Calculator: \n"
      "What would you like to calculate? (Choose a number)\n"
      "1. Voltage \n"
      "2. Current \n"
      "3. Resistance")
calc_choice = int(input("Enter your choice: "))

# Based on their choice, prompt the user to input the appropriate values
# Use Ohm's Law to calculate the missing variable and display the result
# Handle cases where division by zero might occur