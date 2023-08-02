import tkinter as tk
import json
from models.review import Review
from models.usuario import Usuario

# Crear una ventana de Tkinter
root = tk.Tk()
root.title('Tour Festival Pais')

# Crear un widget Label para mostrar el nombre del usuario
nombre_label = tk.Label(root, text='Nombre:')
nombre_label.pack()

# Crear un widget Entry para permitir al usuario ingresar su nombre
nombre_entry = tk.Entry(root)
nombre_entry.pack()

# Crear un widget Canvas para mostrar el mapa
mapa_canvas = tk.Canvas(root, width=400, height=300)
mapa_canvas.pack()

# Crear un widget Listbox para mostrar la lista de destinos
destinos_listbox = tk.Listbox(root)
destinos_listbox.pack()

# Iniciar el bucle principal de Tkinter
root.mainloop()



# Cargar datos de los archivos JSON
data_reviews = json.load(open('data/review.json'))
data_usuarios = json.load(open('data/usuario.json'))

# Crear listas de objetos Review y Usuario
reviews = [Review.from_json(json.dumps(review_data)) for review_data in data_reviews["reviews"]]
usuarios = [Usuario.from_json(json.dumps(usuario_data)) for usuario_data in data_usuarios["usuarios"]]

# Función para obtener las reseñas y calificaciones de un evento
def obtener_resenas_y_calificaciones(id_evento):
    resenas_calificaciones = []
    for review in reviews:
        if review.id_evento == id_evento:
            usuario = next((usuario for usuario in usuarios if usuario.id == review.id_usuario), None)
            if usuario:
                resenas_calificaciones.append((usuario.nombre, review.calificacion, review.comentario, review.animo))
    return resenas_calificaciones

# Ejemplo de uso:
evento_id = 1
resenas_calificaciones_evento = obtener_resenas_y_calificaciones(evento_id)
for nombre_usuario, calificacion, comentario, animo in resenas_calificaciones_evento:
    print(f"Usuario: {nombre_usuario}")
    print(f"Calificación: {calificacion}")
    print(f"Comentario: {comentario}")
    print(f"Ánimo: {animo}")
    print("-------------------------------------")


