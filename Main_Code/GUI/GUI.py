import Tkinter as tk

# make master window
master = tk.Tk()

# make entry field
e = tk.Entry(master,width=30)
e.pack()

e.insert(0, "give time interval in minutes")

# make Button
b = tk.Button(master,text="click to send minutes")
b.pack()

tk.mainloop()
