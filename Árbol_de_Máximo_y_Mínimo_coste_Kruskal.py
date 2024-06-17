#Alma Paola Garcia Landeros
#21110038
#6E1
#Inteligencia Artificial
#Centro de Enseñanza Tecnica Industrial

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1
            return True
        return False

def kruskal_mst(graph):
    """
    Función para encontrar el Árbol de Mínimo y Máximo Coste usando el algoritmo de Kruskal.

    Args:
    - graph: Lista de tuplas (u, v, peso) representando las aristas del grafo ponderado.

    Returns:
    - mst_min: Lista de aristas que forman el Árbol de Mínimo Coste.
    - mst_max: Lista de aristas que forman el Árbol de Máximo Coste.
    """
    n = len(graph)
    mst_min = []
    mst_max = []
    
    # Ordena las aristas por peso
    graph.sort(key=lambda x: x[2])
    
    uf = UnionFind(n)
    
    for u, v, weight in graph:
        if uf.union(u, v):
            mst_min.append((u, v, weight))
            mst_max.append((u, v, weight))
        else:
            mst_max.pop()  # Elimina la última arista añadida en mst_max
    
        # Muestra paso a paso el progreso del algoritmo
        print_step_by_step(mst_min, mst_max, u, v, weight)
    
    return mst_min, mst_max

def print_step_by_step(mst_min, mst_max, u, v, weight):
    """
    Muestra paso a paso la construcción del Árbol de Mínimo y Máximo Coste.

    Args:
    - mst_min: Lista de aristas del Árbol de Mínimo Coste.
    - mst_max: Lista de aristas del Árbol de Máximo Coste.
    - u: Nodo u de la arista añadida.
    - v: Nodo v de la arista añadida.
    - weight: Peso de la arista añadida.
    """
    print(f"\nArista añadida: ({u}, {v}), Peso: {weight}")
    
    print("\nÁrbol de Mínimo Coste:")
    for edge in mst_min:
        print(f"Arista: ({edge[0]}, {edge[1]}), Peso: {edge[2]}")
    
    print("\nÁrbol de Máximo Coste:")
    for edge in mst_max:
        print(f"Arista: ({edge[0]}, {edge[1]}), Peso: {edge[2]}")


# Ejemplo de uso:
graph = [
    (0, 1, 10),
    (0, 2, 6),
    (0, 3, 5),
    (1, 3, 15),
    (2, 3, 4)
]

print("Simulador de Árbol de Máximo y Mínimo Coste Kruskal")
print("Aristas del grafo de ejemplo:")
for u, v, weight in graph:
    print(f"Arista: ({u}, {v}), Peso: {weight}")

print("\nCalculando Árbol de Máximo y Mínimo Coste Kruskal...")
mst_min, mst_max = kruskal_mst(graph)

print("\nÁrbol de Mínimo Coste:")
for edge in mst_min:
    print(f"Arista: ({edge[0]}, {edge[1]}), Peso: {edge[2]}")

print("\nÁrbol de Máximo Coste:")
for edge in mst_max:
    print(f"Arista: ({edge[0]}, {edge[1]}), Peso: {edge[2]}")
