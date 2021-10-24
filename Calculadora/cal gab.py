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
refresca = 0

def pulsar(num):
    global operacion
    global refresca
    #if operacion != "" :
    if refresca == 1:
        enpantalla.set(num)
        refresca = 0

        # operacion = "" la he quitado
    else:
        # concatenar numeros en pantalla
        enpantalla.set(enpantalla.get() + num)

def reinicio():
    enpantalla.set(0) #balblabla

def suma(num):
    global operacion
    global resultado
    global refresca

    resultado = resultado + float(num)
    enpantalla.set(resultado)

    operacion = "suma"
    refresca = 1


def resta(num):
    global operacion
    global resultado
    global refresca

    resultado = float(num) - resultado
    enpantalla.set(resultado)

    operacion = "resta"
    refresca = 1

def multiplica(num):

    global operacion
    global resultado
    global refresca

    resultado=float(num)

    operacion="multiplica"
    refresca = 1

def divide(num):
    global operacion
    global resultado
    global refresca

    resultado=float(num)

    operacion="divide"
    refresca = 1


def elresultado():
    global resultado
    global operacion
    global refresca

    if operacion == "suma":

        enpantalla.set(round(resultado + float(enpantalla.get()),2))

    elif operacion == "resta":

        enpantalla.set(resultado - float(enpantalla.get()))

    elif operacion=="multiplica":

        enpantalla.set(resultado*float(enpantalla.get()))

    elif operacion=="divide":

        enpantalla.set(resultado / float(enpantalla.get()))

    resultado = 0


tecla1 = Button(miframe, command=lambda: pulsar("0"))
tecla1.grid(row=2, column=1)
tecla1.config(text="0", width="4")

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

teclapor = Button(miframe,command=lambda: multiplica(enpantalla.get()))
teclapor.grid(row=3, column=2)
teclapor.config(text="x", width="4")

tecladiv = Button(miframe,command=lambda: divide(enpantalla.get()))
tecladiv.grid(row=3, column=3)
tecladiv.config(text="/", width="4")

teclaigu = Button(miframe, command=lambda: elresultado())
teclaigu.grid(row=3, column=4)
teclaigu.config(text="=", width="4")

teclarei = Button(miframe, command=lambda: reinicio())
teclarei.grid(row=4, column=1)
teclarei.config(text="C", width="4")

raiz.mainloop()