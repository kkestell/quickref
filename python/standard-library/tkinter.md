```python
import tkinter as tk

# Create a root window
root = tk.Tk()
root.title('My Application')
root.geometry('300x200')

# Create a label
label = tk.Label(root, text='Hello, world!')
label.pack()

# Create a button
def button_callback():
    print('Button clicked')

button = tk.Button(root, text='Click me!', command=button_callback)
button.pack()

# Create a text widget
text = tk.Text(root)
text.insert('1.0', 'Enter text here')
text.pack()

# Create a canvas
canvas = tk.Canvas(root, width=200, height=100)
canvas.pack()

# Draw a rectangle on the canvas
rectangle = canvas.create_rectangle(50, 50, 150, 100, fill='blue')

# Bind mouse click event to the rectangle
def rectangle_click(event):
    canvas.itemconfigure(rectangle, fill='red')

canvas.tag_bind(rectangle, '<Button-1>', rectangle_click)

# Create a menu bar
menu_bar = tk.Menu(root)

# Create a file menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label='New')
file_menu.add_command(label='Open')
file_menu.add_separator()
file_menu.add_command(label='Exit', command=root.destroy)

menu_bar.add_cascade(label='File', menu=file_menu)

# Create a help menu
help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label='About')

menu_bar.add_cascade(label='Help', menu=help_menu)

root.config(menu=menu_bar)

# Start the event loop
root.mainloop()

```
