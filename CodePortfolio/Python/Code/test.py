# An Iterative Python 3 program to do DFS  
# traversal from a given source vertex.  
# DFS(s) traverses vertices reachable from s. 
class Graph:  
    def __init__(self, V): 
        self.V = V  
        self.adj = [[] for i in range(V)] 
      
    def addEdge(self, v, w): 
        self.adj[v].append(w) # Add w to v’s list. 

    # prints all not yet visited vertices  
    # reachable from s  
    def DFSUtil(self, s, visited): 
          
        # Create a stack for DFS  
        stack = [] 
      
        # Push the current source node.  
        stack.append(s)  
        print(stack)
        while (len(stack) != 0): 
              
            # Pop a vertex from stack and print it  
            s = stack.pop() 
      
            # Stack may contain same vertex twice.  
            # So we need to prthe popped item only  
            # if it is not visited.  
            if (not visited[s]): 
                print(s, end = " ")  
                visited[s] = True
      
            # Get all adjacent vertices of the  
            # popped vertex s. If a adjacent has not   
            # been visited, then push it to the stack. 
            i = 0
            while i < len(self.adj[s]): 
                if (not visited[self.adj[s][i]]):  
                    stack.append(self.adj[s][i]) 
                i += 1
      
    # prints all vertices in DFS manner  
    def DFS(self): 
          
        # Mark all the vertices as not visited  
        visited = [False] * self.V
        
        for i in range(self.V):
            if (not visited[i]): 
                self.DFSUtil(i, visited) 
  
# Driver Code 
if __name__ == '__main__': 
  
    g = Graph(10) # Total 5 vertices in graph    
    g.addEdge(1,2)
    g.addEdge(3,2)
    g.addEdge(3,4)
    g.addEdge(5,6)
    g.addEdge(5,8)
    g.addEdge(7,4)
    g.addEdge(9,2)
    g.addEdge(9,8)
  
    print("Following is Depth First Traversal")  
    g.DFS() 