import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

# Function convert
def convert():
    # convert the distance in miles to km and round to 2 
    distance = round(entry_double.get() * 1.609,2)
    # set the output to the content of distance variable
    output_string.set(f'{distance} km')

# Create a window
window = ttk.Window(themename='darkly')
# Set the title of the window
window.title('Converter')
# Set the size by width x height
window.geometry('400x200')

# Title
'''
Function Label
    - Master -> Container 
    - Text -> Content to the label
    - Font -> Type of Font | Size
'''
title_label = ttk.Label(master=window, text='Miles to Kilometers', font='Roboto 24')
title_label.pack()

# Input Field
input_frame = ttk.Frame(master=window)
# Components to the frame
entry_double=tk.DoubleVar()
entry = ttk.Entry(master=input_frame, textvariable=entry_double)
submit_btn = ttk.Button(master=input_frame, text='Convert', command= convert)
entry.pack(side='left', padx=16)
submit_btn.pack(side='left')
input_frame.pack(pady= 8)

# output
# set a variable for the output
output_string = tk.StringVar()
output_label = ttk.Label(
    master=window, 
    text='Output',
    font='Roboto 16',
    textvariable=output_string)
output_label.pack(pady=8)

# Run the GUI
window.mainloop()