from customtkinter import *
from PIL import Image, ImageTk

principal = "#FF5733"         
titulo_color = "#F2F2F2"       
texto_color = "#D4D4D4"        
subtitulo_color = "#A0A7AC"    
borde_color = "#C4C4C4"       
contenedor_color = "#212E36" 
cuerpo_color = "#192229"       


class Vista_Detalles(CTkFrame):
    def __init__(self, parent, controlador):
        super().__init__(parent, fg_color=contenedor_color)
        self.parent = parent
        self.controlador = controlador

        #Posición que tendrá en la App
        self.pack(expand=True, fil="both", padx=2, pady=2)

        #Grid Layout
        self.rowconfigure((0,1,3,4,5,6), weight=1, uniform="a")
        self.columnconfigure(0, weight=1, uniform="a")
        self.columnconfigure(1, weight=5, uniform="a")

        #Widgets
        self.twitter_img = ImageTk.PhotoImage(Image.open("assets/twitter_image.png").resize((30, 30)))
        self.crear_widgets()
        self.posicion_widgets()

    #Creación de widgets
    def crear_widgets(self):
        #Frames
        #Frame desplegable en el que se mostrarán los detalles del evento
        self.detalles_frame = CTkScrollableFrame(self, fg_color=contenedor_color, scrollbar_button_color=cuerpo_color, scrollbar_button_hover_color=borde_color)
        self.interior_frame = CTkFrame(self.detalles_frame, height=300, fg_color=cuerpo_color)


        #Grid Layout
        self.interior_frame.rowconfigure((0,1,2,3,4,5,6), weight=1, uniform="a")
        self.interior_frame.columnconfigure((0,1,2,3,4), weight=1, uniform="a")

        #Botones
        self.boton_volver = CTkButton(self, text="Volver", 
                                     fg_color=cuerpo_color,
                                     border_color=contenedor_color,
                                     hover_color=borde_color,
                                     text_color= titulo_color,
                                        font=("Open Sans",20), 
                                        command=self.controlador.volver)
        self.boton_detalles = CTkButton(self, text="Detalles", 
                                     fg_color=cuerpo_color,
                                     border_color=contenedor_color,
                                     text_color= titulo_color,
                                        font=("Open Sans",20),
                                        state="disabled")
        self.boton_ubicacion = CTkButton(self, text="Ubicación", 
                                     fg_color=cuerpo_color,
                                     border_color=contenedor_color,
                                     hover_color=borde_color,
                                     text_color= titulo_color,
                                         font=("Open Sans",20),
                                         command=self.controlador.mostrar_seccion_ubicacion)
        self.boton_compartir = CTkButton(self.interior_frame, width=15, corner_radius=50, 
                                         fg_color="transparent", text="", hover_color=borde_color, 
                                         image=self.twitter_img)
        
        #Etiquetas
        self.detalles_etiqueta = CTkLabel(self, text="Detalles", 
                                          text_color=titulo_color,
                                          font=("Roboto", 30, "bold"))
        self.nombre_etiqueta = CTkLabel(self.interior_frame, 
                                        text=self.controlador.evento_seleccionado.nombre, 
                                        text_color= texto_color,
                                        font=("Roboto", 15))
        self.artista = CTkLabel(self.interior_frame, 
                                text=f"Artista: {self.controlador.evento_seleccionado.artista}",
                                text_color= texto_color,
                                font=("Roboto",15))
        self.imagen = CTkLabel(self.interior_frame, image=self.parent.imagenes[self.controlador.evento_seleccionado.id-1],text="")
        self.fecha_inicio = CTkLabel(self.interior_frame, 
                                     text=f"Desde: {self.controlador.evento_seleccionado.hora_inicio}",
                                     text_color= texto_color,
                                     font=("Roboto",15))
        self.fecha_fin = CTkLabel(self.interior_frame, 
                                  text=f"Hasta: {self.controlador.evento_seleccionado.hora_fin}",
                                  text_color= texto_color,
                                  font=("Roboto",15))
        self.descripbion_titulo = CTkLabel(self.interior_frame, text="Descripción", 
                                           text_color= titulo_color,
                                           font=("Roboto", 20))
        self.descripcion = CTkLabel(self.interior_frame, 
                                    text=self.controlador.evento_seleccionado.descripcion,
                                    text_color= texto_color,
                                    font=("Open Sans",15),wraplength=400,justify=LEFT)
        self.genero_titulo = CTkLabel(self.interior_frame, 
                                      text="Género",
                                       text_color= titulo_color,
                                         font=("Roboto", 20))
        self.genero = CTkLabel(self.interior_frame, 
                               text=self.controlador.evento_seleccionado.genero,
                               text_color= texto_color,
                               font=("Open Sans",13),)


    #Posición de widgets
    def posicion_widgets(self):
        self.detalles_frame.grid(row=1, column=1, rowspan=7, padx=5, pady=5, sticky="nsew")
        self.interior_frame.pack(expand=True, fill="x", padx=2, pady=2)

        self.boton_volver.grid(row=1, column=0, padx=5, pady=5)
        self.boton_detalles.grid(row=2, column=0, padx=5, pady=5)
        self.boton_ubicacion.grid(row=3, column=0, padx=5, pady=5)
        self.detalles_etiqueta.grid(row=0, column=1, padx=5, pady=5)
        self.nombre_etiqueta.grid(row=0, column=0, columnspan=2, sticky="w", padx=10, pady=5)
        self.artista.grid(row=1, column=2, columnspan=2, sticky="w", padx=5, pady=5)
        self.imagen.grid(row=1, column=0, rowspan=2, columnspan=2, sticky="w", padx=10, pady=5)
        self.fecha_inicio.grid(row=2, column=2, columnspan=2, sticky="nw", padx=5, pady=5)
        self.fecha_fin.grid(row=2, column=2, columnspan=2, sticky="sw", padx=5, pady=5)
        self.descripbion_titulo.grid(row=3, column=0, columnspan=2, sticky="w", padx=10, pady=5)
        self.descripcion.grid(row=4, column=0, columnspan=5, sticky="w", padx=10, pady=5)
        self.genero_titulo.grid(row=5, column=0, columnspan=2, sticky="w", padx=10, pady=5)
        self.genero.grid(row=6, column=0, columnspan=5, sticky="w", padx=10, pady=5)
        self.boton_compartir.grid(row=0, column=4, padx=5, pady=5)
