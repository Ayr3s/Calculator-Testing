#############
"""Imports"""
#############

__author__ = 'Feuer'
from tkinter import *
from turtle import *
import math

###################
"""Exit Function"""
###################


def stop():
    exit()

########################
"""Main Window + Menu"""
########################

root = Tk()
root.title("Taschenrechner")
root.geometry("340x300")
root.iconbitmap(default='icon.ico')

Menu1 = Menu(root)
root.config(menu=Menu1)

subMenu1 = Menu(Menu1)
subMenu2 = Menu(subMenu1)
subMenu3 = Menu(Menu1)

Menu1.add_cascade(label="Settings", menu=subMenu1)
Menu1.add_cascade(label="About", menu=subMenu3)

subMenu1.add_cascade(label="Theme", menu=subMenu2)
subMenu1.add_separator()
subMenu1.add_command(label="Exit", command=stop)

subMenu2.add_command(label="1.Theme")
subMenu2.add_command(label="2.Theme")

subMenu3.add_command(label="Information")


################
"""Mainwindow"""
################


class Start:
    def __init__(self, master):
        frame = Frame(master, bg="gray12")
        frame.pack(fill=X)

        self.Label_1 = Label(frame, text="Bitte wählen Sie die Rechenart aus, die Sie benutzen möchten!", bg="gray12",
                             fg="cyan3")
        self.Label_2 = Label(frame, text="Addition", bg="gray12", fg="cyan3")
        self.Label_3 = Label(frame, text="Subtraktion", bg="gray12", fg="cyan3")
        self.Label_4 = Label(frame, text="Multiplikation", bg="gray12", fg="cyan3")
        self.Label_5 = Label(frame, text="Division", bg="gray12", fg="cyan3")
        self.Label_6 = Label(frame, text="Wurzel", bg="gray12", fg="cyan3")
        self.Label_7 = Label(frame, text="Logarithmus", bg="gray12", fg="cyan3")
        self.Label_8 = Label(frame, text="Potenz", bg="gray12", fg="cyan3")
        self.Label_9 = Label(frame, text="Zinsberechnung", bg="gray12", fg="cyan3")
        self.Label_10 = Label(frame, text="Weihnachtsspecial", bg="gray12", fg="cyan3")
        self.Label_11 = Label(frame, text="©2015 - Lars Roth", bg="gray12", fg="cyan3", bd=1)
        self.Button_1 = Button(frame, text="Go!", command=add, width=11, bg="gray12", fg="cyan3", relief=RIDGE)
        self.Button_2 = Button(frame, text="Go!", command=sub, width=11, bg="gray12", fg="cyan3", relief=RIDGE)
        self.Button_3 = Button(frame, text="Go!", command=mul, width=11, bg="gray12", fg="cyan3", relief=RIDGE)
        self.Button_4 = Button(frame, text="Go!", command=div, width=11, bg="gray12", fg="cyan3", relief=RIDGE)
        self.Button_5 = Button(frame, text="Go!", command=wur, width=11, bg="gray12", fg="cyan3", relief=RIDGE)
        self.Button_6 = Button(frame, text="Go!", command=log, width=11, bg="gray12", fg="cyan3", relief=RIDGE)
        self.Button_7 = Button(frame, text="Go!", command=pot, width=11, bg="gray12", fg="cyan3", relief=RIDGE)
        self.Button_8 = Button(frame, text="Go!", command=zin, width=11, bg="gray12", fg="cyan3", relief=RIDGE)
        self.Button_9 = Button(frame, text="Go!", command=troll, width=11, bg="gray12", fg="cyan3", relief=RIDGE)
        self.Button_10 = Button(frame, text="Das Programm beenden!", command=stop, width=36, bg="gray12", fg="cyan3",
                                relief=RIDGE)

        self.Label_1.grid(row=0, columnspan=2)
        self.Label_2.grid(row=1, column=0)
        self.Label_3.grid(row=2, column=0)
        self.Label_4.grid(row=3, column=0)
        self.Label_5.grid(row=4, column=0)
        self.Label_6.grid(row=5, column=0)
        self.Label_7.grid(row=6, column=0)
        self.Label_8.grid(row=7, column=0)
        self.Label_9.grid(row=8, column=0)
        self.Label_10.grid(row=9, column=0)
        self.Label_11.grid(row=11, columnspan=2)
        self.Button_1.grid(row=1, column=1)
        self.Button_2.grid(row=2, column=1)
        self.Button_3.grid(row=3, column=1)
        self.Button_4.grid(row=4, column=1)
        self.Button_5.grid(row=5, column=1)
        self.Button_6.grid(row=6, column=1)
        self.Button_7.grid(row=7, column=1)
        self.Button_8.grid(row=8, column=1)
        self.Button_9.grid(row=9, column=1)
        self.Button_10.grid(row=10, columnspan=2)


