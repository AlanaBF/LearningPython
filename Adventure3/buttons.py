import tkinter as tk
window = tk.Tk()

# count=0

# def buttonClick():
    
#     global count
#     count = count + 1
#     button.config(text=str(count))
#     print ("Beep!")


def changeString():
    stringToCopy = entry.get()
    stringToCopy = stringToCopy[::-1]
    entry.delete(0, tk.END)
    entry.insert(0, stringToCopy)


entry = tk.Entry(window)
button = tk.Button(window, text="Change", command=changeString)

entry.pack()
button.pack()

window.mainloop()
