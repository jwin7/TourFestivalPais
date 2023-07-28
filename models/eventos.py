import json

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

    def to_json(self) :
        return {"id": self.id, "nombre": self.nombre, "artista": self.artista,
                "genero": self.genero, "id_ubicacion": self.id_ubicacion, "hora_inicio": self.hora_inicio,
                "hora_fin": self.hora_fin, "descripcion": self.descripcion, "imagen": self.imagen}
    
    @classmethod
    def from_json(cls, json_data):
        data = json.loads(json_data)
        
        id = data["id"]
        nombre = data["nombre"]
        artista = data["artista"]
        genero = data["genero"]
        id_ubicacion = data["id_ubicacion"]
        hora_inicio = data["hora_inicio"]
        hora_fin = data["hora_fin"]
        descripcion = data["descripcion"]
        imagen = data["imagen"]
        
        return cls(id, nombre, artista, genero, id_ubicacion, hora_inicio, hora_fin, descripcion, imagen)
