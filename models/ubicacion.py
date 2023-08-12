import json

class Ubicacion:
    def __init__(self, id: int, direccion: str, 
                 latitud: float, longitud: float ):
        
        self.id = id
        self.direccion = direccion
        self.latitud = latitud
        self.longitud = longitud

    @classmethod
    def cargar_de_json(cls, archivo):
        with open(archivo, "r") as f:
            data = json.load(f)
        return [cls(**ubicacion) for ubicacion in data]


#ubicaciones = Ubicacion.cargar_de_json("data/ubicacion.json")

#for ubicacion in ubicaciones:
    #print(ubicacion.direccion)
    #print(ubicacion.latitud)
    #print(ubicacion.longitud)
    #print(ubicacion.id)
    #print("")


