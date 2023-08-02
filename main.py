from customtkinter import *
from PIL import Image, ImageTk
from models.evento import Evento
from views.vista_inicio import Vista_Inicio
from views.vista_login import Vista_Login
from views.vista_explorar import Vista_Explorar
from views.vista_eventos import Vista_Eventos
from views.vista_detalles import Vista_Detalles
from views.vista_comentarios import Vista_Comentarios
from views.vista_mapa import Vista_Mapa
from views.vista_usuario import Vista_Usuario
from controllers.controlador_inicio import Controlador_Inicio
from controllers.controlador_login import Controlador_login 
from controllers.controlador_explorar import Controlador_Explorar
from controllers.controlador_eventos import Controlador_Eventos
from controllers.controlador_detalles import Controlador_Detalles
from controllers.controlador_mapa import Controlador_Mapa
from controllers.controlador_usuario import Controlador_usuario
from models.ubicacion import Ubicacion
from models.review import Review
from models.usuario import Usuario

set_appearance_mode("dark")

class App(CTk):
    def __init__(self, imagenes=[]):
        super().__init__()
        #Setup principal
        self.title("App Tour Festival Pais")
        self.geometry("700x500+500+200")
        self.minsize(600,400)
        self.maxsize(800,600)

        #Se cargan los eventos y las ubicaciones
        self.eventos = Evento.cargar_de_json("data/evento.json")
        self.ubicaciones = Ubicacion.cargar_de_json("data/ubicacion.json")
        self.comentarios = Review.cargar_de_json("data/review.json")
        self.usuarios = Usuario.cargar_de_json("data/usuario.json")
        self.imagenes = imagenes

        #Inicializar
        self.inicializar()
        self.cargar_imagenes()

        #Run 
        self.mainloop()

    def inicializar(self):
        #Se cargan los controladores y se les asigna la lista de eventos
        self.controlador_inicio = Controlador_Inicio(self)
        self.controlador_login = Controlador_login(self)
        self.controlador_explorar = Controlador_Explorar(self)
        self.Controlador_eventos = Controlador_Eventos(self, self.eventos)
        self.controlador_detalles = None
        self.controlador_mapa = None
        self.controlador_usuario = None
        self.vista_usuario = None

        #Se muestra la pantalla inicial
        self.mostrar_login()


    #Añade las imagenes a la lista
    def cargar_imagenes(self):
        for evento in self.eventos:
            imagen = ImageTk.PhotoImage(Image.open(f"assets/{evento.imagen}").resize((200, 200)))
            self.imagenes.append(imagen)

    def cargar_fondo(self, fondo):
        return CTkImage(Image.open(f"assets/{fondo}"), size=(700, 500))

    #Mostrar vistas
    def mostrar_inicio(self):
        self.vista_inicio = Vista_Inicio(self, self.controlador_inicio)

    def mostrar_login(self):
        self.vista_login = Vista_Login(self, self.controlador_login)

    def mostrar_explorar(self):
        self.vista_explorar = Vista_Explorar(self, self.controlador_explorar)

    def mostrar_eventos(self):
        self.vista_eventos = Vista_Eventos(self.vista_explorar, self.Controlador_eventos)
        self.vista_eventos.agregar_eventos()

    def mostrar_eventos_filtrados(self):
        self.vista_eventos = Vista_Eventos(self.vista_explorar, self.Controlador_eventos)

    def mostrar_detalles(self):
        self.vista_detalles = Vista_Detalles(self, self.controlador_detalles)

    def mostrar_comentarios(self):
        self.vista_comentarios = Vista_Comentarios(self.vista_detalles.detalles_frame, self.controlador_detalles)

    def mostrar_ubicacion(self):
        self.vista_mapa = Vista_Mapa(self, self.controlador_mapa)

    def mostrar_usuario(self):
        if self.vista_usuario is None:
            self.vista_usuario = Vista_Usuario(self, self.controlador_usuario)  # Si es None crea la ventana
        else:
            self.vista_usuario.focus()

    def seleccionar_evento(self, id):
        for ubicacion, evento in zip(self.ubicaciones, self.eventos):
            if ubicacion.id and evento.id == id:
               self.ubicacion_seleccionada = ubicacion
               self.evento_seleccionado = evento
               self.controlador_detalles = Controlador_Detalles(self, evento)
               self.controlador_mapa = Controlador_Mapa(self, ubicacion)
               
               print(f"ID del evento seleccionado {id}")
               print(self.eventos[id-1].nombre)

    def seleccionar_usuario(self,id):
        for usuario in self.usuarios:
            if usuario.id == id:
                print(usuario.nombre)
                self.controlador_usuario = Controlador_usuario(self, usuario)
                





App()
