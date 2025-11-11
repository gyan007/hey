import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Rectangle Example")
root.geometry("400x300")

# Create a Canvas widget (where shapes can be drawn)
canvas = tk.Canvas(root, width=400, height=300, bg="white")
canvas.pack()

# Draw rectangle → coordinates: (x1, y1, x2, y2)
canvas.create_rectangle(50, 50, 250, 150, fill="skyblue", outline="black", width=2)

# Run the Tkinter event loop
root.mainloop()
