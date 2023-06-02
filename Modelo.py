import sqlite3
import re
from peewee import *
from peewee import SqliteDatabase
from peewee import Model
from peewee import CharField
from tkinter import messagebox


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


class Abmc:
    def __init__(
        self,
    ):
        pass

    # ######################## FUNCION ALTA USUARIOS #######################

    def funcion_alta_usuarios(
        self,
        var_nombre,
        var_apellido,
        var_dni,
        var_direccion,
        var_pais,
        var_ciudad,
        var_cp,
        var_telefono,
        var_email,
        tree,
    ):
        usuarios = (
            Usuarios()
        )
        usuarios.nombre = var_nombre.get()
        usuarios.apellido = var_apellido.get()
        usuarios.dni = var_dni.get()
        usuarios.direccion = var_direccion.get()
        usuarios.pais = var_pais.get()
        usuarios.ciudad = var_ciudad.get()
        usuarios.cp = var_cp.get()
        usuarios.telefono = var_telefono.get()
        usuarios.email = var_email.get()
        usuarios.email_regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
        if re.match(usuarios.email_regex, usuarios.email):
            try:
                usuarios.save()
                self.funcion_consulta_general(tree)
                var_nombre.set("")
                var_apellido.set("")
                var_dni.set("")
                var_direccion.set("")
                var_ciudad.set("")
                var_pais.set("")
                var_cp.set("")
                var_telefono.set("")
                var_email.set("")
            except:
                print("no pasa el try")
            else:
                messagebox.showinfo(
                    "Alta de usuario exitosa",
                    "El usuario ha sido agregado a la base de datos exitosamente.",
                )
            finally:
                print("finaliza bloque de alta")
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

    def funcion_baja_usuarios(self, var_id, tree):
        seleccion_usuario = tree.focus()
        usuarios_id = tree.item(seleccion_usuario)
        borrar = Usuarios.get(Usuarios.id == usuarios_id["text"])
        borrar.delete_instance()
        self.funcion_consulta_general(tree)

    # ######################## FUNCION ACTUALIZAR #############################

    def funcion_actualizar_usuarios(
        self,
        var_nombre,
        var_apellido,
        var_dni,
        var_direccion,
        var_pais,
        var_ciudad,
        var_cp,
        var_telefono,
        var_email,
        tree,
    ):
        seleccion_usuario = tree.focus()
        usuarios_id = tree.item(seleccion_usuario)
        actualizar = Usuarios.update(
            nombre=var_nombre.get(),
            apellido=var_apellido.get(),
            dni=var_dni.get(),
            direccion=var_direccion.get(),
            pais=var_pais.get(),
            ciudad=var_ciudad.get(),
            cp=var_cp.get(),
            telefono=var_telefono.get(),
            email=var_email.get(),
        ).where(
            Usuarios.id == usuarios_id["text"]
        )
        actualizar.execute()
        self.funcion_consulta_general(tree)
        var_nombre.set("")
        var_apellido.set("")
        var_dni.set("")
        var_direccion.set("")
        var_ciudad.set("")
        var_pais.set("")
        var_cp.set("")
        var_telefono.set("")
        var_email.set("")
