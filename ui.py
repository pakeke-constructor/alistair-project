

import tkinter as tk

def on_button_click():
    selected_option1 = option_var1.get()
    selected_option2 = option_var2.get()
    result_label.config(text=f"Option 1: {selected_option1}, Option 2: {selected_option2}")

# Create the main application window
root = tk.Tk()
root.title("Tkinter Example with Dropdowns")

# Dropdown options
options1 = ["Option 1A", "Option 1B", "Option 1C"]
options2 = ["Option 2A", "Option 2B", "Option 2C"]

# Create the first dropdown
option_var1 = tk.StringVar()
option_var1.set(options1[0])
dropdown1 = tk.OptionMenu(root, option_var1, *options1)
dropdown1.pack(pady=10)

# Create the second dropdown
option_var2 = tk.StringVar()
option_var2.set(options2[0])
dropdown2 = tk.OptionMenu(root, option_var2, *options2)
dropdown2.pack(pady=5)

# Create a button widget
button = tk.Button(root, text="Show Selection", command=on_button_click)
button.pack(pady=5)

# Create a label to display the selected options
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()