###################
"""Additionsmode"""
###################


class add:
    def __init__(self):
        newwin = Toplevel()
        newwin.title("Addition")
        newwin.geometry("500x80")
        frame2 = Frame(newwin, bg="gray12")
        frame2.pack(fill=BOTH, expand=5)

        global var1

        var1 = StringVar()
        var1.set("Ready")

        self.Label_1 = Label(frame2, text="Additionsverfahren", bg="gray12", fg="cyan3")
        self.Entry_1 = Entry(frame2, bg="gray12", fg="cyan3", relief=RIDGE)
        self.Label_2 = Label(frame2, text="+", bg="gray12", fg="cyan3")
        self.Entry_2 = Entry(frame2, bg="gray12", fg="cyan3", relief=RIDGE)
        self.Label_3 = Label(frame2, text="=", bg="gray12", fg="cyan3")
        self.Button_1 = Button(frame2, text="Zurück", command=newwin.destroy, width=20, bg="gray12", fg="cyan3",
                               relief=RIDGE)
        self.Button_2 = Button(frame2, text="Ergebniss berechnen", command=self.calc, width=20, bg="gray12", fg="cyan3",
                               relief=RIDGE)
        self.Button_3 = Button(frame2, text="Reset", command=self.reset, width=20, bg="gray12", fg="cyan3",
                               relief=RIDGE)
        self.Label_Erg1 = Label(frame2, textvariable=var1, fg="red", underline=0, relief="ridge", bg="yellow3",
                                width=17)

        self.Label_1.grid(row=0, columnspan=4, pady=2, padx=2)
        self.Entry_1.grid(row=1, column=0, pady=2, padx=2)
        self.Label_2.grid(row=1, column=1, pady=2, padx=2)
        self.Entry_2.grid(row=1, column=2, pady=2, padx=2)
        self.Label_3.grid(row=1, column=3, pady=2, padx=2)
        self.Button_2.grid(row=2, column=2, pady=2, padx=2)
        self.Button_1.grid(row=2, column=4, pady=2, padx=2)
        self.Button_3.grid(row=2, column=0, pady=2, padx=2)
        self.Label_Erg1.grid(row=1, column=4, pady=2, padx=2)

    def calc(self, *args):
        global var1
        z1 = self.Entry_1.get()
        z2 = self.Entry_2.get()
        za1 = float(z1)
        za2 = float(z2)
        erg11 = za1 + za2
        var1.set(erg11)

    def reset(self, *args):
        global var1
        var1.set("Ready")
        self.Entry_1.delete(0, END)
        self.Entry_2.delete(0, END)


######################
"""Subtraktionsmode"""
######################


class sub:
    def __init__(self):
        newwin = Toplevel()
        newwin.title("Subtraktion")
        newwin.geometry("500x80")
        frame2 = Frame(newwin, bg="gray12")
        frame2.pack(fill=BOTH, expand=5)

        global var2

        var2 = StringVar()
        var2.set("Ready")

        self.Label_1 = Label(frame2, text="Subtraktionsverfahren", bg="gray12", fg="cyan3")
        self.Entry_3 = Entry(frame2, bg="gray12", fg="cyan3", relief=RIDGE)
        self.Label_2 = Label(frame2, text="-", bg="gray12", fg="cyan3")
        self.Entry_4 = Entry(frame2, bg="gray12", fg="cyan3", relief=RIDGE)
        self.Label_3 = Label(frame2, text="=", bg="gray12", fg="cyan3")
        self.Button_1 = Button(frame2, text="Zurück", command=newwin.destroy, width=20, bg="gray12", fg="cyan3",
                               relief=RIDGE)
        self.Button_2 = Button(frame2, text="Ergebniss berechnen", command=self.calc, width=20, bg="gray12", fg="cyan3",
                               relief=RIDGE)
        self.Button_3 = Button(frame2, text="Reset", command=self.reset, width=20, bg="gray12", fg="cyan3",
                               relief=RIDGE)
        self.Label_Erg2 = Label(frame2, textvariable=var2, fg="red", underline=0, relief="ridge", bg="yellow3",
                                width=17)

        self.Label_1.grid(row=0, columnspan=4, pady=2, padx=2)
        self.Entry_3.grid(row=1, column=0, pady=2, padx=2)
        self.Label_2.grid(row=1, column=1, pady=2, padx=2)
        self.Entry_4.grid(row=1, column=2, pady=2, padx=2)
        self.Label_3.grid(row=1, column=3, pady=2, padx=2)
        self.Button_2.grid(row=2, column=2, pady=2, padx=2)
        self.Button_1.grid(row=2, column=4, pady=2, padx=2)
        self.Button_3.grid(row=2, column=0, pady=2, padx=2)
        self.Label_Erg2.grid(row=1, column=4, pady=2, padx=2)

    def calc(self, *args):
        global var2
        z3 = self.Entry_3.get()
        z4 = self.Entry_4.get()
        za3 = float(z3)
        za4 = float(z4)
        erg11 = za3 - za4
        var2.set(erg11)

    def reset(self, *args):
        global var2
        var2.set("Ready")
        self.Entry_3.delete(0, END)
        self.Entry_4.delete(0, END)


