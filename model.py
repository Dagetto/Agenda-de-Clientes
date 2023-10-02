import re
from peewee import *
from peewee import SqliteDatabase  # we're using Peewee ORM. you can you check the documentation to understand what happens up to line 43
from peewee import Model
from peewee import CharField
from tkinter import messagebox
from datetime import datetime
from observer import Sujeto


"""
We will use Peewee to facilitate our interaction with the database. 
Essentially, up to line 43, we specify the name of our database and 
the creation of a table with its respective columns and field values.
Please check out the Peewee documentation.
"""
db = SqliteDatabase(
    "base_prueba.db"
)  # Name o the DB


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

# We list all the fields that our database will have.


db.connect()  # DB connector
db.create_tables([Usuarios])  # Name of the Table

"""Let's define three decorators to log CRUD information to a text file """
# 'Create attribute' decorator for the CRUD methods


def decorador_alta(funcion):
    def envoltura(*args,):
        a = funcion(*args)
        registro = open("CRUD register.txt", "a")
        registro.write("A new registration has been added.\n ")
        registro.write(str(datetime.now()) + ("\n"))
        registro.close()
        print('A new registration has been added.')
        return a
    return envoltura

# 'Delete attribute' decorator


def decorador_baja(funcion):
    def envoltura(
        *args,
    ):
        b = funcion(*args)
        registro = open("CRUD register.txt", "a")
        registro.write("A deletion has been performed.\n ")
        registro.write(str(datetime.now()) + ("\n"))
        registro.close()
        print('A deletion has been performed.')
        return b
    return envoltura

# 'Update attribute' decorator


def decorador_modificacion(funcion):
    def envoltura(
        *args,
    ):
        m = funcion(*args)
        registro = open("CRUD register.txt", "a")
        registro.write("A register modification has been made.\n ")
        registro.write(str(datetime.now()) + ("\n"))
        registro.close()
        print('A register modification has been made.')
        return m
    return envoltura


"""
The ABMC class contains all the CRUD functions.
We will explain the 'function_alta_usuarios' (Create)
to understand how to retrieve user-entered data from the interface
and save it in the created database.
"""


class Abmc(Sujeto):
    def __init__(
        self,
    ):
        print('inside CRUD class')

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
    ):  # we define our method "funcion_alta_usuarios (create Attribute), and specify the parameters it will take to execute a user registration."
        usuarios = Usuarios()  # We define a variable that points to our 'usuarios' (users) table. Where the data will be added .

        usuarios.nombre = nombre.get()
        usuarios.apellido = apellido.get()
        usuarios.dni = dni.get()
        usuarios.direccion = direccion.get()  # So, here we have our 'usuarios' (users) variable pointing to our table and the 'direccion' (address) column.
        usuarios.pais = pais.get()  # The same applies to all columns. After assigning table+column, we use .get() to retrieve that information.
        usuarios.ciudad = ciudad.get()
        usuarios.cp = cp.get()
        usuarios.telefono = telefono.get()
        usuarios.email = email.get()
        regex = "[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+.[A-Z|a-z]"    # Regex of the email field
        if re.match(regex, usuarios.email):  # little if/else to check regex
            usuarios.save()  # if this it's true the data will be added and saved in our database.
            self.funcion_consulta_general(tree)  # We call the 'funcion_consulta_general' (read attribute) to update the user interface tree.
            self.notificar(nombre.get(), apellido.get(), email.get())  # We invoke the 'notify' method of the 'Sujeto' (subject) class to return certain obtained parameters. We could request any element, but for this case, it will be enough to obtain the name, last name, and email of the entered user.
            nombre.set("")
            apellido.set("")
            dni.set("")
            direccion.set("")  # Cleaning fields of the interface
            ciudad.set("")
            pais.set("")
            cp.set("")
            telefono.set("")
            email.set("")
            messagebox.showinfo(
                "User registration successful.",
                "The user has been successfully added to the database.",
            )  # success creating and saving a new record.
        else:
            messagebox.showerror(
                "Validation error.", "The entered email address is not valid."
            )  # Error while checking the regex.
            raise Exception("Validation error.'")  # Something went wrong, time to check the entered data.
            return

# ##################### FUNCION CONSULTA GENERAL #########################
    """
    The following method (read attribute) will fetch all the data from our 'usuarios' (User) table to display it in the user interface tree.
    """
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

    """
    The 'funcion_baja_usuarios' method (delete method) will delete the entire selected row with the cursor.
    """
    @decorador_baja
    def funcion_baja_usuarios(self, var_id, tree):
        seleccion_usuario = tree.focus()
        usuarios_id = tree.item(seleccion_usuario)  # Selection of the row
        borrar = Usuarios.get(Usuarios.id == usuarios_id["text"])  # When selecting with the cursor, we are indicating that it should take its ID.
        borrar.delete_instance()  # We execute the deletion of the row from our table and database.
        self.funcion_consulta_general(tree)

    # ######################## FUNCION ACTUALIZAR #############################
    """
    The 'funcion_actualizar_usuarios' method (update method) follows the logic of the previous method,
    selecting with the cursor a user whose data we wish to update.
    """

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
        seleccion_usuario = tree.focus()  # Used exactly the same way as the previous method
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
        )  # Update data where the cursor is positioned.
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
