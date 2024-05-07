class GraphColoring:
    def __init__(self, vertices, graph):
        self.vertices = vertices
        self.graph = graph
        # Initialize colors for each vertex, initially set to -1
        self.colors = [-1] * self.vertices
        self.minColors = float('inf')


    def solve(self):
        self.try_coloring(0, 1)

    def try_coloring(self, vertex, num_colors):
        if num_colors >= self.minColors:
            return

        if vertex == self.vertices:
            self.minColors = num_colors
            self.print_solution(num_colors)
            return

        for color in range(1, num_colors + 1):
            if self.is_safe(vertex, color):
                self.colors[vertex] = color
                self.try_coloring(vertex + 1, num_colors)
                self.colors[vertex] = -1

        self.colors[vertex] = num_colors + 1
        self.try_coloring(vertex + 1, num_colors + 1)
        self.colors[vertex] = -1

    def is_safe(self, vertex, color):
        for i in range(self.vertices):
            if self.graph[vertex][i] == 1 and self.colors[i] == color:
                return False
        return True

    def print_solution(self, num_colors):
        print("Solution found with", num_colors, "colors:")
        for i in range(self.vertices):
            print("Vertex", i, "---> Color", self.colors[i])

if __name__ == "__main__":
    vertices = int(input("Enter the number of vertices: "))
    graph = []

    print("Enter the adjacency matrix:")
    for i in range(vertices):
        row = list(map(int, input().strip()))
        graph.append(row)

    coloring = GraphColoring(vertices, graph)
    coloring.solve()



#Enter the number of vertices: 4
#Enter the adjacency matrix:
#0111
#1010
#1101
#1010
