import heapq

class PuzzleNode:
    def __init__(self, state, parent=None, action=None, cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost
        self.heuristic = self.calculate_heuristic()

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

    def is_goal(self):
        return self.state == tuple(range(16))

    def calculate_heuristic(self):
        return sum(1 for i, j in zip(self.state, range(16)) if i != j)

def get_neighbors(node):
    neighbors = []
    empty_index = node.state.index(0)

    moves = [(0, 1, "arriba"), (0, -1, "abajo"), (1, 0, "izquierda"), (-1, 0, "derecha")]

    for move in moves:
        new_empty_index = empty_index + move[0] + 4 * move[1]

        if 0 <= new_empty_index < 16:
            new_state = list(node.state)
            new_state[empty_index], new_state[new_empty_index] = new_state[new_empty_index], new_state[empty_index]
            neighbors.append(PuzzleNode(tuple(new_state), parent=node, action=move[2], cost=node.cost + 1))

    return neighbors

def a_star(initial_state):
    initial_node = PuzzleNode(initial_state)
    heap = [initial_node]
    heapq.heapify(heap)
    visited = set()

    while heap:
        current_node = heapq.heappop(heap)

        if current_node.is_goal():
            path = []
            while current_node:
                path.append((current_node.state, current_node.action))
                current_node = current_node.parent
            path.reverse()
            return path

        visited.add(current_node.state)

        neighbors = get_neighbors(current_node)
        for neighbor in neighbors:
            if neighbor.state not in visited:
                heapq.heappush(heap, neighbor)

    return None

initial_state = (1, 3, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0)
solution_path = a_star(initial_state)

if solution_path:
    print("Solución encontrada:")
    for step in solution_path:
        print(f"Estado: {step[0]}, Movimiento: {step[1]}")
else:
    print("No se encontró solución.")


