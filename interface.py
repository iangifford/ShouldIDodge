#Author: Ian Gifford
#Project: Should I Dodge?
#For those high-elo players who dodge to avoid L's, this will help give a less subjectiv answer on whether or not you should dodge.
import tkinter
from tkinter import ttk
from loader import loader
from tkinter import messagebox
from algorithms import basiccalc, advancedcalc
from scrape import update_all_champ_data


class interface:
    #The menu where you pick what teams are what champs.
    #window: window to be putting this menu in
    def selectmenu(self, window):
        #Function to click when you want to lock in your selections and do basic algorithm
        def confirmbasic():
            ready = True
            blue = [btop.get(), bjg.get(), bmid.get(), badc.get(), bsup.get()]
            red = [rtop.get(), rjg.get(), rmid.get(), radc.get(), rsup.get()]
            for item in blue:
                if item == "":
                    ready = False
            for item in red:
                if item == "":
                    ready = False
            #Prevents empty boxes
            if ready == False:
                messagebox.showinfo("Error", "Please select all 10 champions.")
            else:
                selectframe.destroy()
                self.calcscreenbasic(blue, red, window)
            #print(btop.get(), bjg.get(), bmid.get(), badc.get(), bsup.get())

        # Function to click when you want to lock in your selections and do advanced algorithm
        def confirmadvanced():
            ready = True
            blue = [btop.get(), bjg.get(), bmid.get(), badc.get(), bsup.get()]
            red = [rtop.get(), rjg.get(), rmid.get(), radc.get(), rsup.get()]
            for item in blue:
                if item == "":
                    ready = False
            for item in red:
                if item == "":
                    ready = False
            # Prevents empty boxes
            if ready == False:
                messagebox.showinfo("Error", "Please select all 10 champions.")
            else:
                selectframe.destroy()
                self.calcscreenbasic(blue, red, window)
            #print(btop.get(), bjg.get(), bmid.get(), badc.get(), bsup.get())

        #Preparing
        l = loader()
        champs = l.getChamps()
        selectframe = tkinter.Frame(window)
        selectframe.config(bg = "slateblue2")
        selectframe.pack()
        selectframe.grid_columnconfigure(0, minsize=100)
        selectframe.grid_columnconfigure(1, minsize=100)
        selectframe.grid_columnconfigure(2, minsize=100)
        selectframe.grid_rowconfigure(0, minsize=50)
        selectframe.grid_rowconfigure(1, minsize=50)
        selectframe.grid_rowconfigure(2, minsize=50)
        selectframe.grid_rowconfigure(3, minsize=50)
        selectframe.grid_rowconfigure(4, minsize=50)
        selectframe.grid_rowconfigure(5, minsize=50)
        #Column headers
        tkinter.Label(selectframe, text="Your Team", fg="black", bg = "orchid3", highlightbackground = "firebrick4", activebackground = "orchid4",bd = 1).grid(row=0, column=0)
        tkinter.Label(selectframe, text="Enemy Team", fg="black", bg = "orchid3", highlightbackground = "firebrick4", activebackground = "orchid4", bd = 1).grid(row=0, column=2)
        #preparing all the comboboxes :)
        btop = tkinter.StringVar(selectframe)
        btop.set(champs[0])
        bjg = tkinter.StringVar(selectframe)
        bjg.set(champs[0])
        bmid = tkinter.StringVar(selectframe)
        bmid.set(champs[0])
        badc = tkinter.StringVar(selectframe)
        badc.set(champs[0])
        bsup = tkinter.StringVar(selectframe)
        bsup.set(champs[0])
        rtop = tkinter.StringVar(selectframe)
        rtop.set(champs[0])
        rjg = tkinter.StringVar(selectframe)
        rjg.set(champs[0])
        rmid = tkinter.StringVar(selectframe)
        rmid.set(champs[0])
        radc = tkinter.StringVar(selectframe)
        radc.set(champs[0])
        rsup = tkinter.StringVar(selectframe)
        rsup.set(champs[0])
        #Lane labels
        tkinter.Label(selectframe, text="Top",fg="black", bg = "orchid3", highlightbackground = "firebrick4", activebackground = "orchid4",bd = 1).grid(row=1, column=1)
        tkinter.Label(selectframe, text="Jungle",fg="black", bg = "orchid3", highlightbackground = "firebrick4", activebackground = "orchid4",bd = 1).grid(row=2, column=1)
        tkinter.Label(selectframe, text="Mid",fg="black", bg = "orchid3", highlightbackground = "firebrick4", activebackground = "orchid4",bd = 1).grid(row=3, column=1)
        tkinter.Label(selectframe, text="ADC",fg="black", bg = "orchid3", highlightbackground = "firebrick4", activebackground = "orchid4",bd = 1).grid(row=4, column=1)
        tkinter.Label(selectframe, text="Support",fg="black", bg = "orchid3", highlightbackground = "firebrick4", activebackground = "orchid4",bd = 1).grid(row=5, column=1)
        #Blue/ally team labels
        bt = ttk.Combobox(selectframe, values=champs, textvariable=btop)
        bt.grid(row=1, column=0)
        bj = ttk.Combobox(selectframe, values=champs, textvariable=bjg)
        bj.grid(row=2, column=0)
        bm = ttk.Combobox(selectframe, values=champs, textvariable=bmid)
        bm.grid(row=3, column=0)
        ba = ttk.Combobox(selectframe, values=champs, textvariable=badc)
        ba.grid(row=4, column=0)
        bs = ttk.Combobox(selectframe, values=champs, textvariable=bsup)
        bs.grid(row=5, column=0)
        #Red/enemy team labels
        rt = ttk.Combobox(selectframe, values=champs, textvariable=rtop)
        rt.grid(row=1, column=2)
        rj = ttk.Combobox(selectframe, values=champs, textvariable=rjg)
        rj.grid(row=2, column=2)
        rm = ttk.Combobox(selectframe, values=champs, textvariable=rmid)
        rm.grid(row=3, column=2)
        ra = ttk.Combobox(selectframe, values=champs, textvariable=radc)
        ra.grid(row=4, column=2)
        rs = ttk.Combobox(selectframe, values=champs, textvariable=rsup)
        rs.grid(row=5, column=2)
        #Select buttons
        button = tkinter.Button(selectframe, text="Basic Calculation", command=confirmbasic, fg="black", bg ="orchid3", highlightbackground ="firebrick4", activebackground ="orchid4", bd = 1)
        button.grid(row=6, column=1)
        button = tkinter.Button(selectframe, text="Advanced Calculation", command=confirmadvanced, fg="black", bg ="orchid3", highlightbackground ="firebrick4", activebackground ="orchid4", bd = 1)
        button.grid(row=7, column=1)
        window.mainloop()
    #window: window to be putting this menu in
    #Screen to show the calculations of the program on how likely you are to win.
    def calcscreenbasic(self, blue, red, window):
        #Frame preparation
        results = advancedcalc(blue, red)
        results_nice = []
        for item in results:
            results_nice.append(str(item) + "%")

        calcframe = tkinter.Frame(window, bg = "slateblue2")
        calcframe.pack()
        #Preps the grid
        calcframe.grid_columnconfigure(0, minsize=100)
        calcframe.grid_columnconfigure(1, minsize=100)
        calcframe.grid_columnconfigure(2, minsize=100)
        calcframe.grid_columnconfigure(3, minsize=100)
        calcframe.grid_columnconfigure(4, minsize=100)
        calcframe.grid_columnconfigure(5, minsize=100)
        calcframe.grid_columnconfigure(6, minsize=100)
        calcframe.grid_rowconfigure(0, minsize=50)
        calcframe.grid_rowconfigure(1, minsize=50)
        calcframe.grid_rowconfigure(2, minsize=50)
        calcframe.grid_rowconfigure(3, minsize=50)
        calcframe.grid_rowconfigure(4, minsize=50)
        calcframe.grid_rowconfigure(5, minsize=50)
        #Lane labels
        tkinter.Label(calcframe, text="Top", fg="black", bg = "orchid3", highlightbackground = "firebrick4", activebackground = "orchid4").grid(row=0, column=0)
        tkinter.Label(calcframe, text="Jungle", fg="black", bg = "orchid3", highlightbackground = "firebrick4", activebackground = "orchid4").grid(row=1, column=0)
        tkinter.Label(calcframe, text="Mid", fg="black", bg = "orchid3", highlightbackground = "firebrick4", activebackground = "orchid4").grid(row=2, column=0)
        tkinter.Label(calcframe, text="ADC", fg="black", bg = "orchid3", highlightbackground = "firebrick4", activebackground = "orchid4").grid(row=3, column=0)
        tkinter.Label(calcframe, text="Support", fg="black", bg = "orchid3", highlightbackground = "firebrick4", activebackground = "orchid4").grid(row=4, column=0)
        #Champ labels(ally)
        tkinter.Label(calcframe, text=str(blue[0]), fg="black", bg = "orchid3", highlightbackground = "firebrick4", activebackground = "orchid4").grid(row=0, column=1)
        tkinter.Label(calcframe, text=str(blue[1]), fg="black", bg = "orchid3", highlightbackground = "firebrick4", activebackground = "orchid4").grid(row=1, column=1)
        tkinter.Label(calcframe, text=str(blue[2]), fg="black", bg = "orchid3", highlightbackground = "firebrick4", activebackground = "orchid4").grid(row=2, column=1)
        tkinter.Label(calcframe, text=str(blue[3]), fg="black", bg = "orchid3", highlightbackground = "firebrick4", activebackground = "orchid4").grid(row=3, column=1)
        tkinter.Label(calcframe, text=str(blue[4]), fg="black", bg = "orchid3", highlightbackground = "firebrick4", activebackground = "orchid4").grid(row=4, column=1)
        #Champ winrates(ally)
        tkinter.Label(calcframe, text=str(results_nice[0]), fg="black", bg = "orchid3", highlightbackground = "firebrick4", activebackground = "orchid4",bd = 1, relief = "raised").grid(row=0, column=2)
        tkinter.Label(calcframe, text=str(results_nice[1]), fg="black", bg = "orchid3", highlightbackground = "firebrick4", activebackground = "orchid4",bd = 1, relief = "raised").grid(row=1, column=2)
        tkinter.Label(calcframe, text=str(results_nice[2]), fg="black", bg = "orchid3", highlightbackground = "firebrick4", activebackground = "orchid4",bd = 1, relief = "raised").grid(row=2, column=2)
        tkinter.Label(calcframe, text=str(results_nice[3]), fg="black", bg = "orchid3", highlightbackground = "firebrick4", activebackground = "orchid4",bd = 1, relief = "raised").grid(row=3, column=2)
        tkinter.Label(calcframe, text=str(results_nice[4]), fg="black", bg = "orchid3", highlightbackground = "firebrick4", activebackground = "orchid4",bd = 1, relief = "raised").grid(row=4, column=2)
        #Game winrate
        tkinter.Label(calcframe, text=str(results_nice[5]), bg = "black", fg = "white").grid(row=2, column=3)
        #Champ winrates (enemy)
        tkinter.Label(calcframe, text=str(results_nice[6]), fg="black", bg = "orchid3", highlightbackground = "firebrick4", activebackground = "orchid4",bd = 1, relief = "raised").grid(row=0, column=4)
        tkinter.Label(calcframe, text=str(results_nice[7]), fg="black", bg = "orchid3", highlightbackground = "firebrick4", activebackground = "orchid4",bd = 1, relief = "raised").grid(row=1, column=4)
        tkinter.Label(calcframe, text=str(results_nice[8]), fg="black", bg = "orchid3", highlightbackground = "firebrick4", activebackground = "orchid4",bd = 1, relief = "raised").grid(row=2, column=4)
        tkinter.Label(calcframe, text=str(results_nice[9]), fg="black", bg = "orchid3", highlightbackground = "firebrick4", activebackground = "orchid4",bd = 1, relief = "raised").grid(row=3, column=4)
        tkinter.Label(calcframe, text=str(results_nice[10]), fg="black", bg = "orchid3", highlightbackground = "firebrick4", activebackground = "orchid4",bd = 1, relief = "raised").grid(row=4, column=4)
        #Champ labels(enemy)
        tkinter.Label(calcframe, text=str(red[0]), fg="black", bg = "orchid3", highlightbackground = "firebrick4", activebackground = "orchid4").grid(row=0, column=5)
        tkinter.Label(calcframe, text=str(red[1]), fg="black", bg = "orchid3", highlightbackground = "firebrick4", activebackground = "orchid4").grid(row=1, column=5)
        tkinter.Label(calcframe, text=str(red[2]), fg="black", bg = "orchid3", highlightbackground = "firebrick4", activebackground = "orchid4").grid(row=2, column=5)
        tkinter.Label(calcframe, text=str(red[3]), fg="black", bg = "orchid3", highlightbackground = "firebrick4", activebackground = "orchid4").grid(row=3, column=5)
        tkinter.Label(calcframe, text=str(red[4]), fg="black", bg = "orchid3", highlightbackground = "firebrick4", activebackground = "orchid4").grid(row=4, column=5)
        #Lane labels again for niceness
        tkinter.Label(calcframe, text="Top", fg="black", bg = "orchid3", highlightbackground = "firebrick4", activebackground = "orchid4").grid(row=0, column=6)
        tkinter.Label(calcframe, text="Jungle", fg="black", bg = "orchid3", highlightbackground = "firebrick4", activebackground = "orchid4").grid(row=1, column=6)
        tkinter.Label(calcframe, text="Mid", fg="black", bg = "orchid3", highlightbackground = "firebrick4", activebackground = "orchid4").grid(row=2, column=6)
        tkinter.Label(calcframe, text="ADC", fg="black", bg = "orchid3", highlightbackground = "firebrick4", activebackground = "orchid4").grid(row=3, column=6)
        tkinter.Label(calcframe, text="Support", fg="black", bg = "orchid3", highlightbackground = "firebrick4", activebackground = "orchid4").grid(row=4, column=6)
        #Little label to go right over the middle
        tkinter.Label(calcframe, text="Estimated chance to win:", bg = "black", fg = "white").grid(row=1, column=3)

        #For cleaning up and going back to main menu
        def goto_main():
            calcframe.destroy()
            self.mainmenu(window)
        #Button at the bottom saying back to main menu
        button = tkinter.Button(calcframe, text="Return to main menu", fg="black", bg = "orchid3", highlightbackground = "firebrick4", activebackground = "orchid4", command=goto_main)
        button.grid(column=3, row=6)

        window.mainloop()



    #window: window to be putting this menu in
    def mainmenu(self,window):
        #For going to the champ select menu

        def goto_select():
            mainf.destroy()
            self.selectmenu(window)

        def update_champ_data():
            if not self.__locked:
                self.__locked = True
                progress = ttk.Progressbar(mainf, orient="horizontal", length=190,)
                progress.pack()
                update_all_champ_data(progress,window)
                self.__locked = False
        #Prep Frame
        mainf = tkinter.Frame(window)
        mainf.pack(side="top")
        startbutton = tkinter.Button(mainf, text="Set up new game", fg="black", bg = "orchid3", highlightbackground = "firebrick4", activebackground = "orchid4", width = 20,command=goto_select)
        startbutton.pack()
        updatebutton = tkinter.Button(mainf, text="Update Champion Data", fg="black", bg="orchid3",highlightbackground="firebrick4", activebackground="orchid4", width = 20, command=update_champ_data)
        updatebutton.pack()

        window.mainloop()

    def __init__(self):
        self.__locked = False
        #Sets the window up and then heads to the main menu
        window = tkinter.Tk()
        window.title("Dodge")
        window.minsize(500, 500)
        window.configure(bg = "slateblue2")
        self.mainmenu(window)