import json
from typing import List
#from eventos import Evento

class Evento:
    def __init__(self, id: int, nombre: str, artista: str, genero:str, ubicacion: int, #aqui cambie int por str
                 hora_inicio: str, hora_fin: str, descripcion: str, imagen: str ):
        self.id = id
        self.nombre = nombre
        self.artista = artista
        self.genero = genero
        self.ubicacion = ubicacion
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        self.descripcion = descripcion
        self.imagen = imagen

    def to_json(self) :
        return {"id": self.id, "nombre": self.nombre, "artista": self.artista,
                "genero": self.genero, "ubicacion": self.ubicacion, "hora_inicio": self.hora_inicio,
                "hora_fin": self.hora_fin, "descripcion": self.descripcion, "imagen": self.imagen}
    
    @classmethod
    def from_json(cls, json_data):
        data = json.loads(json_data)
        
        id = data["id"]
        nombre = data["nombre"]
        artista = data["artista"]
        genero = data["genero"]
        ubicacion = data["ubicacion"]
        hora_inicio = data["hora_inicio"]
        hora_fin = data["hora_fin"]
        descripcion = data["descripcion"]
        imagen = data["imagen"]
        
        return cls(id, nombre, artista, genero, ubicacion, hora_inicio, hora_fin, descripcion, imagen)

    @classmethod
    def cargar_de_json(cls, archivo):
        with open(archivo, 'r') as f:
            data = json.load(f)
            eventos = [cls(id=int(evento["id"]), nombre=evento["nombre"], artista=evento["artista"],
               genero=evento["genero"], ubicacion=evento["ubicacion"], hora_inicio=evento["hora_inicio"],
               hora_fin=evento["hora_fin"], descripcion=evento["descripcion"], imagen=evento["imagen"])
           for evento in data["eventos"]]



def obtener_historial_eventos(id_usuario: int, data: dict) -> List[Evento]:

    usuario = next((u for u in data["usuarios"] if u["id"] == id_usuario), None)
    if not usuario:
            print(f"No se encontró al usuario con ID {id_usuario}")
            return []

    
    historial_eventos = usuario["historial_eventos"]

    
    eventos = [e for e in data["eventos"] if e["id"] in historial_eventos]

    
    eventos_asistidos = []
    for evento in eventos:
        e = Evento(evento["id"], evento["nombre"], evento["artista"], evento["genero"],
                evento["ubicacion"], evento["hora_inicio"], evento["hora_fin"],
                evento["descripcion"], evento["imagen"])  # <-- El problema esta aqui.. estaba
        eventos_asistidos.append(e)
    return eventos_asistidos

def indice_de_eventos(data: dict):
    eventos = data["eventos"]
    
    print("Índice de Eventos:")
    for evento in eventos:
        print(f"ID: {evento['id']}")
        print(f"Nombre: {evento['nombre']}")
        print(f"Artista: {evento['artista']}")
        print(f"Género: {evento['genero']}")
        print(f"Ubicación: {evento['ubicacion']}")
        print("-------------------------------------")

def buscar_y_filtrar_eventos(data: dict, nombre=None, genero=None, ubicacion=None):
    eventos = data["eventos"]
    
    resultados = []
    for evento in eventos:
        # Filtrar por nombre, género y ubicación (si se proporcionan)
        if nombre and nombre.lower() not in evento["nombre"].lower():
            continue
        if genero and genero.lower() not in evento["genero"].lower():
            continue
        if ubicacion and ubicacion.lower() not in evento["ubicacion"].lower():
            continue
        
        resultados.append(evento)
    
    return resultados

@classmethod
def obtener_ubicacion(cls, direccion, ubicaciones):
    for ubicacion in ubicaciones:
        if ubicacion["direccion"] == direccion:
            return ubicacion["id"]
    return None

@classmethod
def cargar_de_json(cls, archivo):
    with open(archivo, 'r') as f:
        data = json.load(f)
        eventos = []
        ubicaciones = json.load(open("data/ubicacion.json"))

        for evento in data["eventos"]:
            ubicacion = cls.obtener_ubicacion(evento["ubicacion"], ubicaciones)
            if ubicacion is not None:
                evento["ubicacion"] = ubicacion
                eventos.append(cls(**evento))
            else:
                print(f"No se encontró la ubicación para el evento '{evento['nombre']}'")

    return eventos
# Ejemplo de uso:
#data = json.load(open('data/eventos.json'))

# Mostrar el Índice de Eventos
#indice_de_eventos(data)

# Búsqueda y filtrado de eventos
#resultados = buscar_y_filtrar_eventos(data, genero="Folclore", ubicacion="Cafayate, Salta")
#print("Resultados de búsqueda:")
#for evento in resultados:
    print(f"Nombre: {evento['nombre']}")
    print(f"Artista: {evento['artista']}")
    print(f"Género: {evento['genero']}")
    print(f"Ubicación: {evento['ubicacion']}")
    print("-------------------------------------")