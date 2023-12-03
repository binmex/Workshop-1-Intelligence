# Importamos la librería random para generar trayectorias aleatorias
import random

# Definimos una función que recibe una red (representada como un diccionario de adyacencia), un nodo inicial y un nodo final
def museo_britanico(red, inicio, fin):
  # Inicializamos una lista vacía para almacenar las trayectorias posibles
  trayectorias = []
  # Inicializamos una variable para almacenar la mejor trayectoria encontrada
  mejor = None
  # Inicializamos una variable para almacenar la longitud de la mejor trayectoria encontrada
  longitud = float("inf")
  # Mientras no hayamos encontrado una trayectoria que llegue al nodo final
  while mejor is None:
    # Generamos una trayectoria aleatoria partiendo del nodo inicial
    trayectoria = [inicio]
    # Mientras la trayectoria no haya llegado al nodo final ni se haya quedado sin opciones
    while trayectoria[-1] != fin and len(red[trayectoria[-1]]) > 0:
      # Elegimos un nodo vecino al azar
      vecino = random.choice(red[trayectoria[-1]])
      # Si el nodo vecino no está en la trayectoria
      if vecino not in trayectoria:
        # Lo añadimos a la trayectoria
        trayectoria.append(vecino)
    # Si la trayectoria ha llegado al nodo final
    if trayectoria[-1] == fin:
      # Añadimos la trayectoria a la lista de trayectorias posibles
      trayectorias.append(trayectoria)
      # Si la longitud de la trayectoria es menor que la longitud de la mejor trayectoria encontrada
      if len(trayectoria) < longitud:
        # Actualizamos la mejor trayectoria y su longitud
        mejor = trayectoria
        longitud = len(trayectoria)
  # Devolvemos la mejor trayectoria y la lista de trayectorias posibles
  return mejor, trayectorias


red = {
    "A": ["B", "C", "D"],
    "B": ["A", "C", "E", "F"],
    "C": ["A", "B", "D", "E"],
    "D": ["A", "C", "E", "G"],
    "E": ["B", "C", "D", "F", "G"],
    "F": ["B", "E", "H"],
    "G": ["D", "E", "H"],
    "H": ["F", "G"]
}

inicio = "A"
fin = "H"

mejor, trayectorias = museo_britanico(red, inicio, fin)

print(f"La mejor trayectoria es: {mejor}")
#print(f"El número de trayectorias posibles es: {len(trayectorias)}")