from customtkinter import *
from tkintermapview import TkinterMapView
from PIL import Image, ImageTk

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
        self.rowconfigure((0,1,2,3), weight=1, uniform="a")
        self.rowconfigure((4), weight=3, uniform="a")
        self.columnconfigure(0, weight=1, uniform="a")
        self.columnconfigure(1, weight=5, uniform="a")

        #Widgets
        self.crear_widgets()
        self.posicion_widgets()
        self.controlador.cargar_marcadores(self)

    def crear_widgets(self):
        #Frame que contendrá la sección de ubicación
        self.frame_desplegable = CTkScrollableFrame(self, fg_color=contenedor_color, scrollbar_button_color=cuerpo_color, scrollbar_button_hover_color=borde_color)
        #Frame que mostrará la ubicación del evento en el mapa
        self.mapa_frame = CTkFrame(self.frame_desplegable)
        #Frames interiores
        self.frame_interior_1 = CTkFrame(self.frame_desplegable, fg_color=contenedor_color)
        self.frame_interior_2 = CTkFrame(self.frame_desplegable, fg_color=cuerpo_color)
        self.frame_interior_3 = CTkFrame(self.frame_desplegable, fg_color=cuerpo_color)
        #Grid Layouts
        self.frame_interior_2.rowconfigure((0,1), weight=1, uniform="a")
        self.frame_interior_2.columnconfigure((0,1,2), weight=1, uniform="a")
        self.frame_interior_3.rowconfigure((0,1,2), weight=1, uniform="a")
        self.frame_interior_3.columnconfigure((0,1,2,3), weight=1, uniform="a")

        #Mapa
        self.mapa = TkinterMapView(self.mapa_frame, corner_radius=0, height=400)

        #Botones
        self.boton_volver = CTkButton(self, text="Volver",
                                      border_width=2,
                                      fg_color=cuerpo_color,
                                      border_color= borde_color,
                                      hover_color=borde_color,
                                      text_color= titulo_color,
                                      font=("Open Sans",20),
                                      command=self.controlador.volver)
        self.boton_detalles = CTkButton(self, text="Detalles", 
                                        border_width=2,
                                        fg_color=cuerpo_color,
                                        border_color= borde_color,
                                        hover_color=borde_color,
                                        text_color= titulo_color,
                                        font=("Open Sans",20),
                                        command=self.controlador.mostrar_seccion_detalles)
        self.boton_ubicacion = CTkButton(self, text="Ubicación",
                                         border_width=2,
                                         fg_color=cuerpo_color,
                                         border_color= borde_color,
                                         text_color= titulo_color,
                                         font=("Open Sans",20),
                                         state="disabled")
        self.boton_planificar_ruta = CTkButton(self.frame_interior_3, text="Crear ruta",
                                               border_width=2,
                                               fg_color=cuerpo_color,
                                               border_color= borde_color,
                                               text_color= titulo_color,
                                               font=("Open Sans",20),
                                               command=lambda: self.controlador.planificar_ruta(self.destino_1_var.get(),
                                                                                                self.destino_2_var.get()))
        self.boton_quitar_ruta = CTkButton(self.frame_interior_3, text="Quitar ruta",
                                           border_width=2,
                                           fg_color=cuerpo_color,
                                           border_color= borde_color,
                                           text_color= titulo_color,
                                           font=("Open Sans",20),
                                           command=self.controlador.quitar_ruta)

        #Etiquetas
        self.ubicacion_etiqueta = CTkLabel(self.frame_interior_1, text="Ubicación en el mapa",
                                           text_color= titulo_color,
                                           font=("Roboto", 30, "bold"))
        self.planificar_etiqueta = CTkLabel(self.frame_interior_2, text="Planificar Ruta",
                                            text_color=titulo_color, font=("Roboto", 20))
        self.planificar_descripcion_etiqueta = CTkLabel(self.frame_interior_2, text="Aquí puedes crear una ruta que podrás usar para asistir a multiples eventos!",
                                                        text_color=texto_color, font=("Open Sans",15))
        self.destinos_etiqueta = CTkLabel(self.frame_interior_3, text="Primero elige los destinos que quieras incluír en tu ruta.",
                                          text_color=texto_color, font=("Open Sans",15))
        self.destino_1_etiqueta = CTkLabel(self.frame_interior_3, text="Destino 1: ",
                                           text_color=texto_color, font=("Open Sans",15))
        self.destino_2_etiqueta = CTkLabel(self.frame_interior_3, text="Destino 2: ",
                                           text_color=texto_color, font=("Open Sans",15))

        #Variable de contról
        self.destino_1_var = StringVar(value=self.parent.eventos[self.controlador.ubicacion_seleccionada.id-1].nombre) #Usa el nombre del evento seleccionado como valor predeterminado
        self.destino_2_var = StringVar(value="Destino 2")
        
        #Option_Menu
        self.option_destino_1 = CTkOptionMenu(self.frame_interior_3, values=[(evento.nombre) for evento in self.parent.eventos],
                                              variable=self.destino_1_var,
                                                fg_color=cuerpo_color, 
                                                button_color=contenedor_color,
                                                button_hover_color=borde_color,
                                                dropdown_fg_color=contenedor_color,
                                                dropdown_hover_color=borde_color,
                                                dropdown_text_color=titulo_color,
                                                text_color=titulo_color)
        self.option_destino_2 = CTkOptionMenu(self.frame_interior_3, values=[(evento.nombre) for evento in self.parent.eventos],
                                              variable=self.destino_2_var,
                                                fg_color=cuerpo_color, 
                                                button_color=contenedor_color,
                                                button_hover_color=borde_color,
                                                dropdown_fg_color=contenedor_color,
                                                dropdown_hover_color=borde_color,
                                                dropdown_text_color=titulo_color,
                                                text_color=titulo_color)

    def posicion_widgets(self):
        self.frame_desplegable.grid(row=0, column=1, rowspan=5, sticky="nsew", padx=5, pady=5)
        self.frame_interior_1.pack(expand=True, fill="x", padx=5, pady=5)
        self.mapa_frame.pack(expand=True, fill="x", padx=5, pady=5)
        self.frame_interior_2.pack(expand=True, fill="x", padx=5, pady=5)
        self.frame_interior_3.pack(expand=True, fill="x", padx=5, pady=5)
        
        self.mapa.pack(expand=True, fill="both")

        self.ubicacion_etiqueta.grid(row=0, column=0, padx=5, pady=5)
        self.planificar_etiqueta.grid(row=0, column=0, sticky="w", padx=10, pady=5)
        self.planificar_descripcion_etiqueta.grid(row=1, column=0, columnspan=3, sticky="w", padx=10, pady=5)
        self.destinos_etiqueta.grid(row=0, column=0, columnspan=4, sticky="w", padx=10, pady=5)
        self.destino_1_etiqueta.grid(row=1, column=0, sticky="w", padx=10, pady=5)
        self.destino_2_etiqueta.grid(row=2, column=0, sticky="w", padx=10, pady=5)

        self.boton_volver.grid(row=1, column=0, padx=5, pady=5)
        self.boton_detalles.grid(row=2, column=0, padx=5, pady=5)
        self.boton_ubicacion.grid(row=3, column=0, padx=5, pady=5)
        self.boton_planificar_ruta.grid(row=1, column=3, padx=10, pady=5)
        self.boton_quitar_ruta.grid(row=2, column=3, padx=10, pady=5)

        self.option_destino_1.grid(row=1, column=1, sticky="w", padx=5, pady=5)
        self.option_destino_2.grid(row=2, column=1, sticky="w", padx=5, pady=5)



    #Coloca un marcador en la ubicación del evento seleccionado
    def agregar_marcador(self, ubicacion, imagen):
        self.mapa.set_position(ubicacion.latitud+0.001, ubicacion.longitud)
        marcador = self.mapa.set_marker(ubicacion.latitud, ubicacion.longitud, 
                                        text=ubicacion.direccion, image=imagen,
                                        command=self.controlador.seleccionar_ubicacion)
        return marcador
    
    def borrar_marcadores(self):
        self.mapa.delete_all_marker()

    def crear_ruta(self, ruta):
        self.mapa.delete_all_path() #Se borra la ruta creada antes de crear una nueva
        self.mapa.set_path(ruta)
    
