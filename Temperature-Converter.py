#Setting up the application window
window = Tk()
window.title("Temperature Converter")
window.geometry("800x500")  # Adjusted window size
window.resizable(False, False)  # Disable resizing
window.configure(bg="#3a3f44")  # Background color (grayish blue)

#Variables
temperature = StringVar()
result = StringVar()

#Conversion functions
def celsius_to_fahrenheit():
    try:
        celsius = float(temperature.get())
        fahrenheit = (celsius * 9/5) + 32
        result.set(f"{fahrenheit:.2f} °F")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number!")

def fahrenheit_to_celsius():
    try:
        fahrenheit = float(temperature.get())
        celsius = (fahrenheit - 32) * 5/9
        result.set(f"{celsius:.2f} °C")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number!")

#User Interface
Label(window, text="Temperature Converter", font=("Arial", 16, "bold"), bg="#3a3f44", fg="white").pack(pady=20)

Label(window, text="Enter Temperature:", font=("Arial", 12), bg="#3a3f44", fg="white").place(relx=0.5, rely=0.3, anchor="center")
Entry(window, textvariable=temperature, font=("Arial", 12), width=20).place(relx=0.5, rely=0.4, anchor="center")

#Centered Buttons
Button(window, text="Convert to Fahrenheit", font=("Arial", 10), width=20, height=2, command=celsius_to_fahrenheit).place(relx=0.5, rely=0.55, anchor="center")
Button(window, text="Convert to Celsius", font=("Arial", 10), width=20, height=2, command=fahrenheit_to_celsius).place(relx=0.5, rely=0.7, anchor="center")

Label(window, text="Result:", font=("Arial", 12), bg="#3a3f44", fg="white").place(relx=0.5, rely=0.85, anchor="center")
Label(window, textvariable=result, font=("Arial", 12, "bold"), bg="#3a3f44", fg="white").place(relx=0.5, rely=0.9, anchor="center")

#Run the application
window.mainloop()
