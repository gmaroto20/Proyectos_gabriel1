from tkinter import *

raiz = Tk()

miframe = Frame()
miframe.pack()

operacion = ""

resultado = 0

enpantalla = StringVar()

pantalla = Entry(miframe, textvariable=enpantalla)
pantalla.grid(row=1, column=1, padx=15, pady=15, columnspan=4)
pantalla.config(bg="yellow", justify="right")


def pulsar(num):
    global operacion
    if operacion != "":
        enpantalla.set(num)
        #operacion = ""
    else:
        enpantalla.set(enpantalla.get() + num)

# func mult div
def suma(num):
    global operacion
    global resultado

    resultado = resultado + int(num)
    enpantalla.set(resultado)

    operacion = "suma"


def resta(num):
    global operacion
    global resultado

    resultado = int(num) - resultado
    enpantalla.set(resultado)

    operacion = "resta"


def elresultado():
    global resultado
    global operacion
    if operacion == 'suma':
        enpantalla.set(resultado + int(enpantalla.get()))
    elif operacion == 'resta':
        enpantalla.set(resultado - int(enpantalla.get()))
    # multip div
    resultado = 0


tecla1 = Button(miframe, command=lambda: pulsar("1"))
tecla1.grid(row=2, column=1)
tecla1.config(text="1", width="4")

tecla2 = Button(miframe, command=lambda: pulsar("2"))
tecla2.grid(row=2, column=2)
tecla2.config(text="2", width="4")

tecla3 = Button(miframe, command=lambda: pulsar("3"))
tecla3.grid(row=2, column=3)
tecla3.config(text="3", width="4")

teclamas = Button(miframe, command=lambda: suma(enpantalla.get()))
teclamas.grid(row=2, column=4)
teclamas.config(text="+", width="4")

teclares = Button(miframe, command=lambda: resta(enpantalla.get()))
teclares.grid(row=3, column=1)
teclares.config(text="-", width="4")

teclapor = Button(miframe)
teclapor.grid(row=3, column=2)
teclapor.config(text="x", width="4")

tecladiv = Button(miframe)
tecladiv.grid(row=3, column=3)
tecladiv.config(text="/", width="4")

teclaigu = Button(miframe, command=lambda: elresultado())
teclaigu.grid(row=3, column=4)
teclaigu.config(text="=", width="4")

raiz.mainloop()