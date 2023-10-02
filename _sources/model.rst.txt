model Module
=============

:synopsis: The module named *model* is responsible for managing the database connection, exception handling, and the CRUD operations of our User Agenda app.


Initial Section: Database and ORM.
----------------------------------

.. note::
   **import re**
.. note::
   **from peewee import**
.. note::
   **from peewee import SqliteDatabase**
.. note::
   **from peewee import Model**
.. note::
   **from peewee import CharField**
.. note::
   **from datetime import datetime**
.. note::
   **from tkinter import messagebox**
.. note::
   **from observer import Sujeto**

Global Variables:
-----------------
.. note::
   **db = SqliteDatabase("base_prueba.db")** # Name of our Database
.. note::
   **db.connect()** # Database Connector.
.. note:: 
   **db.create_tables([Usuarios])** # Creation of the 'Usuarios' Table within our Database.


Creation/Connection of the Database and Tables.
-----------------------------------------------
.. note::
   We will use Peewee to facilitate our interaction with the database. 
   Essentially, up to line 43, we specify the name of our database and 
   the creation of a table with its respective columns and field values.
   Please check out the Peewee documentation.
.. py:class:: BaseModel(Model)

   .. py:method:: Meta()


.. py:class:: Usuarios(BaseModel) 

   .. py:method:: nombre = CharField(unique=True) 
                  apellido = CharField()
                  dni = CharField()
                  direccion = CharField()
                  pais = CharField()
                  ciudad = CharField()
                  cp = CharField()
                  telefono = CharField()
                  email = CharField() 


ABMC(Sujeto) CRUD class.
-------------------------
.. py:class:: Abmc(Sujeto)

   .. py:method:: def __init__(self,):
      print('inside CRUD class')

ABMC (Create method)
--------------------
:synopsis: We create the instance method and the parameters it will take to perform the registration. In the method, we add the regex and exception handling, as well as the variable usuarios, which indicates the name of the table where the data insertion should occur.


.. py:function:: funcion_alta_usuarios(self,nombre,apellido,dni,direccion,pais,ciudad,cp,telefono,email,tree,)

We define a variable that points to our 'usuarios' (users) table. Where the data will be added . 

   **usuarios = (Usuarios())**

The variables that store the data entered by the user will be determined as follows:

   **usuarios.nombre = var_nombre.get()**


Regex of the email field **usuarios.email_regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"** 

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
            messagebox.showinfo("User registration successful.","The user has been successfully added to the database.")  
         
         else:
            messagebox.showerror("Validation error.", "The entered email address is not valid.")  
            raise Exception("Validation error.")  # Something went wrong, time to check the entered data.
            return

ABMC (Delete method)
--------------------

:synopsis: The following method (read attribute) will fetch all the data from our 'usuarios' (User) table to display it in the user interface tree.. 


.. py:function:: funcion_baja_usuarios(var_id, tree):

   **seleccion_usuario = tree.focus()**  # Selection of the row

   **usuarios_id = tree.item(seleccion_usuario)** # When selecting with the cursor, we are indicating that it should take its ID.

   **borrar = Usuarios.get(Usuarios.id == usuarios_id["text"])** # We will delete the selected row with the obtained ID.

   **borrar.delete_instance()** # We execute the deletion of the row from our table and database with a commit.


ABMC (Update method)
--------------------

:synopsis: The 'funcion_actualizar_usuarios' method (update method) follows the logic of the previous method, selecting with the cursor a user whose data we wish to update.


.. py:function:: funcion_actualizar_usuarios(self,nombre,apellido,dni,direccion,pais,ciudad,cp,telefono,email,tree,)

   **seleccion_usuario = tree.focus()**  # Used exactly the same way as the previous method

   **actualizar = Usuarios.update(nombre=var_nombre.get()).where(Usuarios.id == usuarios_id["text"])** # Update data where the cursor is positioned.


ABMC (Read method)
------------------

:synopsis: The following method (read attribute) will fetch all the data from our 'usuarios' (User) table to display it in the user interface tree.

.. py:function:: funcion_consulta_general(tree)

   registros = tree.get_children()
        for element in registros:
            tree.delete(element)

        for (fila) in Usuarios.select():
            tree.insert(
                "",
                0,
                text=fila.id,
                values=(fila.nombre,fila.apellido,fila.dni,fila.direccion,fila.pais,fila.ciudad,fila.cp,fila.telefono,fila.email,),)

.. automodule:: model
   :members:
   :undoc-members:
   :show-inheritance: