import sqlite3
import re
from peewee import *
from peewee import SqliteDatabase
from peewee import Model
from peewee import CharField
from tkinter import messagebox
from datetime import datetime
from observador import Sujeto

db = SqliteDatabase(
    "base_prueba.db"
)


class BaseModel(Model):
    class Meta:
        database = db


class Usuarios(BaseModel):
    nombre = CharField(unique=True)
    apellido = CharField()
    dni = CharField()
    direccion = CharField()
    pais = CharField()
    ciudad = CharField()
    cp = CharField()
    telefono = CharField()
    email = CharField()


db.connect()
db.create_tables([Usuarios])


def decorador_alta(funcion):
    def envoltura(*args,):
        a = funcion(*args)
        registro = open("Registro de ABMC.txt", "a")
        registro.write("Se ha realizado un alta nueva\n ")
        registro.write(str(datetime.now()) + ("\n"))
        registro.close()
        print('SE HA REALIZADO UN ALTA DE REGISTRO NUEVO')
        return a
    return envoltura


def decorador_baja(funcion):
    def envoltura(
        *args,
    ):
        b = funcion(*args)
        registro = open("Registro de ABMC.txt", "a")
        registro.write("Se ha realizado una baja\n ")
        registro.write(str(datetime.now()) + ("\n"))
        registro.close()
        print('SE HA REALIZADO UNA BAJA DE REGISTRO')
        return b
    return envoltura


def decorador_modificacion(funcion):
    def envoltura(
        *args,
    ):
        m = funcion(*args)
        registro = open("Registro de ABMC.txt", "a")
        registro.write("Se ha realizado una modificacion\n ")
        registro.write(str(datetime.now()) + ("\n"))
        registro.close()
        print('SE HA REALIZADO UNA MODIFICACION DE REGISTRO')
        return m
    return envoltura


class Abmc(Sujeto):
    def __init__(
        self,
    ):
        print('Dentro de la clase ABMC')

    # ######################## FUNCION ALTA USUARIOS #######################

    @decorador_alta
    def funcion_alta_usuarios(
        self,
        nombre,
        apellido,
        dni,
        direccion,
        pais,
        ciudad,
        cp,
        telefono,
        email,
        tree,
    ):
        usuarios = Usuarios()

        usuarios.nombre = nombre.get()
        usuarios.apellido = apellido.get()
        usuarios.dni = dni.get()
        usuarios.direccion = direccion.get()
        usuarios.pais = pais.get()
        usuarios.ciudad = ciudad.get()
        usuarios.cp = cp.get()
        usuarios.telefono = telefono.get()
        usuarios.email = email.get()
        regex = "[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+.[A-Z|a-z]"
        if re.match(regex, usuarios.email):  # Regex del campo Email
            usuarios.save()
            self.funcion_consulta_general(tree)
            self.notificar(nombre.get(), apellido.get(), email.get())
            nombre.set("")
            apellido.set("")
            dni.set("")
            direccion.set("")
            ciudad.set("")
            pais.set("")
            cp.set("")
            telefono.set("")
            email.set("")
            messagebox.showinfo(
                "Alta de usuario exitosa",
                "El usuario ha sido agregado a la base de datos exitosamente.",
            )
        else:
            messagebox.showerror(
                "Error de validación", "El correo electrónico ingresado no es válido."
            )
            raise Exception("error al validar campo 'Mail'")
            return

# ##################### FUNCION CONSULTA GENERAL #########################

    def funcion_consulta_general(self, tree):
        registros = tree.get_children()
        for element in registros:
            tree.delete(element)

        for (
            fila
        ) in Usuarios.select():
            tree.insert(
                "",
                0,
                text=fila.id,
                values=(
                    fila.nombre,
                    fila.apellido,
                    fila.dni,
                    fila.direccion,
                    fila.pais,
                    fila.ciudad,
                    fila.cp,
                    fila.telefono,
                    fila.email,
                ),
            )

    # ##################### FUNCION BAJA DE USUARIOS #########################
    @decorador_baja
    def funcion_baja_usuarios(self, var_id, tree):
        seleccion_usuario = tree.focus()
        usuarios_id = tree.item(seleccion_usuario)
        borrar = Usuarios.get(Usuarios.id == usuarios_id["text"])
        borrar.delete_instance()
        self.funcion_consulta_general(tree)

    # ######################## FUNCION ACTUALIZAR #############################
    @decorador_modificacion
    def funcion_actualizar_usuarios(
        self,
        nombre,
        apellido,
        dni,
        direccion,
        pais,
        ciudad,
        cp,
        telefono,
        email,
        tree,
    ):
        seleccion_usuario = tree.focus()
        usuarios_id = tree.item(seleccion_usuario)
        actualizar = Usuarios.update(
            nombre=nombre.get(),
            apellido=apellido.get(),
            dni=dni.get(),
            direccion=direccion.get(),
            pais=pais.get(),
            ciudad=ciudad.get(),
            cp=cp.get(),
            telefono=telefono.get(),
            email=email.get(),
        ).where(
            Usuarios.id == usuarios_id["text"]
        )
        actualizar.execute()
        self.funcion_consulta_general(tree)
        nombre.set("")
        apellido.set("")
        dni.set("")
        direccion.set("")
        ciudad.set("")
        pais.set("")
        cp.set("")
        telefono.set("")
        email.set("")
