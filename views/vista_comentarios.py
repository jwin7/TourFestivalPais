from customtkinter import *

principal = "#FF5733"         
titulo_color = "#F2F2F2"       
texto_color = "#D4D4D4"        
subtitulo_color = "#A0A7AC"    
borde_color = "#C4C4C4"       
contenedor_color = "#212E36" 
cuerpo_color = "#192229" 

class Vista_Comentarios(CTkFrame):
    def __init__(self, parent, controlador):
        super().__init__(parent, fg_color=contenedor_color)
        self.parent = parent
        self.controlador = controlador

        #Posición que tendrá en el frame desplegable en Vista Detalles
        self.pack(expand=True, fill="x", padx=2, pady=2)

        #Widgets
        self.crear_widgets()
        self.posicion_widgets()

        self.agregar_comentarios()

    def crear_widgets(self):
        #Frame en el que el usuario podrá escribir un comentario
        self.frame_enviar_comentario = CTkFrame(self, fg_color=cuerpo_color)
        #Grid Layout
        self.frame_enviar_comentario.rowconfigure((0,1,2,3), weight=1, uniform="a")
        self.frame_enviar_comentario.columnconfigure((0,1,2), weight=1, uniform="a")

        #Variable de contról
        self.nota_var = StringVar(value="5")
        self.nota_var.set("5")
        self.animo_var = StringVar(value="Positivo")
        self.animo_var.set("Positivo")

        #Option Menu
        self.nota_option = CTkOptionMenu(self.frame_enviar_comentario, values=["1", "2", "3", "4", "5"], variable=self.nota_var,fg_color=cuerpo_color, 
                                                button_color=contenedor_color,
                                                button_hover_color=borde_color,
                                                dropdown_fg_color=contenedor_color,
                                                dropdown_hover_color=borde_color,
                                                dropdown_text_color=titulo_color,
                                                text_color=titulo_color)
        self.animo_option = CTkOptionMenu(self.frame_enviar_comentario, values=["Positivo", "Negativo"], variable=self.animo_var,fg_color=cuerpo_color, 
                                                button_color=contenedor_color,
                                                button_hover_color=borde_color,
                                                dropdown_fg_color=contenedor_color,
                                                dropdown_hover_color=borde_color,
                                                dropdown_text_color=titulo_color,
                                                text_color=titulo_color)

        #Botones
        self.boton_enviar_comentario = CTkButton(self.frame_enviar_comentario,
                                                 fg_color=contenedor_color,
                                                 hover_color=borde_color,
                                                 text_color= titulo_color,
                                                 font=("Open Sans",15), 
                                                 text="Enviar", command=lambda: 
                                                 self.controlador.enviar_comentario(self.nota_var.get(), 
                                                                                    self.animo_var.get(),
                                                                                    self.entrada_comentario.get()))

        #Etiquetas
        self.comentarios_titulo = CTkLabel(self.frame_enviar_comentario, text="Deja un comentario", text_color=titulo_color, font=("Roboto", 15))
        self.nota_etiqueta = CTkLabel(self.frame_enviar_comentario, text="Nota", text_color=texto_color, font=("Roboto", 15))
        self.animo_etiqueta = CTkLabel(self.frame_enviar_comentario, text="Ánimo", text_color=texto_color, font=("Roboto", 15))

        #Entrada
        self.entrada_comentario = CTkEntry(self.frame_enviar_comentario, width=400, placeholder_text="Escribir comentario", text_color=texto_color, font=("Open Sans",15)) 

    def posicion_widgets(self):
        self.frame_enviar_comentario.pack(expand=True, fill="x", padx=2, pady=2)
        self.nota_option.grid(row=2, column=0, padx=5, pady=5)
        self.animo_option.grid(row=2, column=1, padx=5, pady=5)
        self.boton_enviar_comentario.grid(row=3, column=3, padx=5, pady=5)
        self.comentarios_titulo.grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.nota_etiqueta.grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.animo_etiqueta.grid(row=1, column=1, sticky="w", padx=5, pady=5)
        self.entrada_comentario.grid(row=3, column=0, columnspan=2, sticky="w", padx=5, pady=5)


    #Crea un frame que contenga un comentario
    def crear_vista_de_comentario(self, usuario, calificacion, animo, comentario, id):
        frame_comentario = CTkFrame(self, fg_color=cuerpo_color)
        frame_comentario.pack(expand=True, fill="x", padx=2, pady=2)

        #Grid Layout
        frame_comentario.rowconfigure((0,1,2), weight=1, uniform="a")
        frame_comentario.columnconfigure((0,1,2), weight=1, uniform="a")

        #Widgets
        #Botón
        boton_ver_perfil = CTkButton(frame_comentario, text="Ver Perfil", fg_color=cuerpo_color,
                                     hover_color=borde_color, text_color= titulo_color, font=("Open Sans", 15),
                                     command=lambda: self.controlador.ver_perfil(id))

        #Etiquetas
        comentario_usuario = CTkLabel(frame_comentario, text=usuario, text_color=titulo_color, font=("Open Sans", 15))
        comentario_calificacion = CTkLabel(frame_comentario, text=f"Nota: {calificacion}/5", text_color=texto_color, font=("Open Sans", 15))
        comentario_animo = CTkLabel(frame_comentario, text=animo, text_color=texto_color, font=("Open Sans", 15))
        comentario_comentario = CTkLabel(frame_comentario, text=comentario, text_color=texto_color, font=("Open Sans", 15))

        #Posición
        boton_ver_perfil.grid(row=2, column=2, sticky="e", padx=5, pady=5)
        comentario_usuario.grid(row=0, column=0, sticky="w", padx=5, pady=5)
        comentario_calificacion.grid(row=1, column=0, sticky="w", padx=5, pady=5)
        comentario_animo.grid(row=1, column=0, sticky="e", padx=5, pady=5)
        comentario_comentario.grid(row=2, column=0, columnspan=2, sticky="w", padx=5, pady=5)


    #Genera frames con los comentarios que tengan el mismo id del evento seleccionado
    #Asigna el usario al comentario que tenga el mismo id_usuario
    def agregar_comentarios(self):
        comentarios = self.controlador.app.comentarios
        usuarios = self.controlador.app.usuarios
        for comentario in comentarios:
            if comentario.id_evento == self.controlador.evento_seleccionado.id:
                for usuario in usuarios:
                    if usuario.id == comentario.id_usuario:
                        self.crear_vista_de_comentario(usuario.nombre, comentario.calificacion, comentario.animo, comentario.comentario, usuario.id)
