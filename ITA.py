import tkinter as tk
import tkstyle
from tkinter import ttk
from tkinter.messagebox import showinfo
from ttkthemes import ThemedStyle



window = tk.Tk()
#getting screen width and height of display
width= window.winfo_screenwidth()
height= window.winfo_screenheight()
#setting tkinter window size
window.geometry("%dx%d" % (width, height))
window.title("Geeeks For Geeks")

# Setting Theme
style = ThemedStyle(window)
style.set_theme("scidgrey")

# Button Widgets
Def_Btn = tk.Button(window,text='Default Button')
Def_Btn.pack()
Themed_Btn = ttk.Button(window,text='Themed button')
Themed_Btn.pack()

# Scrollbar Widgets
Def_Scrollbar = tk.Scrollbar(window)
Def_Scrollbar.pack(side='right',fill='y')
Themed_Scrollbar = ttk.Scrollbar(window,orient='horizontal')
Themed_Scrollbar.pack(side='top',fill='x')

# Entry Widgets
Def_Entry = tk.Entry(window)
Def_Entry.pack()
Themed_Entry = ttk.Entry(window)
Themed_Entry.pack()



greeting = tk.Label(text="Hello, Tkinter")
#greeting.pack()

label = tk.Label(
    text="Hello, Tkinter",
    foreground="white",  # Set the text color to white
    background="black"  # Set the background color to black
)


scrollbar = tk.Scrollbar(window)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

checklist = tk.Text(window, width=20)
checklist.pack()

vars = []
for i in range(50):
    var = tk.IntVar()
    vars.append(var)
    checkbutton = tk.Checkbutton(checklist, text=i, variable=var)
    checklist.window_create("end", window=checkbutton)
    checklist.insert("end", "\n")

checklist.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=checklist.yview)

# disable the widget so users can't insert text into it
checklist.configure(state="disabled")



window.mainloop()
