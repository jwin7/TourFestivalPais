import json

class Ubicacion:
    def __init__(self, id: int, nombre: str, direccion: str, coordenadas: list[float]) :
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        self.coordenadas = coordenadas

    def to_json(self):
        return {"id": self.id, "nombre": self.nombre, "direccion": self.direccion, "coordenadas": self.coordenadas}

    @classmethod
    def from_json(cls, json_data):
        data = json.loads(json_data)
        
        id = data["id"]
        nombre = data["nombre"]
        direccion = data["direccion"]
        coordenadas = data["coordenadas"]
        
        return cls(id, nombre, direccion, coordenadas)
