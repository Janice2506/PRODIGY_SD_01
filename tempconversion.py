def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def convert_temperature(value, unit):
    if unit == 'C':
        fahrenheit = celsius_to_fahrenheit(value)
        kelvin = celsius_to_kelvin(value)
        print(f"{value}°C = {fahrenheit:.2f}°F = {kelvin:.2f}K")
    elif unit == 'F':
        celsius = fahrenheit_to_celsius(value)
        kelvin = fahrenheit_to_kelvin(value)
        print(f"{value}°F = {celsius:.2f}°C = {kelvin:.2f}K")
    elif unit == 'K':
        celsius = kelvin_to_celsius(value)
        fahrenheit = kelvin_to_fahrenheit(value)
        print(f"{value}K = {celsius:.2f}°C = {fahrenheit:.2f}°F")
    else:
        print("Invalid unit. Please enter C for Celsius, F for Fahrenheit, or K for Kelvin.")

# Main program
value = float(input("Enter the temperature value: "))
unit = input("Enter the unit (C for Celsius, F for Fahrenheit, K for Kelvin): ").upper()

convert_temperature(value, unit)
