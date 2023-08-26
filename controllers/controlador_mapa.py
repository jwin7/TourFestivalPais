from customtkinter import *
import folium
import requests
import polyline

class Controlador_Mapa:
    def __init__(self, app, ubicacion_seleccionada):
        self.app = app
        self.ubicacion_seleccionada = ubicacion_seleccionada
        self.route = None

    def cargar_marcadores(self, mapa):
        imagen = self.app.imagenes[self.ubicacion_seleccionada.id-1]
        marcador = mapa.agregar_marcador(self.ubicacion_seleccionada, imagen)
        marcador.hide_image(True)

    #Al clickear el marcador genera la imagen del evento seleccionado
    def seleccionar_ubicacion(self,marcador):
        if marcador.image_hidden is True:
            marcador.hide_image(False)
        else:
            marcador.hide_image(True)
        print("Ubicación seleccionada: ", marcador.text)

    def cargar_marcadores(self, mapa):
        imagen = self.app.imagenes[self.ubicacion_seleccionada.id-1]
        marcador = mapa.agregar_marcador(self.ubicacion_seleccionada, imagen)
        marcador.hide_image(True)

    #Al clickear el marcador genera la imagen del evento seleccionado
    def seleccionar_ubicacion(self,marcador):
        if marcador.image_hidden is True:
            marcador.hide_image(False)
            print("Ubicación seleccionada: ", marcador.text)
        else:
            marcador.hide_image(True)


    def mostrar_seccion_detalles(self):
        self.app.vista_mapa.destroy()
        self.app.mostrar_detalles()
        self.app.mostrar_comentarios()

    def volver(self):
        self.app.vista_mapa.destroy()

        self.app.mostrar_explorar()
        self.app.mostrar_eventos()

    def quitar_ruta(self):
        self.app.vista_mapa.destroy()
        self.app.mostrar_ubicacion()

    #Recoge la latitud y longitud de los destinos elegidos y crea una ruta
    def planificar_ruta(self, destino_1, destino_2):
        self.app.vista_mapa.borrar_marcadores()     #Se borran los marcadores creados previamente
        for evento in self.app.eventos:
            if evento.nombre == destino_1:
                lat_a, lon_a = self.app.ubicaciones[evento.id-1].latitud, self.app.ubicaciones[evento.id-1].longitud
                self.app.vista_mapa.agregar_marcador(self.app.ubicaciones[evento.id-1], self.app.imagenes[evento.id-1])
                print("Destino 1: ",lat_a, lon_a)
            if evento.nombre == destino_2:
                lat_b, lon_b = self.app.ubicaciones[evento.id-1].latitud, self.app.ubicaciones[evento.id-1].longitud
                self.app.vista_mapa.agregar_marcador(self.app.ubicaciones[evento.id-1], self.app.imagenes[evento.id-1])
                print("Destino 2: ",lat_b, lon_b)
        try: 
            self.draw_map(lat_a, lon_a, lat_b, lon_b)
            self.app.vista_mapa.crear_ruta(self.route)
        except: 
            #En caso de no elegir un segundo destino al crear la ruta saldrá un error
            print("Se necesitan al menos 2 destinos para trazar una ruta.")


    def draw_map(self, lon_a, lat_a, lon_b, lat_b):

        route_data = get_route(lat_a, lon_a, lat_b, lon_b)
        self.route = route_data['route']

        if not route_data:
            print("No se pudo obtener los datos de la ruta.")
            return None

        map_instance = folium.Map(location=[lon_a, lat_a], zoom_start=15)

        folium.PolyLine(locations=route_data['route'], color="blue").add_to(map_instance)
        folium.Marker(location=[lon_a, lat_a], popup="Origin").add_to(map_instance)
        folium.Marker(location=[lon_b, lat_b], popup="Destination").add_to(map_instance)

        return map_instance



def get_route(pickup_lat, pickup_lon, dropoff_lat, dropoff_lon, url="https://router.project-osrm.org/route/v1/driving/"):

    location = f"{pickup_lat},{pickup_lon};{dropoff_lat},{dropoff_lon}"
    response = requests.get(url + location)

    if response.status_code != 200:
        print(f"Error en la solicitud con código de estado {response.status_code}")
        return None

    response_json = response.json()
    route = polyline.decode(response_json['routes'][0]['geometry'])
    start_point = [response_json['waypoints'][0]['location'][1], response_json['waypoints'][0]['location'][0]]
    end_point = [response_json['waypoints'][1]['location'][1], response_json['waypoints'][1]['location'][0]]
    distance = response_json['routes'][0]['distance']

    return {
        'route': route,
        'start_point': start_point,
        'end_point': end_point,
        'distance': distance
    }

