import tkinter as tk

# Crear una ventana de Tkinter
root = tk.Tk()
root.title('Mi Aplicación')

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

