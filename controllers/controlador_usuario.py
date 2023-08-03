from customtkinter import *

class Controlador_usuario:
    def __init__(self, app, usuario):
        self.app = app
        self.usuario = usuario

    def cerrar(self):
        self.app.vista_usuario.destroy()
