import Tkinter as tk

    

master = tk.Tk()
w = tk.Frame(master)
w.pack(side="top")

v = tk.IntVar()

tk.Radiobutton(w, text="Cage One", variable=v, value=1).pack(side="left")
tk.Radiobutton(w, text="Cage Two", variable=v, value=2).pack(side="left")
tk.Radiobutton(w, text="Cage Three", variable=v, value=3).pack(side="left")
tk.Radiobutton(w, text="Cage Four", variable=v, value=4).pack(side="left")

w = tk.Canvas(master, width=200, height=200)
w.pack()

tk.mainloop()
