from tkinter import *
from tkinter import Tk, Label, StringVar
ventana_principal=Tk()

z=0

def calcular(): 
    for k in range(int(entry_c.get())):
        
        for i in range(int(entry_a.get())):
            c.create_rectangle(70+(80*i), 70+(50*k), 150+(80*i),120+(50*k), fill="green",outline="black")
   




entry_a=StringVar
entry_b=StringVar

ventana_principal.title("Parcial")
ventana_principal.geometry("500x500")
ventana_principal.resizable(0,0)
ventana_principal.config(bg= "black")

frame_operaciones = Frame(ventana_principal)
frame_operaciones.config(bg="darkorchid", width=480, height=190)
frame_operaciones.place(x=10,y=20)

lb_x = Label(frame_operaciones, text = "Dígita el numero de columnas: ")
lb_x.config(bg="darkorchid", fg="black", font=("Arial",12))
lb_x.place(x=20,y=30,width=300, height=30)

entry_a= Entry(frame_operaciones)
entry_a.config(font=("Arial",20), justify=LEFT, fg="black")
entry_a.focus_set()
entry_a.place(x=295,y=30,width=115, height=30)

lb_x = Label(frame_operaciones, text = "Dígita el numero de filas: ")
lb_x.config(bg="darkorchid", fg="black", font=("Arial",12))
lb_x.place(x=20,y=50,width=300, height=30)

entry_c= Entry(frame_operaciones)
entry_c.config(font=("Arial",20), justify=LEFT, fg="black")
entry_c.focus_set()
entry_c.place(x=265,y=60,width=105, height=30)

lb_x = Label(frame_operaciones, text = "Número a Buscar: ")
lb_x.config(bg="darkorchid", fg="black", font=("Arial",12))
lb_x.place(x=10,y=90,width=300, height=30)
entry_b= Entry(frame_operaciones)
entry_b.config(font=("Arial",20), justify=LEFT, fg="black")
entry_b.focus_set()
entry_b.place(x=205,y=100,width=115, height=30)

bt_borrar = Button(frame_operaciones, text="Calcular", command=calcular)
bt_borrar.place(x=170,y=125, width=90, height=30)


frame_resultados = Frame(ventana_principal)
frame_resultados.config(bg="white", width=480, height=250)
frame_resultados.place(x=10,y=230)





ventana_principal.mainloop()


