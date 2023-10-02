view Module
============

:synopsis: The module named *view* runs the graphical interface of our app. It consists of entry fields, buttons that perform CRUD operations through lambda functions, and the treeview that allows visualizing the information.

Initial Section: Tkinter and Model
----------------------------------

.. note::
   **from Modelo import Abmc** # Call the CRUD class and its respective methods.
.. note::
   **from tkinter import Menu**
.. note::
   **from tkinter import ttk**
.. note::
   **from tkinter import StringVar**
.. note::
   **from tkinter import Label**
.. note::
   **from tkinter import Entry**
.. note::
   **from tkinter import W**
.. note::
   **from tkinter import HORIZONTAL** 
.. note::
   **from tkinter import VERTICAL**
.. note::
   **from tkinter import Button**
.. note::
   **from tkinter import NS**
.. note::
   **from tkinter import EW**

Tkinter GUI Modeling
--------------------
.. note::
   Please check out the Tkinter documentation.

.. py:class:: VistaPoo

   .. py:method:: __init__(ventana_interfaz)

      :param  ventana_interfaz: It refers to the *main* and will be the variable that defines the main window of our app with all its elements.

   .. note:: 
      **main = ventana_interfaz**

      **objeto2_basedatos = Abmc()** # Object that refers to the CRUD operations of the Model Module

      **main.title("PyNotes")** # app name

      **main.config(bg="#FFF7DD")** # app color

      **var_id = StringVar()** # We specify the variables and data types they will receive. These are located behind the entries that the user sees. 


Tkinter Graphic Interface Modeling - Labels, Entrys, Treeview
-------------------------------------------------------------

.. note::
   Labels

**titulo = Label(main, text="Nombre")** 

**titulo.grid(row=1, column=0, sticky=W)** # We specify each of the Labels, their position in the interface, and the associated text


.. note::
   Entrys

**entry_nombre = Entry(main, textvariable=self.var_nombre, width=50)** 

**entry_nombre.grid(row=1, column=1)** # We specify the Entrys and their positions

.. note::
   Treeview

**tree = ttk.Treeview(main)** # We generate the Treeview.

**tree["columns"] = ("col1","col2","col3",)** # We specify how many columns the Treeview should have.

**tree.column("#0", width=20, minwidth=50, anchor=W)**

**tree.heading("#0", text="ID")**  # We assign the size of all columns followed by the accompanying text.

**tree.grid(column=0, row=12, columnspan=5)** # We determine the total size of the Treeview.


Tkinter Graphic Interface Modeling - Buttons and Lambda Function
----------------------------------------------------------------

:synopsis: The App contains 4 buttons that execute the CRUD operations through lambda functions referencing the object that contains the ABMC (CRUD) class and the respective method the user wants to run.

.. note::

   **boton_cliente = Button(main, text="CLIENTES", padx=73, pady=1, command=lambda: objeto2_basedatos.funcion_consulta_general(tree),)**

   **Main** # It refers to its position within the main window.

   **Text** # It indicates the name/text of the button.

   **padx - padxy** # Its location within the App.

   **Command = lambda: objeto2_basedatos.funcion_consulta_general(tree)** # It applies a lambda function where it references the object containing the ABMC (CRUD) and the specific method.



.. automodule:: view
   :undoc-members:
   :show-inheritance:
