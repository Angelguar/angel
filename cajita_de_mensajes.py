# importar librerias de GUI
from tkinter import *
from tkinter import messagebox

#defino mi objeto ventana 
window = Tk()
### area de ventana 

#FUNCIONES
def MSG_INFO():
  messagebox.showinfo("caja de informacion", "informacion para el usuario")

def MSG_ERROR():
    messagebox.showinfo("caja de ERROR", "informacion sobre el ERROR generado")

def MSG_WARNING():
  messagebox.showwarning("caja de Advertencia","advertir al usuario sobre algo")

def ASK_OKCANCEL():
    messagebox.askyesno("caja de SI o NO", "usuario SI o NO ?")

def ASK_YESNO():
    messagebox.askyesno("caja de SI o NO", "usuario SI o NO ?")

window.title("prueba de caja de mensajes")
#defino mis componentes
boton_ERROR = Button(window, text="caja de ERROR!", command=lambda:MSG_ERROR() )
boton_INFO = Button(window, text="caja de INFO", command=lambda:MSG_INFO() )
boton_WARNING = Button(window, text="caja de WARNING", command=lambda:MSG_WARNING() )

boton_OKCANCEL = Button(window, text="caja de OKCANCEL", command=lambda:ASK_OKCANCEL())
boton_YESNO = Button(window, text="caja de SI o NO", command=lambda:ASK_YESNO())

# genero layout de ventana
boton_ERROR.pack(padx=5, pady=5)
boton_INFO.pack(padx=5, pady=5)
boton_WARNING.pack(padx=5, pady=5)

boton_OKCANCEL.pack(padx=5, pady=5)
boton_YESNO.pack(padx=5, pady=5)

### termina area de ventana y todos sus objetos
window.mainloop()
