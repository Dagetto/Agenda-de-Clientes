from Modelo import Abmc
from tkinter import Menu
from tkinter import ttk
from tkinter import StringVar
from tkinter import Label
from tkinter import Entry
from tkinter import W
from tkinter import HORIZONTAL
from tkinter import VERTICAL
from tkinter import Button
from tkinter import NS
from tkinter import EW


# ################################# VISTA ##################################


class VistaPoo:
    def __init__(self, ventana_interfaz):
        self.main = ventana_interfaz
        self.objeto2_basedatos = Abmc()
        self.main.title("PyNotes")
        self.main.config(bg="#FFF7DD")
        (
            self.var_id,
            self.var_nombre,
            self.var_apellido,
            self.var_dni,
            self.var_direccion,
            self.var_pais,
            self.var_ciudad,
            self.var_cp,
            self.var_telefono,
            self.var_email,
            self.var_modifica,
        ) = (
            StringVar(),
            StringVar(),
            StringVar(),
            StringVar(),
            StringVar(),
            StringVar(),
            StringVar(),
            StringVar(),
            StringVar(),
            StringVar(),
            StringVar(),
        )
        self.titulo = Label(self.main, text="Nombre")
        self.titulo.grid(row=1, column=0, sticky=W)

        self.titulo = Label(self.main, text="Apellido")
        self.titulo.grid(row=2, column=0, sticky=W)

        self.titulo = Label(self.main, text="DNI")
        self.titulo.grid(row=3, column=0, sticky=W)

        self.titulo = Label(self.main, text="Direccion")
        self.titulo.grid(row=4, column=0, sticky=W)

        self.titulo = Label(self.main, text="Pais")
        self.titulo.grid(row=5, column=0, sticky=W)

        self.titulo = Label(self.main, text="Ciudad")
        self.titulo.grid(row=6, column=0, sticky=W)

        self.titulo = Label(self.main, text="CP")
        self.titulo.grid(row=7, column=0, sticky=W)

        self.titulo = Label(self.main, text="Telefono")
        self.titulo.grid(row=8, column=0, sticky=W)

        self.titulo = Label(self.main, text="Email")
        self.titulo.grid(row=9, column=0, sticky=W)

        self.titulo = Label(self.main, text="")
        self.titulo.grid(row=0, column=0, sticky=W)
        self.titulo = Label(self.main, text="")
        self.titulo.grid(row=10, column=0, sticky=W)

        self.entry_nombre = Entry(self.main, textvariable=self.var_nombre, width=50)
        self.entry_nombre.grid(row=1, column=1)

        self.entry_apellido = Entry(self.main, textvariable=self.var_apellido, width=50)
        self.entry_apellido.grid(row=2, column=1)

        self.entry_dni = Entry(self.main, textvariable=self.var_dni, width=50)
        self.entry_dni.grid(row=3, column=1)

        self.entry_direccion = Entry(
            self.main, textvariable=self.var_direccion, width=50
        )
        self.entry_direccion.grid(row=4, column=1)

        self.entry_pais = Entry(self.main, textvariable=self.var_pais, width=50)
        self.entry_pais.grid(row=5, column=1)

        self.entry_ciudad = Entry(self.main, textvariable=self.var_ciudad, width=50)
        self.entry_ciudad.grid(row=6, column=1)

        self.entry_cp = Entry(self.main, textvariable=self.var_cp, width=50)
        self.entry_cp.grid(row=7, column=1)

        self.entry_telefono = Entry(self.main, textvariable=self.var_telefono, width=50)
        self.entry_telefono.grid(row=8, column=1)

        self.entry_email = Entry(self.main, textvariable=self.var_email, width=50)
        self.entry_email.grid(row=9, column=1)

        self.tree = ttk.Treeview(self.main)
        self.tree["columns"] = (
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

        self.tree.column("#0", width=20, minwidth=50, anchor=W)
        self.tree.column("col1", width=90, minwidth=100, anchor=W)
        self.tree.column("col2", width=90, minwidth=100, anchor=W)
        self.tree.column("col3", width=80, minwidth=80, anchor=W)
        self.tree.column("col4", width=150, minwidth=150, anchor=W)
        self.tree.column("col5", width=80, minwidth=100, anchor=W)
        self.tree.column("col6", width=100, minwidth=100, anchor=W)
        self.tree.column("col7", width=20, minwidth=50, anchor=W)
        self.tree.column("col8", width=30, minwidth=120, anchor=W)
        self.tree.column("col9", width=120, minwidth=210, anchor=W)
        self.tree.heading("#0", text="ID")
        self.tree.heading("col1", text="Nombre")
        self.tree.heading("col2", text="Apellido")
        self.tree.heading("col3", text="DNI")
        self.tree.heading("col4", text="Dirección")
        self.tree.heading("col5", text="País")
        self.tree.heading("col6", text="Ciudad")
        self.tree.heading("col7", text="CP")
        self.tree.heading("col8", text="Teléfono")
        self.tree.heading("col9", text="Email")
        self.tree.grid(column=0, row=12, columnspan=5)

        scrollbar_v = ttk.Scrollbar(self.main, orient=VERTICAL, command=self.tree.yview)
        scrollbar_v.grid(row=12, column=6, sticky=NS)
        self.tree.configure(yscrollcommand=scrollbar_v.set)

        scrollbar_h = ttk.Scrollbar(
            self.main, orient=HORIZONTAL, command=self.tree.xview
        )
        scrollbar_h.grid(row=13, column=0, columnspan=25, sticky=EW)
        self.tree.configure(xscrollcommand=scrollbar_h.set)

        # ################BOTONES#################

        boton_cliente = Button(
            self.main,
            text="CLIENTES",
            padx=73,
            pady=1,
            command=lambda: self.objeto2_basedatos.funcion_consulta_general(self.tree),
        )
        boton_cliente.grid(row=1, column=4)

        boton_alta = Button(
            self.main,
            text="ALTA DE USUARIO",
            padx=50,
            pady=1,
            command=lambda: self.objeto2_basedatos.funcion_alta_usuarios(
                self.var_nombre,
                self.var_apellido,
                self.var_dni,
                self.var_direccion,
                self.var_pais,
                self.var_ciudad,
                self.var_cp,
                self.var_telefono,
                self.var_email,
                self.tree,
            ),
        )
        boton_alta.grid(row=4, column=4)

        boton_baja = Button(
            self.main,
            text="BAJA DE USUARIO",
            padx=51,
            pady=1,
            command=lambda: self.objeto2_basedatos.funcion_baja_usuarios(
                self.var_id, self.tree
            ),
        )
        boton_baja.grid(row=6, column=4)

        boton_actualizar = Button(
            self.main,
            text="ACTUALIZAR DATOS",
            padx=45,
            pady=1,
            command=lambda: self.objeto2_basedatos.funcion_actualizar_usuarios(
                self.var_nombre,
                self.var_apellido,
                self.var_dni,
                self.var_direccion,
                self.var_pais,
                self.var_ciudad,
                self.var_cp,
                self.var_telefono,
                self.var_email,
                self.tree,
            ),
        )
        boton_actualizar.grid(row=8, column=4)

        #######################################################
