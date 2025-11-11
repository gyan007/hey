import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Movable Rectangle")
root.geometry("400x300")

# Create Canvas
canvas = tk.Canvas(root, width=400, height=300, bg="white")
canvas.pack()

# Create rectangle
rect = canvas.create_rectangle(100, 100, 200, 150, fill="skyblue", outline="black")

# Variables to store position
start_x = start_y = 0

# --- Functions to move rectangle ---

def on_press(event):
    """Record mouse position when clicked"""
    global start_x, start_y
    start_x, start_y = event.x, event.y

def on_drag(event):
    """Move the rectangle as the mouse moves"""
    global start_x, start_y
    dx = event.x - start_x
    dy = event.y - start_y
    canvas.move(rect, dx, dy)
    start_x, start_y = event.x, event.y

# --- Bind mouse events ---
canvas.tag_bind(rect, "<Button-1>", on_press)     # When rectangle is clicked
canvas.tag_bind(rect, "<B1-Motion>", on_drag)     # While mouse is dragged

# Run the app
root.mainloop()
