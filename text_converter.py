import tkinter as tk

def convert_text():
    input_text = input_textbox.get("1.0", tk.END).strip()
    converted_text = input_text.upper()
    output_textbox.delete("1.0", tk.END)
    output_textbox.insert(tk.END, converted_text)

# Create the main window
root = tk.Tk()
root.title("Text Converter")

# Create a label for input
input_label = tk.Label(root, text="Enter text:")
input_label.pack(pady=5)

# Create a text box for input
input_textbox = tk.Text(root, height=10, width=50)
input_textbox.pack(pady=5)

# Create a button to convert text
convert_button = tk.Button(root, text="Convert to Uppercase", command=convert_text)
convert_button.pack(pady=10)

# Create a label for output
output_label = tk.Label(root, text="Uppercase text:")
output_label.pack(pady=5)

# Create a text box for output
output_textbox = tk.Text(root, height=10, width=50)
output_textbox.pack(pady=5)

# Run the application
root.mainloop()
