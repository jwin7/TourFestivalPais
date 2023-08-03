from customtkinter import *
from tkinter.messagebox import *

class Controlador_Inicio:
    def __init__(self, app):
        self.app = app

    def mostrar_explorar(self):
        self.app.vista_inicio.destroy()
        self.app.mostrar_explorar()
        self.app.mostrar_eventos()

    def mi_perfil(self, id):
        self.app.seleccionar_usuario(id)
        self.app.mostrar_usuario()


    def salir(self):
        respuesta = askyesno("Confirmado", "¿Estas seguro que desea salír?")
        if respuesta:
            self.app.destroy()
