# define global variables
FAHRENHEIT_TO_CELSIUS_FACTOR =  5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

# define a function to perform this conversion
def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    # convert global var to local
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    # return the conversion
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# prompt the user for temperature
temperature = float(input("Enter temperature to convert: "))
tempType = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().lower()

# use match case
match tempType:
    case "C" | "c":
        print(f"{temperature}°C is",convert_to_celsius(temperature),"°F")
    case "F" | "f":
        print(f"{temperature}°F is",convert_to_fahrenheit(temperature),"°C")
    case _:
        print("Invalid temperature. Please enter a numeric value.")


