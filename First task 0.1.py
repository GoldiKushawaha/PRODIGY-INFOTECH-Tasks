import tkinter as tk
from tkinter import ttk, messagebox

# Conversion functions
def convert_temperature():
    try:
        temp = float(entry_temp.get())
        unit = unit_var.get()

        if unit == "Celsius":
            f = (temp * 9/5) + 32
            k = temp + 273.15
            result.set(f"Fahrenheit: {f:.2f} °F\nKelvin: {k:.2f} K")
        elif unit == "Fahrenheit":
            c = (temp - 32) * 5/9
            k = c + 273.15
            result.set(f"Celsius: {c:.2f} °C\nKelvin: {k:.2f} K")
        elif unit == "Kelvin":
            c = temp - 273.15
            f = (c * 9/5) + 32
            result.set(f"Celsius: {c:.2f} °C\nFahrenheit: {f:.2f} °F")
        else:
            result.set("Please select a valid unit.")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

# GUI setup
window = tk.Tk()
window.title("Temperature Converter")
window.geometry("350x250")
window.configure(bg="#e0f7fa")

# Input label and entry
tk.Label(window, text="Enter Temperature:", bg="#e0f7fa").pack(pady=5)
entry_temp = tk.Entry(window)
entry_temp.pack(pady=5)

# Dropdown for unit selection
tk.Label(window, text="Select Unit:", bg="#e0f7fa").pack(pady=5)
unit_var = tk.StringVar()
unit_dropdown = ttk.Combobox(window, textvariable=unit_var, values=["Celsius", "Fahrenheit", "Kelvin"])
unit_dropdown.pack(pady=5)
unit_dropdown.current(0)

# Convert button
tk.Button(window, text="Convert", command=convert_temperature, bg="#00796b", fg="white").pack(pady=10)

# Result label
result = tk.StringVar()
tk.Label(window, textvariable=result, bg="#e0f7fa", font=("Arial", 12), justify="center").pack(pady=10)

# Run the application
window.mainloop()