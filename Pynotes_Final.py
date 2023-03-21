import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import re

###################FUNCION DB###########################


def funcion_crear_base():
    con = sqlite3.connect("basededatos.db")
    return con


funcion_crear_base()


def funcion_crear_tabla(con):
    cursor = con.cursor()
    sql = "CREATE TABLE Usuarios(ID INTEGER PRIMARY KEY AUTOINCREMENT, nombre VARCHAR(20), apellido VARCHAR(20), dni VARCHAR(20), direccion VARCHAR(20), pais VARCHAR(20), ciudad VARCHAR(30), codigoPostal VARCHAR(20), telefono VARCHAR(20), email VARCHAR(30))"
    cursor.execute(sql)
    con.commit()

try:
    con = funcion_crear_base()
    funcion_crear_tabla(con)
except:
    pass

################################## SECCION INICIAL TKINTER ##################################

main = Tk()
main.title("PyNotes")
main.config(bg="#FFF7DD")

var_id = StringVar()
var_nombre = StringVar()
var_apellido = StringVar()
var_dni = StringVar()
var_direccion = StringVar()
var_pais = StringVar()
var_ciudad = StringVar()
var_cp = StringVar()
var_telefono = StringVar()
var_email = StringVar()
var_modifica = StringVar()

titulo = Label(main, text="Nombre")
titulo.grid(row=1, column=0, sticky=W)

titulo = Label(main, text="Apellido")
titulo.grid(row=2, column=0, sticky=W)

titulo = Label(main, text="DNI")
titulo.grid(row=3, column=0, sticky=W)

titulo = Label(main, text="Direccion")
titulo.grid(row=4, column=0, sticky=W)

titulo = Label(main, text="Pais")
titulo.grid(row=5, column=0, sticky=W)

titulo = Label(main, text="Ciudad")
titulo.grid(row=6, column=0, sticky=W)

titulo = Label(main, text="CP")
titulo.grid(row=7, column=0, sticky=W)

titulo = Label(main, text="Telefono")
titulo.grid(row=8, column=0, sticky=W)

titulo = Label(main, text="Email")
titulo.grid(row=9, column=0, sticky=W)

titulo = Label(main, text="ID")
titulo.grid(row=10, column=0, sticky=W)

titulo = Label(main, text="")  # separador entrys/treeview
titulo.grid(row=0, column=0, sticky=W)
titulo = Label(main, text="")  # separador entrys/treeview
titulo.grid(row=11, column=0, sticky=W)

entry_id = Entry(main, textvariable=var_id, width=50)
entry_id.grid(row=10, column=1)

entry_nombre = Entry(main, textvariable=var_nombre, width=50)
entry_nombre.grid(row=1, column=1)

entry_apellido = Entry(main, textvariable=var_apellido, width=50)
entry_apellido.grid(row=2, column=1)

entry_dni = Entry(main, textvariable=var_dni, width=50)
entry_dni.grid(row=3, column=1)

entry_direccion = Entry(main, textvariable=var_direccion, width=50)
entry_direccion.grid(row=4, column=1)

entry_pais = Entry(main, textvariable=var_pais, width=50)
entry_pais.grid(row=5, column=1)

entry_ciudad = Entry(main, textvariable=var_ciudad, width=50)
entry_ciudad.grid(row=6, column=1)

entry_cp = Entry(main, textvariable=var_cp, width=50)
entry_cp.grid(row=7, column=1)

entry_telefono = Entry(main, textvariable=var_telefono, width=50)
entry_telefono.grid(row=8, column=1)

entry_email = Entry(main, textvariable=var_email, width=50)
entry_email.grid(row=9, column=1)

##################TREEVIEW########################################

tree = ttk.Treeview(main)
tree["columns"] = (
    "col1",
    "col2",
    "col3",
    "col4",
    "col5",
    "col6",
    "col7",
    "col8",
    "col9",
)

