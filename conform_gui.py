"""
This module creates a GUI application using Tkinter for managing GCP projects.
The main window is non-resizable and set to half the screen size. It includes
a dropdown list for selecting GCP projects and a login button.

Modules:
    tkinter: Provides classes and functions for creating a GUI application.
    json: Provides functions for working with JSON data.

Functions:
    None

Classes:
    None

Exceptions:
    None
"""

import tkinter as tk
from tkinter import ttk
import json

# Load data from gcp_projects.json
with open('gcp_projects.json', 'r', encoding='utf-8') as file:
    projects = json.load(file)

# Create the main window
root = tk.Tk()
root.title("Conform GUI")

# Get screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate half of the screen width and height
half_width = screen_width // 2
half_height = screen_height // 2

# Set the geometry of the main window to half of the screen size
root.geometry(f"{half_width}x{half_height}")

# Make the window non-resizable
root.resizable(False, False)

# Create a frame for the first row
frame = tk.Frame(root)
frame.pack(pady=10)

# Create a dropdown list (combobox)
project_var = tk.StringVar()
project_combobox = ttk.Combobox(frame, textvariable=project_var)
project_combobox['values'] = projects
project_combobox.pack(side=tk.LEFT, padx=5)

# Create a login button
login_button = tk.Button(frame, text="Login")
login_button.pack(side=tk.RIGHT, padx=5)

# Create a frame for the table and refresh button
frame2 = tk.Frame(root)
frame2.pack(pady=10)

# Create a table (Treeview)
columns = ('#1', '#2', '#3')
catalogue_tree = ttk.Treeview(frame2, columns=columns, show='headings')
catalogue_tree.heading('#1', text='Column 1')
catalogue_tree.heading('#2', text='Column 2')
catalogue_tree.heading('#3', text='Column 3')
catalogue_tree.pack(side=tk.LEFT, padx=5)

# Create a generate button
refresh_button = tk.Button(frame2, text="Refresh")
refresh_button.pack(side=tk.RIGHT, padx=5)

# Create a frame for the table and generate button
frame3 = tk.Frame(root)
frame3.pack(pady=10)

# Create a table (Treeview)
columns = ('#1', '#2', '#3')
conform_tree = ttk.Treeview(frame3, columns=columns, show='headings')
conform_tree.heading('#1', text='Column 1')
conform_tree.heading('#2', text='Column 2')
conform_tree.heading('#3', text='Column 3')
conform_tree.pack(side=tk.LEFT, padx=5)

# Create a generate button
generate_button = tk.Button(frame3, text="Generate")
generate_button.pack(side=tk.RIGHT, padx=5)

# Run the application
root.mainloop()
