import json

class Usuario:
    def __init__(self,id: int, nombre: str, apellido: str, historial_eventos: list[int]):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.historial_eventos = historial_eventos


    @classmethod
    def cargar_de_json(cls, archivo):
        with open(archivo, "r") as f:
            data = json.load(f)
        return [cls(**usuario) for usuario in data]
    
    @classmethod
    def añadir_usuario(cls, usuario):
        return cls(**usuario)