tree.column("#0", width=20, minwidth=50, anchor=W)
tree.column("col1", width=90, minwidth=100, anchor=W)
tree.column("col2", width=90, minwidth=100, anchor=W)
tree.column("col3", width=80, minwidth=80, anchor=W)
tree.column("col4", width=150, minwidth=150, anchor=W)
tree.column("col5", width=80, minwidth=100, anchor=W)
tree.column("col6", width=100, minwidth=100, anchor=W)
tree.column("col7", width=20, minwidth=50, anchor=W)
tree.column("col8", width=30, minwidth=120, anchor=W) #telefono
tree.column("col9", width=120, minwidth=210, anchor=W)
tree.heading("#0", text="ID")
tree.heading("col1", text="Nombre")
tree.heading("col2", text="Apellido")
tree.heading("col3", text="DNI")
tree.heading("col4", text="Dirección")
tree.heading("col5", text="País")
tree.heading("col6", text="Ciudad")
tree.heading("col7", text="CP")
tree.heading("col8", text="Teléfono")
tree.heading("col9", text="Email")
tree.grid(column=0, row=12, columnspan=5)

scrollbar_v = ttk.Scrollbar(main, orient=VERTICAL, command=tree.yview)
scrollbar_v.grid(row=12, column=6, sticky=NS)
tree.configure(yscrollcommand=scrollbar_v.set)

scrollbar_h = ttk.Scrollbar(main, orient=HORIZONTAL, command=tree.xview)
scrollbar_h.grid(row=13, column=0, columnspan=25, sticky=EW)
tree.configure(xscrollcommand=scrollbar_h.set)

######################### FUNCION ALTA USUARIOS #######################

def funcion_alta_usuarios():
    cursor = con.cursor()

    email_regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
    if not re.match(email_regex, var_email.get()):
        messagebox.showerror(
            "Error de validación", "El correo electrónico ingresado no es válido."
        )
        return

    sql = "INSERT INTO Usuarios(nombre, apellido, dni, direccion, pais, ciudad, codigoPostal, telefono, email) VALUES (?,?,?,?,?,?,?,?,?); "
    datos = (
        (var_nombre.get()),
        (var_apellido.get()),
        (var_dni.get()),
        (var_direccion.get()),
        (var_pais.get()),
        (var_ciudad.get()),
        (var_cp.get()),
        (var_telefono.get()),
        (var_email.get()),
    )
    cursor.execute(sql, datos)
    tree.insert(
        "",
        "end",
        values=(
            var_nombre.get(),
            var_apellido.get(),
            var_dni.get(),
            var_direccion.get(),
            var_pais.get(),
            var_ciudad.get(),
            var_cp.get(),
            var_telefono.get(),
            var_email.get(),
        ),
    )
    con.commit()

    messagebox.showinfo(
        "Alta de usuario exitosa",
        "El usuario ha sido agregado a la base de datos exitosamente.",
    )

    entry_nombre.delete(0, "end")  # BORRA LOS CAMPOS DE ENTRADA DESPUES DE CADA ALTA
    entry_apellido.delete(0, "end")
    entry_dni.delete(0, "end")
    entry_direccion.delete(0, "end")
    entry_pais.delete(0, "end")
    entry_ciudad.delete(0, "end")
    entry_cp.delete(0, "end")
    entry_telefono.delete(0, "end")
    entry_email.delete(0, "end")

    print(
        (var_nombre.get()),
        (var_apellido.get()),
        (var_dni.get()),
        (var_direccion.get()),
        (var_pais.get()),
        (var_ciudad.get()),
        (var_cp.get()),
        (var_telefono.get()),
        (var_email.get()),
    )


con = funcion_crear_base()

###################### FUNCION CONSULTA DE USUARIOS #############################

def funcion_consulta_usuarios(var_dni):
    sql = "SELECT * FROM usuarios WHERE dni = ?"
    cursor = con.cursor()
    cursor.execute(sql, (var_dni,))
    tabla = cursor.fetchall()

    for i in tabla:
        var_id.set(i[0])
        var_nombre.set(i[1])
        var_apellido.set(i[2])
        var_direccion.set(i[4])
        var_pais.set(i[5])
        var_ciudad.set(i[6])
        var_cp.set(i[7])
        var_telefono.set(i[8])
        var_email.set(i[9])

    return tabla

def cargar_datos(var_dni):
    tree.delete(*tree.get_children())
    datos = funcion_consulta_usuarios(var_dni)

    for fila in datos:
        tree.insert(
            "",
            END,
            text=fila[0],
            values=(
                fila[1],
                fila[2],
                fila[3],
                fila[4],
                fila[5],
                fila[6],
                fila[7],
                fila[8],
                fila[9],
            ),
        )

