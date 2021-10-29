from tkinter import *
#Creando ventana raiz
root = Tk()


label = Label(root, text="Nombre")
label.grid(row=0, column=0, sticky="e",padx=8, pady=8)

entry = Entry(root)
entry.grid(row=0, column=1, padx=8, pady=8)
entry.config(justify="center", state="disable")


label2 = Label(root, text="Apellidos",padx=8, pady=8)
label2.grid(row=1, column=0, sticky="w")

entry2 = Entry(root)
entry2.grid(row=1, column=1,padx=8, pady=8)
entry2.config(justify="right")

label3 = Label(root, text="Contraseña",padx=8, pady=8)
label3.grid(row=2, column=0, sticky="w")

entry3 = Entry(root)
entry3.grid(row=2, column=1,padx=8, pady=8)
entry3.config(justify="center", show="x")

#creando ciclo  #Emelyn Rodriguez Lila
root.mainloop()