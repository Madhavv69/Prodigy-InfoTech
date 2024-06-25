import tkinter as tk
from tkinter import messagebox

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit + 459.67) * 5/9

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin * 9/5) - 459.67

def convert_temperature(value, unit):
    try:
        value = float(value)
        if unit == "C":
            fahrenheit = celsius_to_fahrenheit(value)
            kelvin = celsius_to_kelvin(value)
            return f"{value:.2f}°C is {fahrenheit:.2f}°F and {kelvin:.2f}K"
        elif unit == "F":
            celsius = fahrenheit_to_celsius(value)
            kelvin = fahrenheit_to_kelvin(value)
            return f"{value:.2f}°F is {celsius:.2f}°C and {kelvin:.2f}K"
        elif unit == "K":
            celsius = kelvin_to_celsius(value)
            fahrenheit = kelvin_to_fahrenheit(value)
            return f"{value:.2f}K is {celsius:.2f}°C and {fahrenheit:.2f}°F"
        else:
            return "Invalid unit of measurement. Please enter C, F, or K."
    except ValueError:
        return "Invalid input. Please enter a numeric value."

class TemperatureConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Temperature Conversion Program")
        self.root.geometry("400x300")  # Set window size to 400x300

        self.label = tk.Label(root, text="Enter temperature value and select the unit of measurement:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(root)
        self.entry.pack(pady=5)

        self.unit_var = tk.StringVar(value="C")
        self.celsius_radio = tk.Radiobutton(root, text="Celsius", variable=self.unit_var, value="C")
        self.celsius_radio.pack(pady=2)
        self.fahrenheit_radio = tk.Radiobutton(root, text="Fahrenheit", variable=self.unit_var, value="F")
        self.fahrenheit_radio.pack(pady=2)
        self.kelvin_radio = tk.Radiobutton(root, text="Kelvin", variable=self.unit_var, value="K")
        self.kelvin_radio.pack(pady=2)

        self.convert_button = tk.Button(root, text="Convert", command=self.convert)
        self.convert_button.pack(pady=10)

        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=5)

    def convert(self):
        value = self.entry.get()
        unit = self.unit_var.get()
        result = convert_temperature(value, unit)
        self.result_label.config(text=result)

if __name__ == "__main__":
    root = tk.Tk()
    app = TemperatureConverterApp(root)
    root.mainloop()
