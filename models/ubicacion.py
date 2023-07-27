class Ubicacion:
    def __init__(self, id: int, nombre: str, direccion: str, coordenadas: list[float]) :
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        self.coordenadas = coordenadas

    def to_jsaon(self) :
        pass

    @classmethod    
    def from_jsaon(self) :   
        pass    