import Tkinter as tk

def getCagePlot:
    

master = tk.Tk()

v = tk.IntVar()

tk.Radiobutton(master, text="Cage One", variable=v, command=getCagePlot, value=1)
tk.Radiobutton(master, text="Cage Two", variable=v, command=getCagePlot, value=2)
tk.Radiobutton(master, text="Cage Three", variable=v, command=getCagePlot, value=3)
tk.Radiobutton(master, text="Cage Four", variable=v, command=getCagePlot, value=4)

w = tk.Canvas(master, width=200, height=200)
w.pack()

w.create_line(0, 0, 200, 100)
w.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))

w.create_rectangle(50, 25, 150, 75, fill="blue")

tk.mainloop()
