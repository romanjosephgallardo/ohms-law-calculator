''' Instructions:
1.	Ask the user what they want to calculate: Voltage, Current, or Resistance.
2.	Based on their choice, prompt the user to input the appropriate values.
3.	Use Ohm's Law to calculate the missing variable and display the result.
4.	Handle cases where division by zero might occur.
'''

# Ohm's Law Calculator:

# Ask the user what they want to calculate: Voltage, Current, or Resistance
print("Ohm's Law Calculator: \n"
      "What would you like to calculate? (Choose a number)\n"
      "1. Voltage \n"
      "2. Current \n"
      "3. Resistance")
try:
    calc_choice = int(input("Enter your choice: "))
except ValueError:
    print("Error: Invalid input. Please enter a number.")

# Based on their choice, prompt the user to input the appropriate values
if calc_choice == 1:
    try:
        voltage = float(input("Enter the voltage: "))
        resistance = float(input("Enter the resistance: "))
        current = voltage / resistance
        print(f"The current is: {current:.3g}A")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ValueError:
        print("Error: Invalid input. Please enter a number.")
    
elif calc_choice == 2:
    try:
        current = float(input("Enter the current: "))
        resistance = float(input("Enter the resistance: "))
        voltage = current * resistance
        print(f"The voltage is: {voltage:.3g}V")
    except ValueError:
        print("Error: Invalid input. Please enter a number.")
elif calc_choice == 3:
    try:
        voltage = float(input("Enter the voltage: "))
        current = float(input("Enter the current: "))
        resistance = voltage / current
        print(f"The resistance is: {resistance:.3g}Ω")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ValueError:
        print("Error: Invalid input. Please enter a number.")
else:
    print("Invalid input, please enter a number from 1-3.")

# Use Ohm's Law to calculate the missing variable and display the result
# Handle cases where division by zero might occur