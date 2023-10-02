from tkinter import Tk
import view
import observer


class ControladorPoo:
    def __init__(self, root):
        self.root_controler = root
        self.objeto_vista = view.VistaPoo(self.root_controler)
        self.objeto_observador = observer.ConcreteObserverA(
            self.objeto_vista.objeto2_basedatos
        )


if __name__ == "__main__":
    main = Tk()
    application = ControladorPoo(main)
    main.mainloop()
