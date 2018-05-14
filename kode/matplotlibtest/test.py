import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style

import tkinter as tk
from tkinter import ttk

LARGE_FONT = ("Verdana", 12)
style.use("ggplot")

f = Figure(figsize = (5,5), dpi=100)
a = f.add_subplot(111)

def animate(i):
    pullData = open("sampleData.txt", "r").read()
    dataList = pullData.split('\n')
    xList = []
    yList = []
    for eachLine in dataList:
        if len(eachLine) > 1:
            x, y = eachLine.split(',')
            xList.append(int(x))
            yList.append(int(y))
    a.clear()
    a.plot(xList, yList)


class TestApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "Test app med graf")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartSide, SideEn, SideTo, SideTre):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column = 0, sticky="nsew")

        self.show_frame(StartSide)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()




class StartSide(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="StartSide", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button = ttk.Button(self, text="Besøk side 1", #Create button
                command=lambda: controller.show_frame(SideEn))   #functionality of button
        button.pack()

        button2 = ttk.Button(self, text="Besøk Side To", #Create button
                command=lambda: controller.show_frame(SideTo))   #functionality of button
        button2.pack()

        button3 = ttk.Button(self, text="Grafside", #Create button
                command=lambda: controller.show_frame(SideTre))   #functionality of button
        button3.pack()



class SideEn(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Side En", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Hjem", #Create button
                command=lambda: controller.show_frame(StartSide))   #functionality of button
        button1.pack()

        button2 = ttk.Button(self, text="Side To", #Create button
                command=lambda: controller.show_frame(SideTo))   #functionality of button
        button2.pack()

class SideTo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Side To!!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Hjem", #Create button
                command=lambda: controller.show_frame(StartSide))   #functionality of button
        button1.pack()

        button2 = ttk.Button(self, text="Side En", #Create button
                command=lambda: controller.show_frame(SideEn))   #functionality of button
        button2.pack()


class SideTre(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Grafside!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Hjem", #Create button
                command=lambda: controller.show_frame(StartSide))   #functionality of button
        button1.pack()


        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand = True)
        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand = True)


app = TestApp()
ani = animation.FuncAnimation(f, animate, interval=1000)
app.mainloop()
