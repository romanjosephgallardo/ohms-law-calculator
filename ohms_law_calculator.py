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
if calc_choice == 1:
    voltage = float(input("Enter the voltage: "))
    resistance = float(input("Enter the resistance: "))
    current = voltage / resistance
    print(f"The current is: {current:.3g}A")
elif calc_choice == 2:
    current = float(input("Enter the current: "))
    resistance = float(input("Enter the resistance: "))
    voltage = current * resistance
    print(f"The voltage is: {voltage:.3g}V")
elif calc_choice == 3:
    voltage = float(input("Enter the voltage: "))
    current = float(input("Enter the current: "))
    resistance = voltage / current
    print(f"The resistance is: {resistance:.3g}Ω")
else:
    print("Invalid input, please enter a number from 1-3.")

# Use Ohm's Law to calculate the missing variable and display the result
# Handle cases where division by zero might occur