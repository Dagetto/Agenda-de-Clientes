from tkinter import Tk
import Vista


class ControladorPoo:
    def __init__(self, root):

        self.root_controler = root
        self.objeto_vista = Vista.ventana_interfaz(
            self.root_controler
        )

    if __name__ == "__main__":
        main = Tk()
        objeto1_controlador = Vista.VistaPoo(main)
        main.mainloop()
