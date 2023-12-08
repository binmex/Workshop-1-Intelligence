import random
def museo_britanico(red, inicio, fin):
  trayectorias = []
  # variable de mejor trayectoria
  mejor = None
  longitud = float("inf")
  while mejor is None:
    trayectoria = [inicio]
    while trayectoria[-1] != fin and len(red[trayectoria[-1]]) > 0:
      vecino = random.choice(red[trayectoria[-1]])
      if vecino not in trayectoria:
        trayectoria.append(vecino)
    if trayectoria[-1] == fin:
      # Añadimos la trayectoria a la lista de trayectorias posibles
      trayectorias.append(trayectoria)
      # Si la longitud de la trayectoria es menor que la longitud de la mejor trayectoria encontrada
      if len(trayectoria) < longitud:
        # Actualizamos la mejor trayectoria y su longitud
        mejor = trayectoria
        longitud = len(trayectoria)
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
#indicamos nodos de Inicio y fin
inicio = "A"
fin = "H"

mejor, trayectorias = museo_britanico(red, inicio, fin)

print(f"La mejor trayectoria es: {mejor}")
#print(f"El número de trayectorias posibles es: {len(trayectorias)}")