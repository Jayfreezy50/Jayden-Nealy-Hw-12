#Jayden
class Graph:
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.adj_matrix = [[0] * num_nodes for _ in range(num_nodes)]

    def addEdge(self, u, v):
        if 0 <= u < self.num_nodes and 0 <= v < self.num_nodes:
            self.adj_matrix[u][v] = 1
            self.adj_matrix[v][u] = 1
        else:
            print(f"Invalid edge ({u}, {v}). Nodes must be in range 0-{self.num_nodes - 1}.")

    def deleteNode(self, node):
        if node >= self.num_nodes or node < 0:
            print(f"Node {node} is out of range.")
            return

        self.adj_matrix.pop(node)
        for i in range(len(self.adj_matrix)):
            self.adj_matrix[i].pop(node)
        self.num_nodes -= 1

    def display(self):
        print("Adjacency Matrix:")
        for row in self.adj_matrix:
            print(" ".join(map(str, row)))

def main():
    num_nodes = int(input("Enter the amount of nodes in the graph: "))
    graph = Graph(num_nodes)
    num_edges = int(input(f"Enter the amount of edges: "))
    print("Enter each edge node as indicated example --> ('0 1'):")

    for _ in range(num_edges):
        u, v = map(int, input().split())
        graph.addEdge(u, v)
    print("\nGraph before deletion:")
    graph.display()
    nodeToDelete = int(input("\nEnter the node you want to delete: "))
    print(f"\nDeleting node {nodeToDelete}")
    graph.deleteNode(nodeToDelete)
    print("\nGraph after deletion:")
    graph.display()

if __name__ == "__main__":
    main()
