# -*- coding: cp1252 -*-
from pylab import*
from numpy import*
from datetime import datetime, date, time, timedelta
import calendar
from Tkinter import*
"""
#calculo de la actividad
m=int(input("entre el mes"))
d=int(input("entre el dia"))
fecha1 = datetime.now()   # Asigna datetime de la fecha actual
fecha2 = datetime(1978, m, d, 0, 0, 0)  # Asigna datetime específica
#fecha2 = datetime(1978, 1, 1, 0, 0, 0)  # Asigna datetime específica
diferencia = fecha1 - fecha2
print("Fecha1:", fecha1)
print("Fecha2:", fecha2)
print("Diferencia:", diferencia)
print("Entre las 2 fechas hay ", diferencia.days, "dias y ", diferencia.seconds, "seg.")
"""
def actividad():
    Ao=AoVar.get()
    yi=yiVar.get()
    mi=miVar.get()
    di=diVar.get()
    yf=yfVar.get()
    mf=mfVar.get()
    df=dfVar.get()
    Thalf=ThalfVar.get()
    A=AVar.get()
    #hoy=datetime.now()
    #datei=datetime(yi,mi,di,0,0,0)
    #datef=datetime(yf,mf,df,0,0,0)
    #dif=datef-datei #dias
    #print dif
    #t=dif*3600*24
    #print t
    years=(yf-yi)*365.0*24.0*3600.0
    print (years)
    months=(mf-mi)*30.0*24.0*3600.0
    print (months)
    days=(df-di)*24.0*3600.0
    print (days)
    t=years+months+days
    t12=Thalf*365.0*24.0*60.0*60.0
    print (t12)
    A=Ao*exp((-log(2)*t)/t12)
    print (A)
    AVar.set(A)
    
Options=["Ci","mCi","Bq"]
#master = Tk()
    
###MAIN###
root = Tk()
root.title("Actividad")
mainframe=Frame(root)
mainframe.grid()

AoVar=IntVar()
AoVar.set(int(0))
yiVar=IntVar()
yiVar.set(int(0))
yfVar=IntVar()
yfVar.set(int(0))
miVar=IntVar()
miVar.set(int(0))
mfVar=IntVar()
mfVar.set(int(0))
diVar=IntVar()
diVar.set(int(0))
dfVar=IntVar()
dfVar.set(int(0))
ThalfVar=DoubleVar()
ThalfVar.set(float(0))
AVar=IntVar()
AVar.set(float(0))

variable = StringVar()
variable.set(Options[0]) # default value

titleLabel = Label (mainframe, text = "Actividad (mCi)", font = ("Courier", 13, "bold"), justify = CENTER)
titleLabel.grid(row = 1, column = 1, columnspan = 3, pady = 10, padx = 20)

AoLabel = Label (mainframe, text = "Actividad inicial: ", font = ("Courier", 10), fg = "red",justify = CENTER)
AoLabel.grid(row = 2, column = 1, pady = 10, padx=1,sticky = NW)

w = apply(OptionMenu, (mainframe, variable) + tuple(Options))
w.grid(row=2,column=1,pady=10,padx=235,sticky=W)

yiLabel = Label (mainframe, text = "initial year: ", font = ("Courier", 10), fg = "red")
yiLabel.grid(row = 3, column = 1, pady = 10, sticky = NW)

yfLabel = Label (mainframe, text = "final year: ", font = ("Courier", 10), fg = "red")
yfLabel.grid(row = 3, column = 2, pady = 10, sticky = NW)

miLabel = Label (mainframe, text = "initial month: ", font = ("Courier", 10), fg = "red")
miLabel.grid(row = 4, column = 1, pady = 10, sticky = NW)

mfLabel = Label (mainframe, text = "final month: ", font = ("Courier", 10), fg = "red")
mfLabel.grid(row = 4, column = 2, pady = 10, sticky = NW)

diLabel = Label (mainframe, text = "initial day: ", font = ("Courier", 10), fg = "red")
diLabel.grid(row = 5, column = 1, pady = 10, sticky = NW)

dfLabel = Label (mainframe, text = "final day: ", font = ("Courier", 10), fg = "red")
dfLabel.grid(row = 5, column = 2, pady = 10, sticky = NW)

ThalfLabel = Label (mainframe, text = "Time 1/2: ", font = ("Courier", 10), fg = "red")
ThalfLabel.grid(row = 6, column = 1, pady = 10, sticky = NW)

ALabel = Label (mainframe, text = "Actividad: ", font = ("Courier", 10), fg = "blue")
ALabel.grid(row = 7, column = 1, pady = 10, sticky = NW)

AoEntry = Entry (mainframe, width = 10, bd = 5, textvariable = AoVar)
AoEntry.grid(row = 2, column = 1, pady = 10, sticky = NW, padx = 150 )

yiEntry = Entry (mainframe, width = 10, bd = 5, textvariable = yiVar)
yiEntry.grid(row = 3, column = 1, pady = 10, sticky = NW, padx = 125 )

yfEntry = Entry (mainframe, width = 10, bd = 5, textvariable = yfVar)
yfEntry.grid(row = 3, column = 2, pady = 10, sticky = NW, padx = 125 )

mEntry = Entry (mainframe, width = 10, bd = 5, textvariable = miVar)
mEntry.grid(row = 4, column = 1, pady = 10, sticky = NW, padx = 125 )

mfEntry = Entry (mainframe, width = 10, bd = 5, textvariable = mfVar)
mfEntry.grid(row = 4, column = 2, pady = 10, sticky = NW, padx = 125 )

diEntry = Entry (mainframe, width = 10, bd = 5, textvariable = diVar)
diEntry.grid(row = 5, column = 1, pady = 10, sticky = NW, padx = 125 )

dfEntry = Entry (mainframe, width = 10, bd = 5, textvariable = dfVar)
dfEntry.grid(row = 5, column = 2, pady = 10, sticky = NW, padx = 125 )

ThalfEntry = Entry (mainframe, width = 10, bd = 5, textvariable = ThalfVar)
ThalfEntry.grid(row = 6, column = 1, pady = 10, sticky = NW, padx = 125 )

AEntry = Entry (mainframe, width = 10, bd = 5, textvariable = AVar)
AEntry.grid(row = 7, column = 1, pady = 10, sticky = NW, padx = 125 )

ActividadButton =Button (mainframe, text = "Calculation", font = ("Courier", 8, "bold"), relief = RAISED, bd=5, justify = CENTER, highlightbackground = "red", overrelief = GROOVE, activebackground = "green", activeforeground="blue", command = actividad)
ActividadButton.grid(row = 8, column = 1, ipady = 8, ipadx = 12, pady = 5, sticky = NW, padx = 55)

root.mainloop()

#decaimiento radiactivo

#t = arange(1978,2016,1.0)

#A0 = 100.0
#Thalf = 31.0
#A = []
#print "%8s %8s"%("Agnos","Actividad")
#for value in t:
#    A.append(A0*exp(-0.693*(value-1978)/Thalf))

#for i in range(len(t)):
#    print "%8.1f %8.3f"%(t[i], A[i])

#plot(t,A)
#title("Decay")
#xlabel("agnos")
#ylabel("Actividad")
