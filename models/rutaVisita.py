import json

class RutaVisita:
    def __init__(self, id:int, nombre: str, destino: list[int]) :
        self.id = id
        self.nombre = nombre
        self.destino = destino

    def to_json(self):
        return {"id": self.id, "nombre": self.nombre, "destino": self.destino}

    @classmethod
    def from_json(cls, json_data):
        data = json.loads(json_data)
        
        id = data["id"]
        nombre = data["nombre"]
        destino = data["destino"]
        
        return cls(id, nombre, destino)