###################### FUNCION CONSULTA GENERAL #############################

def funcion_consulta_general():
    sql = "SELECT * FROM usuarios"
    cursor = con.cursor()
    cursor.execute(sql)
    tabla = cursor.fetchall()
    return tabla

def cargar_datos_general():
    tree.delete(*tree.get_children())
    datos = funcion_consulta_general()

    for fila in datos:
        tree.insert(
            "",
            END,
            text=fila[0],
            values=(
                fila[1],
                fila[2],
                fila[3],
                fila[4],
                fila[5],
                fila[6],
                fila[7],
                fila[8],
                fila[9],
            ),
        )

###################### FUNCION BAJA DE USUARIOS #############################

def funcion_baja_usuarios(var_id):
    cursor = con.cursor()
    id_string = var_id.get()

    id_integer = int(id_string)

    cursor.execute("SELECT * FROM Usuarios WHERE ID = ?", (id_integer,))
    listado_id = cursor.fetchone()

    if listado_id is None:
        messagebox.showinfo(
            "No se ha podido dar de baja al usuario indicado",
            "Introduzca un ID válido.",
        )
    else:
        sql = "DELETE FROM Usuarios WHERE ID = ?"
        cursor.execute(sql, (id_integer,))
        con.commit()
        messagebox.showinfo(
            "Baja de usuario exitosa",
            "El usuario ha sido eliminado de la base de datos exitosamente.",
        )

    entry_nombre.delete(0, "end")  # BORRA LOS CAMPOS DE ENTRADA DESPUES DE CADA BAJA
    entry_apellido.delete(0, "end")
    entry_dni.delete(0, "end")
    entry_direccion.delete(0, "end")
    entry_pais.delete(0, "end")
    entry_ciudad.delete(0, "end")
    entry_cp.delete(0, "end")
    entry_telefono.delete(0, "end")
    entry_email.delete(0, "end")
    entry_id.delete(0,"end")

######################### FUNCION ACTUALIZAR #############################

def funcion_actualizar_usuarios():
    sql = "UPDATE Usuarios SET nombre = ?, apellido = ?, dni = ?, direccion = ?, pais = ?, ciudad = ?, codigoPostal = ?, telefono = ?, email = ? WHERE dni = ?"
    datos = (
        (var_nombre.get()),
        (var_apellido.get()),
        (var_dni.get()),
        (var_direccion.get()),
        (var_pais.get()),
        (var_ciudad.get()),
        (var_cp.get()),
        (var_telefono.get()),
        (var_email.get()),
        (var_dni.get()),
    )
    cursor = con.cursor()
    cursor.execute(sql, datos)
    con.commit()
    messagebox.showinfo(
        "Modificación de datos del usuario exitosa",
        "Los datos del usuario han sido modificados exitosamente.",
    )
    print((var_nombre.get()), (var_apellido.get()), (var_dni.get()))

    entry_id.delete(0, "end")
    entry_nombre.delete(0, "end")
    entry_apellido.delete(0, "end")
    entry_dni.delete(0, "end")
    entry_direccion.delete(0, "end")
    entry_pais.delete(0, "end")
    entry_ciudad.delete(0, "end")
    entry_cp.delete(0, "end")
    entry_telefono.delete(0, "end")
    entry_email.delete(0, "end")

#################BOTONES#################

boton_cliente = Button(main, text="CLIENTES", padx=73, pady=1, command=cargar_datos_general)
boton_cliente.grid(row=1, column=4)

boton_alta = Button(main, text="ALTA DE USUARIO", padx=50, pady=1, command=funcion_alta_usuarios)
boton_alta.grid(row=4, column=4)

boton_baja = Button(
    main, text="BAJA DE USUARIO", padx=51, pady=1, command=lambda: funcion_baja_usuarios(var_id)
)
boton_baja.grid(row=6, column=4)

boton_actualizar = Button(
    main, text="ACTUALIZAR DATOS", padx=45, pady=1, command=funcion_actualizar_usuarios
)
boton_actualizar.grid(row=8, column=4)

boton_consulta = Button(
    main, text="CONSULTA", padx=70, pady=1, command=lambda: cargar_datos(var_dni.get())
)
boton_consulta.grid(row=10, column=4)

#######################################################

main.mainloop()
