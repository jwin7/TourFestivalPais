from customtkinter import *

class Controlador_usuario:
    def __init__(self, app, usuario):
        self.app = app
        self.usuario = usuario

    def cerrar(self):
        self.app.vista_usuario.destroy()
        self.app.vista_usuario = None

    def quitar_boton_exit(asd):
        pass


