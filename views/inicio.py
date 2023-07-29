import json
import tkinter as tk
from ..models.eventos import Evento

# Crear una ventana de Tkinter
root = tk.Tk()
root.title('Pantalla de Inicio')

# Crear un widget Listbox para mostrar la lista de eventos destacados
listbox = tk.Listbox(root)
listbox.pack()

# Leer los datos de eventos desde el archivo JSON
with open('data.json', 'r') as f:
    data = json.load(f)

# Crear instancias de la clase Evento a partir de los datos
eventos = [Evento.from_json(evento_data) for evento_data in data['eventos']]

# Seleccionar los eventos que deseas mostrar en la pantalla de inicio
eventos_destacados = eventos[:3]  # Los primeros 3 eventos

# Agregar los eventos destacados al widget Listbox
for evento in eventos_destacados:
    listbox.insert(tk.END, evento.nombre)

# Iniciar el bucle principal de Tkinter
root.mainloop()
