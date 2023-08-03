from customtkinter import *

class Controlador_Explorar:
    def __init__(self, app):
        self.app = app

    def volver(self):
        self.app.vista_explorar.destroy()
        self.app.mostrar_inicio()


    def filtrar(self, filtro, valor):
        eventos_filtrados = []
        if filtro == "Artista":
            for evento in self.app.eventos:
                if evento.artista == valor:
                    eventos_filtrados.append(evento)
                    print(eventos_filtrados)
        else:
            for evento in self.app.eventos:
                if valor in evento.genero:
                    eventos_filtrados.append(evento)
                    print(eventos_filtrados)
        self.app.vista_eventos.destroy()
        self.app.mostrar_eventos_filtrados()
        self.app.vista_eventos.agregar_eventos(eventos_filtrados)

    def quitar_filtro(self):
        self.app.vista_eventos.destroy()
        self.app.mostrar_eventos()
