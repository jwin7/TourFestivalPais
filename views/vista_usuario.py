from customtkinter import *

principal = "#FF5733"         
titulo_color = "#F2F2F2"       
texto_color = "#D4D4D4"        
subtitulo_color = "#A0A7AC"    
borde_color = "#C4C4C4"       
contenedor_color = "#212E36" 
cuerpo_color = "#192229" 



class Vista_Usuario(CTkToplevel):
    def __init__(self, parent, controlador):
        super().__init__(parent)
        self.parent = parent
        self.controlador = controlador

        self.title("Detalles de Usuario")
        self.geometry("600x400+400+100")


        self.frame = CTkFrame(self,fg_color=contenedor_color)
        self.frame.pack(expand=True, fill="both")

        self.protocol("WM_DELETE_WINDOW", self.controlador.quitar_boton_exit)

        #Grid Layout
        self.frame.rowconfigure((0,1,2,3), weight=1, uniform="a")
        self.frame.rowconfigure((4), weight=3, uniform="a")
        self.frame.columnconfigure((0,1,2,3), weight=1, uniform="a")

        #Widgets
        self.crear_widgets()
        self.posicion_widgets()
        self.mostrar_historial()

    def crear_widgets(self):
        #Frame en el que se mostrar la lista con eventos asistidos
        self.frame_historial = CTkScrollableFrame(self.frame, fg_color=cuerpo_color)

        #Etiquetas
        self.usuario_etiqueta = CTkLabel(self.frame, text="Detalles de Usuario", font=("Roboto", 30, "bold"),text_color=titulo_color)
        self.nombre_etiqueta = CTkLabel(self.frame, text=f"Nombre: {self.controlador.usuario.nombre}", font=("Roboto",20),text_color=titulo_color)
        self.apellido_etiqueta = CTkLabel(self.frame, text=f"Apellido: {self.controlador.usuario.apellido}", font=("Roboto",20),text_color=titulo_color)
        self.eventos_asistidos_etiqueta = CTkLabel(self.frame, text="Eventos asistidos:", font=("Roboto",20),text_color=titulo_color)

        #Botones
        self.boton_cerrar = CTkButton(self.frame, width=100, text="Cerrar", font=("Open Sans",15),fg_color=cuerpo_color, border_color=contenedor_color, text_color= titulo_color, command=self.controlador.cerrar)

    def posicion_widgets(self):
        self.frame_historial.grid(row=4, column=1, columnspan=3, sticky="nsew", padx=10, pady=5)
        self.usuario_etiqueta.grid(row=0, column=1, sticky="w", columnspan=4)
        self.nombre_etiqueta.grid(row=1, column=1, columnspan=2, sticky="w", padx=10, pady=5)
        self.apellido_etiqueta.grid(row=2, column=1, columnspan=2, sticky="w", padx=10, pady=5)
        self.eventos_asistidos_etiqueta.grid(row=3, column=1, columnspan=2, sticky="w", padx=10, pady=5)
        self.boton_cerrar.grid(row=0, column=0, sticky="w", padx=10, pady=5)


    def crear_vista_historial(self, nombre):
        nombre_de_evento = CTkLabel(self.frame_historial, text=nombre,text_color=texto_color)
        nombre_de_evento.pack()


    def mostrar_historial(self):
        eventos_asistidos = []
        for evento in self.parent.eventos:
            if evento.id in self.controlador.usuario.historial_eventos:
                eventos_asistidos.append(evento)
                self.crear_vista_historial(evento.nombre)
        if eventos_asistidos == []:
            self.etiqueta = CTkLabel(self.frame_historial, text="Aún no se asistió a ningún evento",text_color=texto_color)
            self.etiqueta.pack()
