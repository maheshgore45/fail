#DFS for a graph
graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}
visited = set()
def dfs(visited, graph, node):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)
print("DFS for the graph is as follows")
dfs(visited, graph, '5')


print()

#BFS for a graph
graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

visited = []
queue = []

def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue :
        m = queue.pop(0)
        print(m, end=" ")

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

print("BFS for the graph is as follows")
bfs(visited, graph, '5')


print()

# Selection sort

def selectionSort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i] , arr[min_index] = arr[min_index], arr[i]

if __name__  == "__main__":

    print("Enter the no of elements ")
    n = int(input())
    arr = []

    print("Enter the elemnts ")
    for i in range(n):
        arr.append(int(input()))

    print("Before sorting")
    print(*arr)

    selectionSort(arr)

    print("After sorting")
    print(*arr)


#  N - Queen 

N = int(input("Enter th no of queen:-"))

board = [[0]*N for i in range(N)]

def isSafe(i,j):
    for p in range(N):
        if board[i][p] == 1 or board[p][j] == 1:
            return False

    for n in range(N):
        for m in range(N):
            if i+j == n+m or i-j == n-m:
                if board[n][m] == 1:
                    return False
    return True

def nqueen(no_of_queen):
    if no_of_queen == 0:
        return True

    for i in range(N):
        for j in range(N):
            if board[i][j] != 1 and isSafe(i,j):
                board[i][j] = 1
                if nqueen(no_of_queen-1) == True:
                    return True
                board[i][j] = 0
    return False

def printBoard(board):
    for i in board:
        for j in i:
            print(j, end=" ")
        print()

if nqueen(N):
    printBoard(board)
else:
    print("Can't place")



# PRIMS 
#   identical graph as the YouTube video: https://youtu.be/cplfcGZmX7I
#   tuple = (cost, n1, n2)


import heapq

graph = {
        'A': [(3, 'D', 'A'), (3, 'C', 'A'), (2, 'B', 'A')],
        'B': [(2, 'A', 'B'), (4, 'C', 'B'), (3, 'E', 'B')],
        'C': [(3, 'A', 'C'), (5, 'D', 'C'), (6, 'F', 'C'), (1, 'E', 'C'), (4, 'B', 'C')],
        'D': [(3, 'A', 'D'), (5, 'C', 'D'), (7, 'F', 'D')],
        'E': [(8, 'F', 'E'), (1, 'C', 'E'), (3, 'B', 'E')],
        'F': [(9, 'G', 'F'), (8, 'E', 'F'), (6, 'C', 'F'), (7, 'D', 'F')],
        'G': [(9, 'F', 'G')],
    }

def prims(graph, start='A'):
    unvisited = list(graph.keys())
    visited = []
    total_cost = 0
    MST = []

    unvisited.remove(start)
    visited.append(start)

    heap = graph[start]
    heapq.heapify(heap)

    while unvisited:
        (cost, n1, n2) = heapq.heappop(heap)
        new_node = None

        if n1 in unvisited and n2 in visited:
            new_node = n1
            MST.append((cost, n2, n1))
        elif n2 in unvisited and n1 in visited:
            new_node = n2
            MST.append((cost, n1, n2))

        if new_node != None:
            unvisited.remove(new_node)
            visited.append(new_node)
            total_cost += cost

            for node in graph[new_node]:
                heapq.heappush(heap, node)

    return MST, total_cost

def main():
    MST, total_cost = prims(graph, 'A')
    print(f'Minimum spanning tree: {MST}')
    print(f'Total cost: {total_cost}')

main()