#invocamos biblioteca de funciones para GUI
from tkinter import *

#generamos el frame o marco de ventana
window = Tk()
#### todos los elementos, funciones y caracteristicas pertenecientes a las ventana

#Definimos todas las funciones en uso de la GUI
    #variable global
posicion = 0
def CLICK_ON_BUTTON(dato):
    global posicion
    EntryText.insert(posicion, dato)
    posicion = posicion + 1
    #posicion +=1

def ClearAll():
    global posicion
    EntryText.delete(0, END)
    posicion = 0

def E_BACK():
    global posicion
    posicion = posicion - 1
    EntryText.delete(posicion, END)

def RESULTADO():
    ecuacion = EntryText.get()
    resultado = eval(ecuacion)
    #resultado = eval(EntryText.get())
    EntryText.delete(0, END)
    EntryText.insert(0, resultado)
    posicion = 0 

#aspectos de configuración de ventana
window.title('calculadora final con multiples funciones')
window.configure(bg= "black")
window.geometry('200x400')
#window.geometry('200x400')

#declaración de controles en ventana
EntryText = Entry(window, bg="grey", font=("calibri 25"))

boton1 = Button(window, text="1", width=5, height=2, bg="grey", command=lambda:CLICK_ON_BUTTON(1))
boton2 = Button(window, text="2", width=5, height=2, bg="grey", command=lambda:CLICK_ON_BUTTON(2))
boton3 = Button(window, text="3", width=5, height=2, bg="grey", command=lambda:CLICK_ON_BUTTON(3))
boton4 = Button(window, text="4", width=5, height=2, bg="grey", command=lambda:CLICK_ON_BUTTON(4))
boton5 = Button(window, text="5", width=5, height=2, bg="grey", command=lambda:CLICK_ON_BUTTON(5))
boton6 = Button(window, text="6", width=5, height=2, bg="grey", command=lambda:CLICK_ON_BUTTON(6))
boton7 = Button(window, text="7", width=5, height=2, bg="grey", command=lambda:CLICK_ON_BUTTON(7))
boton8 = Button(window, text="8", width=5, height=2, bg="grey", command=lambda:CLICK_ON_BUTTON(8))
boton9 = Button(window, text="9", width=5, height=2, bg="grey", command=lambda:CLICK_ON_BUTTON(9))
boton0 = Button(window, text="0", width=5, height=2, bg="grey", command=lambda:CLICK_ON_BUTTON(0))

boton_CLR = Button(window, text="AC", width=5, height=2, command=lambda:ClearAll())
boton_Par1 = Button(window, text="(", width=5, height=2, command=lambda:CLICK_ON_BUTTON("("))
boton_Par2 = Button(window, text=")", width=5, height=2,command=lambda:CLICK_ON_BUTTON(")") )
boton_Dot = Button(window, text=".", width=5, height=2, command=lambda:CLICK_ON_BUTTON("."))
boton_Back = Button(window, text="<-", width=5, height=2, command=lambda: E_BACK())

boton_Div = Button(window, text="/", width=5, height=2, command=lambda:CLICK_ON_BUTTON("/"))
boton_Mul = Button(window, text="*", width=5, height=2, command=lambda:CLICK_ON_BUTTON("*"))
boton_ADD = Button(window, text="+", width=5, height=2, command=lambda:CLICK_ON_BUTTON("+"))
boton_SUB = Button(window, text="-", width=5, height=2, command=lambda:CLICK_ON_BUTTON("-"))
boton_EQU = Button(window, text="=", width=5, height=2, command=lambda: RESULTADO())

#configuramos la disposición de los controles en la ventana=window
EntryText.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
#EntryText.pack(padx=15, pady=5)
#EntryText.place(x=35, y=25)

boton_CLR.grid(row=1, column=0, padx=5, pady=5)
boton_Par1.grid(row=1, column=1, padx=5, pady=5)
boton_Par2.grid(row=1, column=2, padx=5, pady=5)
boton_Div.grid(row=1, column=3, padx=5, pady=5)

boton7.grid(row=2, column=0, padx=5, pady=5)
boton8.grid(row=2, column=1, padx=5, pady=5)
boton9.grid(row=2, column=2, padx=5, pady=5)
boton_Mul.grid(row=2, column=3, padx=5, pady=5)

boton4.grid(row=3, column=0, padx=5, pady=5)
boton5.grid(row=3, column=1, padx=5, pady=5)
boton6.grid(row=3, column=2, padx=5, pady=5)
boton_ADD.grid(row=3, column=3, padx=5, pady=5)

boton1.grid(row=4, column=0, padx=5, pady=5)
boton2.grid(row=4, column=1, padx=5, pady=5)
boton3.grid(row=4, column=2, padx=5, pady=5)
boton_SUB.grid(row=4, column=3, padx=5, pady=5)

boton0.grid(row=5, column=0, padx=5, pady=5)
boton_Back.grid(row=5, column=1, padx=5, pady=5)
boton_Dot.grid(row=5, column=2, padx=5, pady=5)
boton_EQU.grid(row=5, column=3, padx=5, pady=5)



#boton1.pack(padx=15, pady=5)
#boton1.place(x=100, y=40)
####termina espacio de ventana 
window=mainloop()