# temperatura.py

def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_a_kelvin(celsius):
    return celsius + 273.15

def kelvin_a_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_a_kelvin(fahrenheit):
    return celsius_a_kelvin(fahrenheit_a_celsius(fahrenheit))

def kelvin_a_fahrenheit(kelvin):
    return celsius_a_fahrenheit(kelvin_a_celsius(kelvin))
