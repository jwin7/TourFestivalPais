import json

class Ubicacion:
    def __init__(self, id: int, nombre: str, direccion: str, latitud: float, longitud: float):
        self.id = id
        self.nombre = nombre  
        self.direccion = direccion
        self.latitud = latitud
        self.longitud = longitud

    def to_json(self):
        return {"id": self.id, "nombre": self.nombre, "direccion": self.direccion, "latitud": self.latitud, "longitud": self.longitud}

@classmethod
def cargar_de_json(cls, archivo_json):
    with open(archivo_json, "r") as f:
        data = json.load(f)

    ubicaciones = []
    for item in data:
        ubicacion = cls(id=item["id"], nombre=item["nombre"], direccion=item["direccion"], latitud=item["latitud"], longitud=item["longitud"])
        ubicaciones.append(ubicacion)

    return ubicaciones

