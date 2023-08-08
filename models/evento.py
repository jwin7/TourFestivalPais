import json

class Evento:
    def __init__(self,id: int, nombre: str, artista: str, 
                 genero: str, id_ubicacion: int, hora_inicio: str, 
                 hora_fin: str, descripcion: str, imagen: str ):
        """
        hora_inicio datetime ISO 8601
        hora_fin datetime ISO 8601
        imagen URL apuntar a un archivo en la carpeta assets
        """
        self.id = id
        self.nombre = nombre
        self.artista = artista
        self.genero = genero
        self.id_ubicacion = id_ubicacion
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        self.descripcion = descripcion
        self.imagen = imagen
        

    @classmethod
    def cargar_de_json(cls, archivo):
        with open(archivo, "r") as f:
            data = json.load(f)
        return [cls(**evento) for evento in data]
        
"""    def to_json(self):
        return {"id": self.id, "nombre": {self.nombre}, "artista": {self.artista}, "genero": {self.genero}, 
                "id_ubicacion": {self.id_ubicacion}, "hora_inicio": {self.hora_inicio}, "hora_fin": {self.hora_fin},
                "descripcion": {self.descripcion}, "imagen": {self.imagen}}


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

    @staticmethod
    def cargar_eventos(archivo_json):
        with open(archivo_json, "r") as archivo:
            datos = json.load(archivo)
        return [Evento.from_json(json.dumps(dato)) for dato in datos]"""
