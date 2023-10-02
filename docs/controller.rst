controller Module
==================

:synopsis: The controller module manages access to the User Agenda app. In its initial section, it imports the **tk** and the **view** module, followed by the ControladorPoo class.

Initial Section: Tk y view Module.
----------------------------------------
.. note::
   **from tkinter import Tk**
.. note::
   **import view** # It imports the module that runs our interface.
.. note::
   **import observer** 

Class *ControladorPoo*
-----------------------

.. py:class:: ControladorPoo

   .. py:method:: def __init__(self, root):
      self.root_controler = root
      self.objeto_vista = view.VistaPoo(self.root_controler)
      self.objeto_observador = observer.ConcreteObserverA(
         self.objeto_vista.objeto2_basedatos
      )

if __name__ == "__main__":
   main = Tk()
   application = ControladorPoo(main)
   main.mainloop()

.. automodule:: controller
   :members:
   :undoc-members:
   :show-inheritance:
