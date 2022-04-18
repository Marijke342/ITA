import tkinter as tk

from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter.font as font
import tkinter.ttk as ttk

class inputData:

    def __init__(self):

        data1 = {'Country': ['US','CA','GER','UK','FR'],
                 'GDP_Per_Capita': [45000,42000,52000,49000,47000]
                }
        self.df1 = DataFrame(data1,columns=['Country','GDP_Per_Capita'])


        data2 = {'Year': [1920,1930,1940,1950,1960,1970,1980,1990,2000,2010],
                 'Unemployment_Rate': [9.8,12,8,7.2,6.9,7,6.5,6.2,5.5,6.3]
                }
        self.df2 = DataFrame(data2,columns=['Year','Unemployment_Rate'])


        data3 = {'Interest_Rate': [5,5.5,6,5.5,5.25,6.5,7,8,7.5,8.5],
                 'Stock_Index_Price': [1500,1520,1525,1523,1515,1540,1545,1560,1555,1565]
                }
        self.df3 = DataFrame(data3,columns=['Interest_Rate','Stock_Index_Price'])





class App():

    # Here, set everything up you want to override later, when restarting the GUI
    def __init__(self):
        # This will be shown on the button (when dark mode is active it needs to say "light theme")
        self.bg, self.fg = ('#282828', 'white')
        self.mainGUI()  # Call the actual GUI and Inistialize with the standard Settings. This has to be AFTER all the setup

    def mainGUI(self):
        # Set up Root window
        self.root = tk.Tk()
        self.font = font.Font(family = 'Helvetica', size = 16)
        width= self.root.winfo_screenwidth()
        height= self.root.winfo_screenheight()
        self.root.geometry("%dx%d" % (width, height))
        self.root.title('Investment Tracker Application')
        self.root.configure(bg=self.bg)


        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.root.columnconfigure(2, weight=5)
        self.root.rowconfigure(0,weight=8)
        self.root.rowconfigure(1,weight=6)



        frame1= tk.Frame(self.root,  bg = self.bg, highlightthickness=1, highlightbackground=self.fg)
        frame1.grid(column=0, row=0, columnspan=1, sticky='ewns', padx=5, pady=5)
        frame2= tk.Frame(self.root,  bg = self.bg, highlightthickness=1, highlightbackground=self.fg)
        frame2.grid(column=1, row=0, columnspan=1, sticky='ewns', padx=5, pady=5)
        frame3= tk.Frame(self.root,  bg = self.bg, highlightthickness=1, highlightbackground=self.fg)
        frame3.grid(column=2, row=0, columnspan=8, sticky='ewns', padx=5, pady=5)
        frame4= tk.Frame(self.root,  bg = self.bg, highlightthickness=1, highlightbackground='red')
        frame4.grid(column=0, row=1, sticky='ewns', padx=5, pady=5)

        self.btn4 = tk.Button(frame4, text='test')

        self.btn1 = tk.Button(frame1, text='Load data as JSON')
        self.btn2 = tk.Button(frame1,text='Make JSON file')
        self.btn3 = tk.Button(frame1, text = "Quit")

        for btn in [self.btn1, self.btn2, self.btn3, self.btn4]:
            btn.configure(bg=self.bg,
                          fg=self.fg,
                          activebackground=self.bg,
                          borderwidth=0)
            btn.pack(padx=20, pady=20, fill = 'x')
            btn['font'] = self.font

        self.scrollbar = tk.Scrollbar(frame2)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.checklist = tk.Text(frame2, width=20)
        self.checklist.pack()

        vars = []
        for i in range(50):
            var = tk.IntVar()
            vars.append(var)
            checkbutton = tk.Checkbutton(self.checklist, text=i, variable=var)
            checkbutton.configure(bg=self.bg,
                          fg=self.fg,
                          activebackground=self.bg,
                          borderwidth=0,
                          font = self.font)
            self.checklist.window_create("end", window=checkbutton)
            self.checklist.insert("end", "\n")

        self.checklist.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.checklist.yview)

        # disable the widget so users can't insert text into it
        self.checklist.configure(state="disabled")


        # Set up the attributes that all buttons have in common and pack them (or better use grid)
        # Style them however you want
        self.checklist.configure(bg=self.bg,
                        fg = self.fg)
        self.checklist['font'] = self.font
        self.scrollbar.configure(bg=self.bg)

# Don't forget that everything needs to be between the TK() and the mainloop()

        OPTIONS = [
        "Rendement",
        "Total Wealth",
        "Asset Division",
        "Inflation",
        "Prediction",
        "To do"

        ] #etc





        framefig= tk.Frame(frame3,  bg = self.bg, highlightthickness=1, highlightbackground=self.fg)
        #frame1.grid(column=0, row=0, sticky='ewns', padx=5, pady=5)
        dd = inputData()
        figure1 = plt.Figure()
        df1 = dd.df1
        ax1 = figure1.add_subplot(111)
        bar1 = FigureCanvasTkAgg(figure1, master = frame3)
        #bar1.get_tk_widget().grid(column=0, row=0, sticky='ewns', padx=5, pady=5)
        bar1.draw()
        bar1.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, padx = 15, pady = 15, expand=1)
        print(frame3["highlightbackground"])
        df1 = df1[['Country','GDP_Per_Capita']].groupby('Country').sum()
        df1.plot(kind='bar', legend=True, ax=ax1)
        ax1.set_title('Country Vs. GDP Per Capita')
        #framefig.grid(column=0, row=0, sticky='ewns', padx=5, pady=5)

        variable = tk.StringVar()
        variable.set(OPTIONS[0]) # default value

        self.options = tk.OptionMenu(frame1, variable, *OPTIONS)
        print(variable.get())
        self.options.pack(padx=20, pady=20, fill = 'x')

        self.options.configure(bg=self.bg,
                        borderwidth=0,
                        activebackground=self.bg,
                        fg = self.fg)
        self.options["menu"].config(bg=self.bg,
                        borderwidth=0,
                        fg = self.fg,
                        font = self.font)
        self.options["font"] = self.font

        self.root.mainloop()


x = App()
