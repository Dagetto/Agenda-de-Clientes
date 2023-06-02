Módulo Modelo
=============

:synopsis: El módulo denomiado *Modelo* se encarga de gestionar la conexión a la Base de Datos, el manejo de excepciones y el CRUD de nuestra App Agenda de Usuarios.


Seccion inicial: Base de Datos y ORM.
-------------------------------------

.. note::
   **import sqlite3** 
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
   **from tkinter import messagebox**

Variables Globales:
-------------------
.. note::
   **db = SqliteDatabase("base_prueba.db")** # Nombre de nuestra Bases de Datos.
.. note::
   **db.connect()** # Conector a Base de Datos.
.. note:: 
   **db.create_tables([Usuarios])** # Creacion de la Tabla 'Usuarios' dentro de nuestra Base de Datos.


Creación/conexión de Base de Datos y Tablas
--------------------------------------------
.. py:class:: BaseModel(Model)

   .. py:method:: Meta()


.. py:class:: Usuarios(BaseModel) 

   .. py:method:: nombre = CharField(unique=True) # Campos de la Tabla
                  apellido = CharField()
                  dni = CharField()
                  direccion = CharField()
                  pais = CharField()
                  ciudad = CharField()
                  cp = CharField()
                  telefono = CharField()
                  email = CharField() 


ABMC (CRUD) y sus métodos
-------------------------
.. py:class:: Abmc

   .. py:method:: def __init__(self,):
      pass

ABMC (Alta)
------------
:synopsis: Creamos el método de instancia y los parámetros que tomará para realizar el alta. En el método se agrega el *regex* y *manejo de excepciones*, así como también la variable *usuarios* que indica el nombre de la tabla donde debe generarse la inserción de datos.


.. py:function:: funcion_alta_usuarios(var_nombre,var_apellido,var_dni,var_direccion,var_pais,var_ciudad,var_cp,var_telefono,var_email,tree,)


   :param str var_nombre:  Cada parámetro iniciado con la palabra 'var' indica el campo y dato que el usuario ingresará mediante la interfaz gráfica. 
   
   :param str tree:  El parámetro 'tree' se encarga de ingresar los datos ingresados en el treeview de nuestra app. 

Asignamos una variable referida a la tabla en la cual inseriremos los datos obtenidos del usuario. 

   **usuarios = (Usuarios())**

Las variables que almacenan los datos ingresados por el usuario se determinarán de la siguiente manera:

   **usuarios.nombre = var_nombre.get()**

.. note::

   La misma forma se adapta para el regex **usuarios.email_regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"**

Para finalizar el alta se aplica un bloque con el condicional *if/else*  y dentro de el aplicamos la secuencia *try/except/else/finally* 

if re.match(usuarios.email_regex, usuarios.email): #  tomamos el regex y los datos ingresados por el usuario  
            try:
                usuarios.save() # Realiza el commit con los datos ingresados.
                self.funcion_consulta_general(tree) # Ingresa los datos en el treeview.
            except:
                print("no pasa el try")
            else:
                messagebox.showinfo(
                    "Alta de usuario exitosa",
                    "El usuario ha sido agregado a la base de datos exitosamente.",) # Mensaje divisado por el usuario y generado por *Tkinter* messagebox
            finally:
                print("finaliza bloque de alta")

else: # Ejecutamos un manejo de excepciones si el regex no se cumple
   raise Exception("error al validar campo 'Mail'") 
   messagebox.showerror("Error de validación", "El correo electrónico ingresado no es válido.")


ABMC (Baja)
------------

:synopsis: Creamos el método de instancia y los parámetros que tomará para realizar la baja. 


.. py:function:: funcion_baja_usuarios(var_id, tree):

   **seleccion_usuario = tree.focus()**  # Permite seleccionar una fila en el treeeview por el usuario.

   **usuarios_id = tree.item(seleccion_usuario)** # Asignamos una variable con la fila seleccionada en treeview.

   **borrar = Usuarios.get(Usuarios.id == usuarios_id["text"])** # indicamos que la baja se ejecutará sobre la fila seleccionada.

   **borrar.delete_instance()** # Borra la fila indicada y genera un commit en nuestra Base de Datos.

   **self.funcion_consulta_general(tree)** # Actualiza el treeview.

ABMC (Modificación)
-------------------

:synopsis: Creamos el método de instancia y los parámetros que tomará para realizar la modificación. Al tratarse de una modificación tomará todos los parámetros que tiene el Alta.


.. py:function:: funcion_actualizar_usuarios(var_nombre,var_apellido,var_dni,var_direccion,var_pais,var_ciudad,var_cp,var_telefono,var_email,tree)

   :param str var_nombre:  Cada parámetro iniciado con la palabra 'var' indica el campo y dato que el usuario ingresará mediante la interfaz gráfica. 
   
   :param str tree:  El parámetro 'tree' se encarga de ingresar los datos ingresados en el treeview de nuestra app. 


   **seleccion_usuario = tree.focus()**

   **usuarios_id = tree.item(seleccion_usuario)** # Asignamos variables en donde se almacena la fila seleccionada por el usuario en el treeview.

   **actualizar = Usuarios.update(nombre=var_nombre.get()).where(Usuarios.id == usuarios_id["text"])** # La variable *Actualizar* indica donde se ejecutará la modificación con los datos ingresados por el usuario donde realizó la selección del treeview.

   **actualizar.execute()** # Se ejecuta la modificación y se realiza el commit en nuestra Base de Datos

   **self.funcion_consulta_general(tree)** # Se actualiza el treeview
   
   **var_nombre.set("")** # Se limpian los campos de la interfaz.

ABMC (Consulta)
----------------

:synopsis: Creamos el método de instancia y los parámetros que tomará para realizar la modificación. El método se encargará de traer toda la información de la Base de datos e insertarlas en el treeview mediante un bucle *For*

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

.. automodule:: Modelo
   :members:
   :undoc-members:
   :show-inheritance:
