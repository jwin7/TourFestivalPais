import json

class Usuario:
    def __init__(self, id, nombre, apellido, historial_eventos):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.historial_eventos = historial_eventos

    def to_json(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "historial_eventos": self.historial_eventos
        }

    @classmethod
    def from_json(cls, json_data):
        data = json.loads(json_data)
        return cls(
            data["id"],
            data["nombre"],
            data["apellido"],
            data["historial_eventos"]
        )
