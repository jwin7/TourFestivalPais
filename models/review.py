import json

class Review:
    def __init__(self, id: int, id_evento: int, id_usuario: int, calificacion: int, comentario: str, animo: str):
        """
        Calificacion int del 1 al 5
        animo str "Positivo" / "Negativo"
        """
        self.id = id
        self.id_evento = id_evento
        self.id_usuario = id_usuario
        self.calificacion = calificacion
        self.comentario = comentario
        self.animo = animo

    @classmethod
    def cargar_de_json(cls, archivo):
        with open(archivo, "r") as f:
            data = json.load(f)
        return [cls(**review) for review in data]
    
    @classmethod
    def añadir_comentario(cls, comentario):
        return cls(**comentario)
