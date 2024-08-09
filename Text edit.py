import tkinter as tk
from tkinter import filedialog, messagebox

# Function to open a file
def open_file():
    file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "r") as file:
            text_area.delete(1.0, tk.END)  # Clear the current text
            text_area.insert(tk.END, file.read())  # Insert the file content

# Function to save the current file
def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(text_area.get(1.0, tk.END))  # Save the current text to the file

# Function to exit the editor
def exit_editor():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()

# Setting up the main application window
root = tk.Tk()
root.title("Simple Text Editor")

# Creating the text area widget
text_area = tk.Text(root, undo=True)
text_area.pack(fill=tk.BOTH, expand=1)

# Creating the menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Adding file menu options
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_editor)

# Running the application
root.mainloop()
