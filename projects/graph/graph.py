"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex] = set()
    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist!")    
    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # BFS
        # Create an empty Queue
        q = Queue()
        # Create an empty Visited set
        visited = set()
        # Add the starting vertex to the queue
        q.enqueue(starting_vertex)
        # While the queue is not empty...
        while q.size() > 0:
        # Dequeue the first vertex
            v = q.dequeue()
        # If it has not been visited...
            if v not in visited:
            # Mark it as visited (print it and add it to the visited set)
                print(v)
                visited.add(v)
            # Then enqueue each of its neighbors in the queue
                for neighbor in self.vertices[v]:
                    q.enqueue(neighbor)
        
    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # DFT
        # Create an empty Stack
        s = Stack()
        # Create an empty Visited set
        visited = set()
        # Push the starting vertex to the stack
        s.push(starting_vertex)
        # While the Stack is not empty...
        while s.size() > 0:
            # Pop the first vertex
            v = s.pop()
            # If it has not been visited...
            if v not in visited:
            # Mark it as visited (print it and add it to the visited set)
                print(v)
                visited.add(v)
            # Then push each of its neighbors onto the Stack
            for neighbor in self.vertices[v]:
                s.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=set() ):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        # Mark the starting node as visited
        print(starting_vertex)
        visited.add(starting_vertex)
        # Call DFT recursive on each neighbor
        for neighbor in self.vertices[starting_vertex]:
            if neighbor not in visited:
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        verts = self.vertices
        # maintain a queue of paths
        queue = []
        # push the first path into the queue
        queue.append([starting_vertex])
        while len(queue) > 0:
            # get the first path from the queue
            path = queue.pop(0)
            # get the last node from the path
            node = path[-1]
            # path found
            if node == destination_vertex:
                return print(path)
            # enumerate all adjacent nodes, construct a new path and push it into the queue
            for adjacent in verts.get(node, []):
                new_path = list(path)
                new_path.append(adjacent)
                queue.append(new_path)      

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create an empty stack
        s = Stack()
        # Create an empty set of visited vertices
        visited = set()
        # Put the starting vertex in our Stack
        s.push(starting_vertex)
        # While the value passed as "end" is not in the visit array....
        while destination_vertex not in visited:
            # Pop the top node from the stack
            v = s.pop()
            # If that node has not been visted...
            if v not in visited:
                    # Mark it as visited
                print(v)
                visited.add(v)
                # Then, put all of it's children into the stack
                if v is not None:
                    for neighbor in self.vertices[v]:
                        s.push(neighbor)
                else:
                    return print("they don't connect")





if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    # print(graph.vertices)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    # graph.dft(1)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    # graph.bft(1)

    '''
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    # graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
