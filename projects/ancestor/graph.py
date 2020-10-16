from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("noneexistent vertex")

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        # Create the empty Queue 
        q = Queue()
        # Create the visited dictionary
        visited = set()
        # Add all the starting_vertex into the queue
        q.enqueue(starting_vertex)
        # Loop through the queuse size if the size bigger than 0 then
        while q.size() > 0:
            # Set the variable for vertex to delete or remove from queue
            vertex = q.dequeue()
            # If vertex is not in visited yet 
            if vertex not in visited:
                print(vertex)
                # Add the vertex in to visited as already visit
                visited.add(vertex)
                for neighbor in self.get_neighbors(vertex):
                    q.enqueue(neighbor)
        
           
    def dft(self, starting_vertex):
        s = Stack()
        visited = set()

        s.push(starting_vertex)
        while s.size() > 0:
            vertex = s.pop()
            if vertex not in visited:
                print(vertex)
                visited.add(vertex)
                for neighbor in self.get_neighbors(vertex):
                    s.push(neighbor)


    def dft_recursive(self, starting_vertex, visited=set()):
        # Return self.dft(starting_vertex)
        if starting_vertex not in visited:
            visited.add(starting_vertex)
            print(starting_vertex)
            for neighbor in self.get_neighbors(starting_vertex):
                self.dft_recursive(neighbor, visited)
       


       
    def bfs(self, starting_vertex, destination_vertex):
        # Create an empty queue and enqueue A PATH TO the starting vertex ID
        q = Queue()
        # Enqueue A PATH TO the starting vertex ID
        q.enqueue([starting_vertex])
        # Create a Set to store visited vertices
        visited = set()
        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first PATH
            vertex = q.dequeue()
            # Grab the last vertex from the PATH
            last_vertex = vertex[-1]
            # If that vertex has not been visited...
            if last_vertex not in visited:
                if last_vertex == destination_vertex:
                    return vertex
                visited.add(last_vertex)
                for neighbor in self.get_neighbors(last_vertex):
                    # Next path is the list of new path
                    # Add the neighbor to the new path
                    next_path = vertex + [neighbor]
                    # Add the next path to the queue
                    # Append the neighbor to the back
                    q.enqueue(next_path)
    def dfs(self, starting_vertex, destination_vertex):
        # Create an empty Stack and push a path to the starting vertex ID
        s = Stack()
        # Push the starting vertex ID
        s.push([starting_vertex])
        # Create a Set to store visited vertices
        visited = set()
        # While the Stack is not empty
        while s.size() > 0:
            # Pop the first path of the stack
            vertex = s.pop()
            # Grab the last vertex from the Path
            last_vertex = vertex[-1]
            # If that vertex has not been visited...
            if last_vertex not in visited:
                # Check if the vertex is equal to target
                if last_vertex == destination_vertex:
                    # If yes return the path
                    return vertex
                # Mark the vertex as visited.
                visited.add(last_vertex)
                # Then add a path its neighbors to the back of the queue
				# Copy the path and append the neighbor to back  
                for neighbor in self.get_neighbors(last_vertex):
                    next_path = vertex[:]
                    next_path.append(neighbor)
                    s.push(next_path)
        return None

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=set(), path=[]):
        # Check if the starting vertex if not visited yet
        if starting_vertex not in visited:
            # Add the starting vertex into visited dictionary 
            visited.add(starting_vertex)
        # Check if the starting vertex is in the path 
        if starting_vertex not in path:
            # If if still empty we store that starting to path as list
            path = [starting_vertex]
        # Loop through all neighbor of starting vertex
        for neighbor in self.get_neighbors(starting_vertex):
            # Check if not visit that neighbor yet add the visiting neighbor to visited
            if neighbor not in visited:
                # Copy the new path of neighbor
                new_path = path +[neighbor]
                # If neighbor equal to destination or target return that new path
                if neighbor == destination_vertex:
                    # Return the new path
                    return new_path
                # Other wise create the variable that store call back function 
                dfs_path = self.dfs_recursive(neighbor, destination_vertex, visited, new_path)
                # Check if that the dfs path is not none then we return the the dfs path
                if dfs_path is not None:
                    return dfs_path
        return None