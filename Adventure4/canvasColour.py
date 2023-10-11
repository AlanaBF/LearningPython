import tkinter as tk
window = tk.Tk()

colour = "#00FFFF"

canvas = tk.Canvas(window, height = 300, width = 300, bg=colour)

canvas.pack()
window.mainloop()