#########################
"""Multiplikationsmode"""
#########################


class mul:
    def __init__(self):
        newwin = Toplevel()
        newwin.title("Multiplikation")
        newwin.geometry("500x80")
        frame2 = Frame(newwin, bg="gray12")
        frame2.pack(fill=BOTH, expand=5)

        global var3

        var3 = StringVar()
        var3.set("Ready")

        self.Label_1 = Label(frame2, text="Multiplikationssverfahren", bg="gray12", fg="cyan3")
        self.Entry_5 = Entry(frame2, bg="gray12", fg="cyan3", relief=RIDGE)
        self.Label_2 = Label(frame2, text="*", bg="gray12", fg="cyan3")
        self.Entry_6 = Entry(frame2, bg="gray12", fg="cyan3", relief=RIDGE)
        self.Label_3 = Label(frame2, text="=", bg="gray12", fg="cyan3")
        self.Button_1 = Button(frame2, text="Zurück", command=newwin.destroy, width=20, bg="gray12", fg="cyan3",
                               relief=RIDGE)
        self.Button_2 = Button(frame2, text="Ergebniss berechnen", command=self.calc, width=20, bg="gray12", fg="cyan3",
                               relief=RIDGE)
        self.Button_3 = Button(frame2, text="Reset", command=self.reset, width=20, bg="gray12", fg="cyan3",
                               relief=RIDGE)
        self.Label_Erg3 = Label(frame2, textvariable=var3, fg="red", underline=0, relief="ridge", bg="yellow3",
                                width=17)

        self.Label_1.grid(row=0, columnspan=4, pady=2, padx=2)
        self.Entry_5.grid(row=1, column=0, pady=2, padx=2)
        self.Label_2.grid(row=1, column=1, pady=2, padx=2)
        self.Entry_6.grid(row=1, column=2, pady=2, padx=2)
        self.Label_3.grid(row=1, column=3, pady=2, padx=2)
        self.Button_2.grid(row=2, column=2, pady=2, padx=2)
        self.Button_1.grid(row=2, column=4, pady=2, padx=2)
        self.Button_3.grid(row=2, column=0, pady=2, padx=2)
        self.Label_Erg3.grid(row=1, column=4, pady=2, padx=2)

    def calc(self, *args):
        global var3
        z5 = self.Entry_5.get()
        z6 = self.Entry_6.get()
        za5 = float(z5)
        za6 = float(z6)

        erg11 = za5 * za6
        var3.set(erg11)

    def reset(self, *args):
        global var3
        var3.set("Ready")
        self.Entry_5.delete(0, END)
        self.Entry_6.delete(0, END)


###################
"""Divisiosnmode"""
###################


class div:
    def __init__(self):
        newwin = Toplevel()
        newwin.title("Division")
        newwin.geometry("500x80")
        frame2 = Frame(newwin, bg="gray12")
        frame2.pack(fill=BOTH, expand=5)

        global var4

        var4 = StringVar()
        var4.set("Ready")

        self.Label_1 = Label(frame2, text="Divisionsverfahren", bg="gray12", fg="cyan3")
        self.Entry_7 = Entry(frame2, bg="gray12", fg="cyan3", relief=RIDGE)
        self.Label_2 = Label(frame2, text="/", bg="gray12", fg="cyan3")
        self.Entry_8 = Entry(frame2, bg="gray12", fg="cyan3", relief=RIDGE)
        self.Label_3 = Label(frame2, text="=", bg="gray12", fg="cyan3")
        self.Button_1 = Button(frame2, text="Zurück", command=newwin.destroy, width=20, bg="gray12", fg="cyan3",
                               relief=RIDGE)
        self.Button_2 = Button(frame2, text="Ergebniss berechnen", command=self.calc, width=20, bg="gray12", fg="cyan3",
                               relief=RIDGE)
        self.Button_3 = Button(frame2, text="Reset", command=self.reset, width=20, bg="gray12", fg="cyan3",
                               relief=RIDGE)
        self.Label_Erg4 = Label(frame2, textvariable=var4, fg="red", underline=0, relief="ridge", bg="yellow3",
                                width=17)

        self.Label_1.grid(row=0, columnspan=4, pady=2, padx=2)
        self.Entry_7.grid(row=1, column=0, pady=2, padx=2)
        self.Label_2.grid(row=1, column=1, pady=2, padx=2)
        self.Entry_8.grid(row=1, column=2, pady=2, padx=2)
        self.Label_3.grid(row=1, column=3, pady=2, padx=2)
        self.Button_2.grid(row=2, column=2, pady=2, padx=2)
        self.Button_1.grid(row=2, column=4, pady=2, padx=2)
        self.Button_3.grid(row=2, column=0, pady=2, padx=2)
        self.Label_Erg4.grid(row=1, column=4, pady=2, padx=2)

    def calc(self, *args):
        global var4
        z7 = self.Entry_7.get()
        z8 = self.Entry_8.get()
        za7 = float(z7)
        za8 = float(z8)
        erg11 = za7 / za8
        var4.set(erg11)

    def reset(self, *args):
        global var4
        var4.set("Ready")
        self.Entry_7.delete(0, END)
        self.Entry_8.delete(0, END)


