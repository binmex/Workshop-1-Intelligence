import random

def museo_astar(red, inicio, fin):
    trayectorias = []
    mejor = None
    longitud = float("inf")

    while mejor is None:
        trayectoria = [inicio]
        while trayectoria[-1] != fin and len(red[trayectoria[-1]]) > 0:
            # Seleccionar el nodo vecino que minimiza la suma de la longitud actual y la estimación heurística
            vecino = min(red[trayectoria[-1]], key=lambda nodo: len(trayectoria) + estimacion_heuristica(nodo, fin))
            if vecino not in trayectoria:
                trayectoria.append(vecino)

        if trayectoria[-1] == fin:
            trayectorias.append(trayectoria)
            if len(trayectoria) < longitud:
                mejor = trayectoria
                longitud = len(trayectoria)

    return mejor, trayectorias

def estimacion_heuristica(nodo, objetivo):
    #la estimación heurística es la longitud mínima de la trayectoria desde el nodo hasta el objetivo
    return len(mejor_camino_entre_nodos(red, nodo, objetivo))

def mejor_camino_entre_nodos(red, inicio, fin):
    visitados = set()
    mejor_camino = []

    def dfs(actual, camino_actual):
        nonlocal mejor_camino
        if actual == fin:
            if not mejor_camino or len(camino_actual) < len(mejor_camino):
                mejor_camino = camino_actual.copy()
            return
        for vecino in red[actual]:
            if vecino not in visitados:
                visitados.add(vecino)
                dfs(vecino, camino_actual + [vecino])
                visitados.remove(vecino)

    dfs(inicio, [inicio])
    return mejor_camino

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
#Indicamos nodo de inicio y fin
inicio = "A"
fin = "H"

mejor, trayectorias = museo_astar(red, inicio, fin)

print(f"La mejor trayectoria es: {mejor}")
print(f"El número de trayectorias posibles es: {len(trayectorias)}")
