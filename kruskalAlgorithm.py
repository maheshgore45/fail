class UnionFind:
    def __init__(self, vertices):
        self.parent = {vertex: vertex for vertex in vertices}
        self.rank = {vertex: 0 for vertex in vertices}

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            elif self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1


def kruskal(graph):
    edges = []
    for u in graph:
        edges.extend(graph[u])
    edges.sort(key=lambda edge: edge.weight)

    tree = []
    uf = UnionFind(graph.keys())

    for edge in edges:
        if len(tree) == len(graph) - 1:
            break
        u, v, weight = edge.u, edge.v, edge.weight
        if uf.find(u) != uf.find(v):
            tree.append(edge)
            uf.union(u, v)

    return tree


class Edge:
    def __init__(self, u, v, weight):
        self.u = u
        self.v = v
        self.weight = weight


if __name__ == "__main__":
    graph = {}

    numVertices = int(input("Enter the number of vertices: "))
    numEdges = int(input("Enter the number of edges: "))

    print("Enter edges in the format 'source destination weight':")
    for _ in range(numEdges):
        source, destination, weight = input().split()
        weight = int(weight)

        if source not in graph:
            graph[source] = []
        if destination not in graph:
            graph[destination] = []
        graph[source].append(Edge(source, destination, weight))
        graph[destination].append(Edge(destination, source, weight))

    startVertex = input("Enter the starting vertex: ")

    mst = kruskal(graph)

    print("Minimal Spanning Tree:")
    for edge in mst:
        print(edge.u, "--", edge.v, "==", edge.weight)

    totalWeight = sum(edge.weight for edge in mst)
    print("Total Weight of Minimal Spanning Tree:", totalWeight)



#Enter the number of vertices: 4
#Enter the number of edges: 5
#Enter edges in the format 'source destination weight':
#A B 10
#A C 6
#A D 5
#B D 15
#C D 4
#Enter the starting vertex: A