################
"""Wurzelmode"""
################


class wur:
    def __init__(self):
        newwin = Toplevel()
        newwin.title("Wurzel")
        newwin.geometry("510x80")
        frame2 = Frame(newwin, bg="gray12")
        frame2.pack(fill=BOTH, expand=5)

        global var5

        var5 = StringVar()
        var5.set("Ready")

        self.Label_1 = Label(frame2, text="Wurzelziehen", bg="gray12", fg="cyan3")
        self.Label_4 = Label(frame2, text="Die", bg="gray12", fg="cyan3")
        self.Entry_9 = Entry(frame2, bg="gray12", fg="cyan3", relief=RIDGE)
        self.Label_2 = Label(frame2, text="Wurzel von", bg="gray12", fg="cyan3")
        self.Entry_10 = Entry(frame2, bg="gray12", fg="cyan3", relief=RIDGE)
        self.Label_3 = Label(frame2, text="=", bg="gray12", fg="cyan3")
        self.Button_1 = Button(frame2, text="Zurück", command=newwin.destroy, width=20, bg="gray12", fg="cyan3",
                               relief=RIDGE)
        self.Button_2 = Button(frame2, text="Ergebniss berechnen", command=self.calc, width=20, bg="gray12", fg="cyan3",
                               relief=RIDGE)
        self.Button_3 = Button(frame2, text="Reset", command=self.reset, width=20, bg="gray12", fg="cyan3",
                               relief=RIDGE)
        self.Label_Erg5 = Label(frame2, textvariable=var5, fg="red", underline=0, relief="ridge", bg="yellow3",
                                width=17)

        self.Label_1.grid(row=0, columnspan=4, pady=2, padx=2)
        self.Label_4.grid(row=1, column=0, pady=2, padx=2)
        self.Entry_9.grid(row=1, column=1, pady=2, padx=2)
        self.Label_2.grid(row=1, column=2, pady=2, padx=2)
        self.Entry_10.grid(row=1, column=3, pady=2, padx=2)
        self.Label_3.grid(row=1, column=4, pady=2, padx=2)
        self.Button_2.grid(row=2, column=2, columnspan=2, pady=2, padx=2)
        self.Button_1.grid(row=2, column=4, columnspan=2, pady=2, padx=2)
        self.Button_3.grid(row=2, column=0, columnspan=2, pady=2, padx=2)
        self.Label_Erg5.grid(row=1, column=5, pady=2, padx=2)

    def calc(self, *args):
        global var5
        z9 = self.Entry_9.get()
        z10 = self.Entry_10.get()
        za9 = float(z9)
        za10 = float(z10)
        erg11 = za10 ** (1 / za9)
        var5.set(erg11)

    def reset(self, *args):
        global var5
        var5.set("Ready")
        self.Entry_9.delete(0, END)
        self.Entry_10.delete(0, END)


#####################
"""Logarithmusmode"""
#####################


class log:
    def __init__(self):
        newwin = Toplevel()
        newwin.title("Wurzel")
        newwin.geometry("550x80")
        frame2 = Frame(newwin, bg="gray12")
        frame2.pack(fill=BOTH, expand=5)

        global var6

        var6 = StringVar()
        var6.set("Ready")

        self.Label_1 = Label(frame2, text="Logarithmus", bg="gray12", fg="cyan3")
        self.Label_4 = Label(frame2, text="Der Log. von", bg="gray12", fg="cyan3")
        self.Entry_11 = Entry(frame2, bg="gray12", fg="cyan3", relief=RIDGE)
        self.Label_2 = Label(frame2, text="mit Basis", bg="gray12", fg="cyan3")
        self.Entry_12 = Entry(frame2, bg="gray12", fg="cyan3", relief=RIDGE)
        self.Label_3 = Label(frame2, text="=", bg="gray12", fg="cyan3")
        self.Button_1 = Button(frame2, text="Zurück", command=newwin.destroy, width=20, bg="gray12", fg="cyan3",
                               relief=RIDGE)
        self.Button_2 = Button(frame2, text="Ergebniss berechnen", command=self.calc, width=20, bg="gray12", fg="cyan3",
                               relief=RIDGE)
        self.Button_3 = Button(frame2, text="Reset", command=self.reset, width=20, bg="gray12", fg="cyan3",
                               relief=RIDGE)
        self.Label_Erg6 = Label(frame2, textvariable=var6, fg="red", underline=0, relief="ridge", bg="yellow3",
                                width=17)

        self.Label_1.grid(row=0, columnspan=4, pady=2, padx=2)
        self.Label_4.grid(row=1, column=0, pady=2, padx=2)
        self.Entry_11.grid(row=1, column=1, pady=2, padx=2)
        self.Label_2.grid(row=1, column=2, pady=2, padx=2)
        self.Entry_12.grid(row=1, column=3, pady=2, padx=2)
        self.Label_3.grid(row=1, column=4, pady=2, padx=2)
        self.Button_2.grid(row=2, column=2, columnspan=2, pady=2, padx=2)
        self.Button_1.grid(row=2, column=4, columnspan=2, pady=2, padx=2)
        self.Button_3.grid(row=2, column=0, columnspan=2, pady=2, padx=2)
        self.Label_Erg6.grid(row=1, column=5, pady=2, padx=2)

    def calc(self, *args):
        global var6
        z11 = self.Entry_11.get()
        z12 = self.Entry_12.get()
        za11 = float(z11)
        za12 = float(z12)
        erg11 = math.log(za11, za12)
        var6.set(erg11)

    def reset(self, *args):
        global var6
        var6.set("Ready")
        self.Entry_11.delete(0, END)
        self.Entry_12.delete(0, END)


################
"""Potenzmode"""
################


class pot:
    def __init__(self):
        newwin = Toplevel()
        newwin.title("Potenz")
        newwin.geometry("520x80")
        frame2 = Frame(newwin, bg="gray12")
        frame2.pack(fill=BOTH, expand=5)

        global var7

        var7 = StringVar()
        var7.set("Ready")

        self.Label_1 = Label(frame2, text="Potenzierung", bg="gray12", fg="cyan3")
        self.Entry_13 = Entry(frame2, bg="gray12", fg="cyan3", relief=RIDGE)
        self.Label_2 = Label(frame2, text="hoch", bg="gray12", fg="cyan3")
        self.Entry_14 = Entry(frame2, bg="gray12", fg="cyan3", relief=RIDGE)
        self.Label_3 = Label(frame2, text="=", bg="gray12", fg="cyan3")
        self.Button_1 = Button(frame2, text="Zurück", command=newwin.destroy, width=20, bg="gray12", fg="cyan3",
                               relief=RIDGE)
        self.Button_2 = Button(frame2, text="Ergebniss berechnen", command=self.calc, width=20, bg="gray12", fg="cyan3",
                               relief=RIDGE)
        self.Button_3 = Button(frame2, text="Reset", command=self.reset, width=20, bg="gray12", fg="cyan3",
                               relief=RIDGE)
        self.Label_Erg7 = Label(frame2, textvariable=var7, fg="red", underline=0, relief="ridge", bg="yellow3",
                                width=17)

        self.Label_1.grid(row=0, columnspan=4, pady=2, padx=2)
        self.Entry_13.grid(row=1, column=0, pady=2, padx=2)
        self.Label_2.grid(row=1, column=1, pady=2, padx=2)
        self.Entry_14.grid(row=1, column=2, pady=2, padx=2)
        self.Label_3.grid(row=1, column=3, pady=2, padx=2)
        self.Button_2.grid(row=2, column=2, pady=2, padx=2)
        self.Button_1.grid(row=2, column=4, pady=2, padx=2)
        self.Button_3.grid(row=2, column=0, pady=2, padx=2)
        self.Label_Erg7.grid(row=1, column=4, pady=2, padx=2)

    def calc(self, *args):
        global var7
        z13 = self.Entry_13.get()
        z14 = self.Entry_14.get()
        za13 = float(z13)
        za14 = float(z14)
        erg11 = za13 ** za14
        var7.set(erg11)

    def reset(self, *args):
        global var7
        var7.set("Ready")
        self.Entry_13.delete(0, END)
        self.Entry_14.delete(0, END)


##############
"""Zinsmode"""
##############


class zin:
    def __init__(self):
        newwin = Toplevel()
        newwin.title("Zinsberechnung")
        newwin.geometry("299x190")
        frame2 = Frame(newwin, bg="gray12")
        frame2.pack(fill=BOTH, expand=5)

        global var_zin

        var_zin = StringVar()
        var_zin.set("Ready")

        self.Label_1 = Label(frame2, text="Zinsberechnung", bg="gray12", fg="cyan3")
        self.Label_2 = Label(frame2, text="Kapital:", bg="gray12", fg="cyan3")
        self.Label_3 = Label(frame2, text="Zinssatz:", bg="gray12", fg="cyan3")
        self.Label_4 = Label(frame2, text="Anlagejahre:", bg="gray12", fg="cyan3")
        self.Label_5 = Label(frame2, text="Endkapital:", bg="gray12", fg="cyan3")
        self.Entry_zin1 = Entry(frame2, bg="gray12", fg="cyan3", relief=RIDGE)
        self.Entry_zin2 = Entry(frame2, bg="gray12", fg="cyan3", relief=RIDGE)
        self.Entry_zin3 = Entry(frame2, bg="gray12", fg="cyan3", relief=RIDGE)
        self.Button_1 = Button(frame2, text="Zurück", command=newwin.destroy, width=40, bg="gray12", fg="cyan3",
                               relief=RIDGE)
        self.Button_2 = Button(frame2, text="Ergebniss berechnen", command=self.calc, width=19, bg="gray12", fg="cyan3",
                               relief=RIDGE)
        self.Button_3 = Button(frame2, text="Reset", command=self.reset, width=19, bg="gray12", fg="cyan3",
                               relief=RIDGE)
        self.Label_Erg_zin = Label(frame2, textvariable=var_zin, fg="red", underline=0, relief="ridge", bg="yellow3",
                                   width=17)

        self.Label_1.grid(row=0, columnspan=4, pady=2, padx=2)
        self.Label_2.grid(row=1, column=0, pady=2, padx=2)
        self.Label_3.grid(row=2, column=0, pady=2, padx=2)
        self.Label_4.grid(row=3, column=0, pady=2, padx=2)
        self.Label_5.grid(row=5, column=0, pady=2, padx=2)
        self.Entry_zin1.grid(row=1, column=1, pady=2, padx=2)
        self.Entry_zin2.grid(row=2, column=1, pady=2, padx=2)
        self.Entry_zin3.grid(row=3, column=1, pady=2, padx=2)
        self.Button_2.grid(row=6, column=1, pady=2, padx=2)
        self.Button_1.grid(row=7, columnspan=2, pady=2, padx=2)
        self.Button_3.grid(row=6, column=0, pady=2, padx=2)
        self.Label_Erg_zin.grid(row=5, column=1, pady=2, padx=2)

    def calc(self, *args):
        global var_zin
        zin1 = self.Entry_zin1.get()
        zin2 = self.Entry_zin2.get()
        zin3 = self.Entry_zin3.get()
        zina1 = float(zin1)
        zina2 = float(zin2)
        zina3 = float(zin3)
        zina4 = zina2 / 100
        erg11 = zina1 * ((1 + zina4) ** zina3)
        var_zin.set(erg11)

    def reset(self, *args):
        global var_zin
        var_zin.set("Ready")
        self.Entry_zin1.delete(0, END)
        self.Entry_zin2.delete(0, END)
        self.Entry_zin3.delete(0, END)


#######################
"""Weihnachtsspecial"""
#######################


class troll:
    def __init__(self):
        newvin = Toplevel()
        newvin.title("Special")
        frame = Frame(newvin, bg="gray12")
        frame.pack(fill=BOTH, expand=5)

        self.Button_1 = Button(frame, text="Stern", command=self.go, width=40, height=20, bg="gray12", fg="cyan3",
                               relief=RIDGE)
        self.Button_2 = Button(frame, text="Weihnachtsbaum", command=self.go2, width=40, height=20, bg="gray12",
                               fg="cyan3", relief=RIDGE)
        self.Button_3 = Button(frame, text="Baum1", command=self.go3, width=40, height=20, bg="gray12", fg="cyan3",
                               relief=RIDGE)
        self.Button_4 = Button(frame, text="Baum2", command=self.go4, width=40, height=20, bg="gray12", fg="cyan3",
                               relief=RIDGE)
        self.Button_5 = Button(frame, text="Sphere", command=self.go5, width=40, height=20, bg="gray12", fg="cyan3",
                               relief=RIDGE)
        self.Button_6 = Button(frame, text="Muster", command=self.go6, width=40, height=20, bg="gray12", fg="cyan3",
                               relief=RIDGE)

        self.Button_1.grid(row=0, column=1, pady=2, padx=2)
        self.Button_2.grid(row=0, column=0, pady=2, padx=2)
        self.Button_3.grid(row=1, column=0, pady=2, padx=2)
        self.Button_4.grid(row=1, column=1, pady=2, padx=2)
        self.Button_5.grid(row=0, column=2, pady=2, padx=2)
        self.Button_6.grid(row=1, column=2, pady=2, padx=2)

    def go(self):
        for n in range(1):
            newar = Toplevel()
            newar.title("Stern")
            """newar.geometry("1280x720")"""

            framez = Frame(newar)
            framez.pack()

            canvas_width = 200
            canvas_height = 200
            python_green = "#476042"

            w = Canvas(framez, width=canvas_width, height=canvas_height)
            w.pack()

            points = [100, 140, 110, 110, 140, 100, 110, 90, 100, 60, 90, 90, 60, 100, 90, 110]

            w.create_polygon(points, outline=python_green, fill='yellow', width=3)

    def go2(self):
        screen = Screen()
        screen.setup(800, 600)

        circle = Turtle()
        circle.shape('circle')
        circle.color('red')
        circle.speed('fastest')
        circle.up()

        square = Turtle()
        square.shape('square')
        square.color('green')
        square.speed('fastest')
        square.up()

        circle.goto(0, 280)
        circle.stamp()

        k = 0
        for i in range(1, 17):
            y = 30 * i
            for j in range(i - k):
                x = 30 * j
                square.goto(x, -y + 280)
                square.stamp()
                square.goto(-x, -y + 280)
                square.stamp()

            if i % 4 == 0:
                x = 30 * (j + 1)
                circle.color('red')
                circle.goto(-x, -y + 280)
                circle.stamp()
                circle.goto(x, -y + 280)
                circle.stamp()
                k += 2

            if i % 4 == 3:
                x = 30 * (j + 1)
                circle.color('yellow')
                circle.goto(-x, -y + 280)
                circle.stamp()
                circle.goto(x, -y + 280)
                circle.stamp()

        square.color('brown')
        for i in range(17, 20):
            y = 30 * i
            for j in range(3):
                x = 30 * j
                square.goto(x, -y + 280)
                square.stamp()
                square.goto(-x, -y + 280)
                square.stamp()

    def go3(self):
        from turtle import Turtle, Screen
        from time import clock

        screen = Screen()

        def tree(plist, l, a, f):
            for p in plist:
                yield p.forward(l)
            if l > 5:
                lst = []
                for p in plist:
                    q = p.clone()
                    p.left(a)
                    q.right(a)
                    lst.append(p)
                    lst.append(q)
                for x in tree(lst, l * f, a, f):
                    yield None

        def maketree():
            p = Turtle(shape="triangle", visible=False)
            p.setundobuffer(None)
            p.fillcolor("green")
            p.shapesize(0.4)
            p.speed(0)
            p.left(90)
            p.penup()
            p.backward(210)
            p.pendown()
            for x in tree([p], 200, 65, 0.6375):
                pass

        def main():
            screen.tracer(30, 0)
            a = clock()
            maketree()
            b = clock()
            screen.tracer(True)
            for t in screen.turtles():
                t.showturtle()
            print(len(screen.turtles()))
            return "done: {0:.2f} sec.".format(b - a)

        if __name__ == "__main__":
            msg = main()
            print(msg)
            screen.mainloop()

    def go4(self):
        from turtle import Screen, Turtle

        screen = Screen()

        def itree(t, l, f, colors):
            t.color(colors[0])
            t.forward(l)
            turtles = [t]
            colors.pop(0)
            while colors:
                l *= f
                newturtles = []
                for t in turtles:
                    t.color(colors[0])
                    t1 = t.clone()
                    t.left(45)
                    t.forward(l)
                    t1.right(45)
                    t1.forward(l)
                    newturtles.extend([t, t1])
                turtles = newturtles
                colors.pop(0)
            for t in turtles:
                t.color("green")

        def main():
            screen.mode("logo")
            t = Turtle(shape="triangle")
            t.penup();
            t.back(280);
            t.pendown()
            t.pensize(3)
            itree(t, 250, 0.63,
                  ["gray12", "brown", "red", "orange", "violet", "lightblue"])

        if __name__ == '__main__':
            main()
            screen.mainloop()

    def go5(self):
        from turtle import Screen, Turtle
        from time import clock, sleep

        def mn_eck(p, ne, sz):
            turtlelist = [p]
            # create ne-1 additional turtles
            for i in range(1, ne):
                q = p.clone()
                q.rt(360.0 / ne)
                turtlelist.append(q)
                p = q
            for i in range(ne):
                c = abs(ne / 2.0 - i) / (ne * .7)
                # let those ne turtles make a step
                # in parallel:
                for t in turtlelist:
                    t.rt(360. / ne)
                    t.pencolor(1 - c, 0, c)
                    t.fd(sz)

        def main():
            s = Screen()
            s.bgcolor("gray12")
            p = Turtle()
            p.speed(0)
            p.hideturtle()
            p.pencolor("red")
            p.pensize(3)

            s.tracer(36, 0)

            at = clock()
            mn_eck(p, 36, 19)
            et = clock()
            z1 = et - at

            sleep(1)

            at = clock()
            while any([t.undobufferentries() for t in s.turtles()]):
                for t in s.turtles():
                    t.undo()
            et = clock()
            return "Laufzeit: {0:.3f} sec".format(z1 + et - at)


        if __name__ == '__main__':
            msg = main()
            print(msg)
            mainloop()

    def go6(self):
        from turtle import Turtle, Screen
        from time import clock

        class Designer(Turtle):

            def design(self, homePos, scale):
                self.up()
                for i in range(5):
                    self.forward(64.65 * scale)
                    self.down()
                    self.wheel(self.position(), scale)
                    self.up()
                    self.backward(64.65 * scale)
                    self.right(72)
                self.up()
                self.goto(homePos)
                self.right(36)
                self.forward(24.5 * scale)
                self.right(198)
                self.down()
                self.centerpiece(46 * scale, 143.4, scale)

            def wheel(self, initpos, scale):
                self.right(54)
                for i in range(4):
                    self.pentpiece(initpos, scale)
                self.down()
                self.left(36)
                for i in range(5):
                    self.tripiece(initpos, scale)
                self.left(36)
                for i in range(5):
                    self.down()
                    self.right(72)
                    self.forward(28 * scale)
                    self.up()
                    self.backward(28 * scale)
                self.left(54)

            def tripiece(self, initpos, scale):
                oldh = self.heading()
                self.down()
                self.backward(2.5 * scale)
                self.tripolyr(31.5 * scale, scale)
                self.up()
                self.goto(initpos)
                self.setheading(oldh)
                self.down()
                self.backward(2.5 * scale)
                self.tripolyl(31.5 * scale, scale)
                self.up()
                self.goto(initpos)
                self.setheading(oldh)
                self.left(72)

            def pentpiece(self, initpos, scale):
                oldh = self.heading()
                self.up()
                self.forward(29 * scale)
                self.down()
                for i in range(5):
                    self.forward(18 * scale)
                    self.right(72)
                self.pentr(18 * scale, 75, scale)
                self.up()
                self.goto(initpos)
                self.setheading(oldh)
                self.forward(29 * scale)
                self.down()
                for i in range(5):
                    self.forward(18 * scale)
                    self.right(72)
                self.pentl(18 * scale, 75, scale)
                self.up()
                self.goto(initpos)
                self.setheading(oldh)
                self.left(72)

            def pentl(self, side, ang, scale):
                if side < (2 * scale): return
                self.forward(side)
                self.left(ang)
                self.pentl(side - (.38 * scale), ang, scale)

            def pentr(self, side, ang, scale):
                if side < (2 * scale): return
                self.forward(side)
                self.right(ang)
                self.pentr(side - (.38 * scale), ang, scale)

            def tripolyr(self, side, scale):
                if side < (4 * scale): return
                self.forward(side)
                self.right(111)
                self.forward(side / 1.78)
                self.right(111)
                self.forward(side / 1.3)
                self.right(146)
                self.tripolyr(side * .75, scale)

            def tripolyl(self, side, scale):
                if side < (4 * scale): return
                self.forward(side)
                self.left(111)
                self.forward(side / 1.78)
                self.left(111)
                self.forward(side / 1.3)
                self.left(146)
                self.tripolyl(side * .75, scale)

            def centerpiece(self, s, a, scale):
                self.forward(s);
                self.left(a)
                if s < (7.5 * scale):
                    return
                self.centerpiece(s - (1.2 * scale), a, scale)

        def main():
            t = Designer()
            t.speed(0)
            Screen().tracer(1, 0)
            t.hideturtle()
            at = clock()
            t.design(t.position(), 2)
            et = clock()
            return "runtime: %.2f sec." % (et - at)

        if __name__ == '__main__':
            msg = main()
            print(msg)
            Screen().mainloop()


###################
"""Programmstart"""
###################


app = Start(root)
root.mainloop()
