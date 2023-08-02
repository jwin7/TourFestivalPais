from customtkinter import *
from tkintermapview import TkinterMapView

principal = "#52A5E0"
titulo_color = "#EFF3F5"        #Se suele usar para los titulos y el texto en los botones
texto_color = "#C8CDD0"         #Para los parrafos de texto
subtitulo_color = "#A0A7AC"     #Para los subtitulos
borde_color = "#2A3B47"         #Para el borde de los widgets y para el color del hover
contenedor_color = "#212E36"    #Para el color del frame principal
cuerpo_color = "#192229"        #Para los frames secundarios

class Vista_Mapa(CTkFrame):
    def __init__(self, parent, controlador):
        super().__init__(parent, fg_color= contenedor_color, border_color=borde_color)
        self.parent = parent
        self.controlador = controlador

        #Posición que tendrá en la App
        self.pack(expand=True, fill="both")

        #Grid Layout
        self.rowconfigure((0,1,3,4,5,6), weight=1, uniform="a")
        self.columnconfigure(0, weight=1, uniform="a")
        self.columnconfigure(1, weight=5, uniform="a")

        #Widgets
        self.crear_widgets()
        self.posicion_widgets()

        self.agregar_marcador()

    def crear_widgets(self):
        #Frame que mostrará la ubicación del evento en el mapa
        self.mapa_frame = CTkFrame(self)

        #Mapa
        self.mapa = TkinterMapView(self.mapa_frame, corner_radius=0)

        #Botones
        self.boton_volver = CTkButton(self, text="Volver",
                                      fg_color=cuerpo_color,
                                      border_color= contenedor_color,
                                      hover_color=borde_color,
                                      text_color= titulo_color,
                                      font=("Open Sans",20),
                                      command=self.controlador.volver)
        self.boton_detalles = CTkButton(self, text="Detalles", 
                                        fg_color=cuerpo_color,
                                        border_color= contenedor_color,
                                        hover_color=borde_color,
                                        text_color= titulo_color,
                                        font=("Open Sans",20),
                                        command=self.controlador.mostrar_seccion_detalles)
        self.boton_ubicacion = CTkButton(self, text="Ubicación",
                                         fg_color=cuerpo_color,
                                         border_color= contenedor_color,
                                         text_color= titulo_color,
                                         font=("Open Sans",20),
                                         state="disabled")

        #Etiquetas
        self.ubicacion_etiqueta = CTkLabel(self, text="Ubicación en el mapa",
                                           text_color= titulo_color,
                                           font=("Roboto", 30, "bold"))


    def posicion_widgets(self):
        self.mapa_frame.grid(row=1, column=1, rowspan=5, sticky="nsew", padx=5, pady=5)
        
        self.mapa.pack(expand=True, fill="both")

        self.ubicacion_etiqueta.grid(row=0, column=1)

        self.boton_volver.grid(row=1, column=0, padx=5, pady=5)
        self.boton_detalles.grid(row=2, column=0, padx=5, pady=5)
        self.boton_ubicacion.grid(row=3, column=0, padx=5, pady=5)


    #Coloca un marcador en la ubicación del evento seleccionado
    def agregar_marcador(self):
        ubicacion_seleccionada = self.controlador.ubicacion_seleccionada
        self.mapa.set_position(ubicacion_seleccionada.latitud, ubicacion_seleccionada.longitud)
        self.mapa.set_marker(ubicacion_seleccionada.latitud, ubicacion_seleccionada.longitud)
        print(ubicacion_seleccionada.latitud, ubicacion_seleccionada.longitud)
