observer Module
==================

:synopsis: We apply the **observer pattern** just as a practical example. This way, we obtain responses when there are CRUD actions

Class *Sujeto*
--------------

.. py:class:: Sujeto 

   .. py:method:: agregar(self, obj)
         self.observadores.append(obj)
   .. py:method:: notificar(self, *args)
         for observador in self.observadores:
            observador.update(args)  # calls 'notificar' (notify) to indicates actions on the CRUD
      
   observadores = []  # Empty list to save observers

.. py:class:: Observador
   
   .. py:method::update(self):
      raise NotImplementedError("Delegación de actualización")

.. py:class:: ConcreteObserverA(Observador):
   
   .. py:method:: __init__(self, obj)
         self.observado_a = obj
         self.observado_a.agregar(self)
   .. py:method:: update(self, *args)
         print("Actualización dentro de ObservadorConcretoA")
         print("Parametros ingresados: ", args)


.. automodule:: observer
   :members:
   :undoc-members:
   :show-inheritance:
