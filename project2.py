#calcultor
from tkinter import *
from tkinter import ttk
a = Tk()
a.config(bg="Pink")
a.geometry("500x600")
a.resizable(False,False)
var = StringVar()
lb = Label(a,text="Calculator",font=("Times New Roman",30,"bold"),bg="aquamarine1")
lb.place(x=90,y=0,height=70,width=320)
entry_ = Entry(a,relief="sunken",font=("Times New Roman",30,"bold"),bd=5,textvariable=var)
entry_.place(x=25,y=80,height=60,width=450)
data = ""
def python(value):
    global data
    data = data+str(value)
    var.set(data)
def equal():
    global data
    try:
        total = str(eval(data))
        var.set(total)
    except:
        var.set("Error")
def clear():
    global data
    data=""
    var.set(data)
but_c = Button(a,text="Clear",font=("Times New Roman",30,"bold"),command=lambda:clear())
but_c.place(x=0,y=510,height=90,width=125)
#---------------------------
but_0 = Button(a,text="0",font=("Times New Roman",30,"bold"),command=lambda:python(0))
but_0.place(x=125,y=510,height=90,width=125)
#-------------------------------
but_d = Button(a,text=" . ",font=("Times New Roman",30,"bold"),command=lambda:python("."))
but_d.place(x=250,y=510,height=90,width=125)
#------------------------------------------
but_d1 = Button(a,text=" / ",font=("Times New Roman",30,"bold"),command=lambda:python("/"))
but_d1.place(x=375,y=510,height=90,width=125)
#---------------------------------------
but_1 = Button(a,text=" 1 ",font=("Times New Roman",30,"bold"),command=lambda:python(1))
but_1.place(x=0,y=420,height=90,width=125)
#----------------------------------------
but_2 = Button(a,text=" 2 ",font=("Times New Roman",30,"bold"),command=lambda:python(2))
but_2.place(x=125,y=420,height=90,width=125)
#-----------------------------------------
but_3 = Button(a,text=" 3 ",font=("Times New Roman",30,"bold"),command=lambda:python(3))
but_3.place(x=250,y=420,height=90,width=125)
#------------------------------------------
but_p = Button(a,text=" + ",font=("Times New Roman",30,"bold"),command=lambda:python("+"))
but_p.place(x=375,y=420,height=90,width=125)
#--------------------------------------------
but_4 = Button(a,text=" 4 ",font=("Times New Roman",30,"bold"),command=lambda:python(4))
but_4.place(x=0,y=330,height=90,width=125)
#-------------------------------------------
but_5 = Button(a,text=" 5 ",font=("Times New Roman",30,"bold"),command=lambda:python(5))
but_5.place(x=125,y=330,height=90,width=125)
#--------------------------------------------
but_6 = Button(a,text=" 6 ",font=("Times New Roman",30,"bold"),command=lambda:python(6))
but_6.place(x=250,y=330,height=90,width=125)
#------------------------------------------
but_m = Button(a,text=" - ",font=("Times New Roman",30,"bold"),command=lambda:python("-"))
but_m.place(x=375,y=330,height=90,width=125)
#---------------------------------------------
but_7 = Button(a,text=" 7 ",font=("Times New Roman",30,"bold"),command=lambda:python(7))
but_7.place(x=0,y=240,height=90,width=125)
#-------------------------------------------
but_8 = Button(a,text=" 8 ",font=("Times New Roman",30,"bold"),command=lambda:python(8))
but_8.place(x=125,y=240,height=90,width=125)
#--------------------------------------------
but_9 = Button(a,text=" 9 ",font=("Times New Roman",30,"bold"),command=lambda:python(9))
but_9.place(x=250,y=240,height=90,width=125)
#------------------------------------------
but_x = Button(a,text=" x ",font=("Times New Roman",30,"bold"),command=lambda:python("*"))
but_x.place(x=375,y=240,height=90,width=125)
#-------------------------------------------
but_e = Button(a,text=" = ",font=("Times New Roman",30,"bold"),command=lambda:equal())
but_e.place(x=100,y=150,height=90,width=300)


a.mainloop()