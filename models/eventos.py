class Evento:
    def __init__(self, id: int, nombre: str, artista: str, genero:str, id_ubicacion: int, 
                 hora_inicio: str, hora_fin: str, descripcion: str, imagen: str ):
        self.id = id
        self.nombre = nombre
        self.artista = artista
        self.genero = genero
        self.id_ubicacion = id_ubicacion
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        self.descripcion = descripcion
        self.imagen = imagen

    def to_jsaon(self) :
        pass

    @classmethod    
    def from_jsaon(self) :   
        pass
        