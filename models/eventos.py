import json
from typing import List
#from eventos import Evento

class Evento:
    def __init__(self, id: int, nombre: str, artista: str, genero:str, id_ubicacion: int, 
                 hora_inicio: str, hora_fin: str, descripcion: str, imagen: str ):
        self.id = id
        self.nombre = nombre
        self.artista = artista
        self.genero = genero
        self.id_ubicacion = id_ubicacion
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        self.descripcion = descripcion
        self.imagen = imagen

    def to_json(self) :
        return {"id": self.id, "nombre": self.nombre, "artista": self.artista,
                "genero": self.genero, "id_ubicacion": self.id_ubicacion, "hora_inicio": self.hora_inicio,
                "hora_fin": self.hora_fin, "descripcion": self.descripcion, "imagen": self.imagen}
    
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
                evento["descripcion"], evento["imagen"])
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

# Ejemplo de uso:
data = json.load(open('data/eventos.json'))

# Mostrar el Índice de Eventos
indice_de_eventos(data)

# Búsqueda y filtrado de eventos
resultados = buscar_y_filtrar_eventos(data, genero="Folclore", ubicacion="Cafayate, Salta")
print("Resultados de búsqueda:")
for evento in resultados:
    print(f"Nombre: {evento['nombre']}")
    print(f"Artista: {evento['artista']}")
    print(f"Género: {evento['genero']}")
    print(f"Ubicación: {evento['ubicacion']}")
    print("-------------------------------------")