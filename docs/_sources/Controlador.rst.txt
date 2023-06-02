Módulo Controlador 
==================

:synopsis: El módulo Controlador gestiona el acceso a la app Agenda de Usuarios. En su sección inicial importa el **tk** y el modulo correspondiente a **Vista**, seguido de la Clase ControladorPoo.

Seccion inicial: Tk y Módulo Vista.
----------------------------------------
.. note::   
   **from tkinter import Tk**
.. note::
   **import Vista** # Importa el modulo que ejecuta nuestra interfaz

Clase *ControladorPoo*
-----------------------

El Módulo denominado Controlador cuenta con una Clase *ControladorPoo* y un método de instancia *def __init__(self, root)* definido en su interior que permite ejecutar nuestra app.

.. py:class:: ControladorPoo

   .. py:method:: def __init__(self, root):
      self.root_controler = root
      self.objeto_vista = Vista.ventana_interfaz(
      self.root_controler
      )
      if __name__ == "__main__":
        main = Tk()
        objeto1_controlador = Vista.VistaPoo(main)
        main.mainloop()

.. automodule:: Controlador
   :members:
   :undoc-members:
   :show-inheritance:
