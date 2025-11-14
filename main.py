from collections import deque
from heapq import heappush, heappop 

def shortest_shortest_path(graph, source):
    """
    Params: 
      graph.....a graph represented as a dict where each key is a vertex
                and the value is a set of (vertex, weight) tuples (as in the test case)
      source....the source node
      
    Returns:
      a dict where each key is a vertex and the value is a tuple of
      (shortest path weight, shortest path number of edges). See test case for example.
    """
    # initialize distances - weight, number of edges
    dist = {v: (float('inf'), float('inf')) for v in graph}
    dist[source] = (0, 0)
    
    # priority queue - weight, number of edges, vertex
    pq = [(0, 0, source)]
    visited = set()
    
    while pq:
        weight, num_edges, u = heappop(pq)
        
        # skip if we've already found a better path
        if u in visited:
            continue
            
        visited.add(u)
        
        # explore neighbors
        for v, edge_weight in graph.get(u, set()):
            new_weight = weight + edge_weight
            new_num_edges = num_edges + 1
            
            # update if we find a better path - lower weight or same weight but fewer edges
            current_weight, current_edges = dist[v]
            if (new_weight < current_weight or 
                (new_weight == current_weight and new_num_edges < current_edges)):
                dist[v] = (new_weight, new_num_edges)
                heappush(pq, (new_weight, new_num_edges, v))
    
    return dist
    

    
    
def bfs_path(graph, source):
    """
    Returns:
      a dict where each key is a vertex and the value is the parent of 
      that vertex in the shortest path tree.
    """
    parents = {}
    queue = deque([source])
    visited = {source}
    
    while queue:
        u = queue.popleft()
        
        # explore neighbors
        for v in graph.get(u, set()):
            if v not in visited:
                visited.add(v)
                parents[v] = u
                queue.append(v)
    
    return parents

def get_sample_graph():
     return {'s': {'a', 'b'},
            'a': {'b'},
            'b': {'c'},
            'c': {'a', 'd'},
            'd': {}
            }


    
def get_path(parents, destination):
    """
    Returns:
      The shortest path from the source node to this destination node 
      (excluding the destination node itself). See test_get_path for an example.
    """
    path = []
    current = destination
    
    # go backwards through parents until source is reached
    while current in parents:
        parent = parents[current]
        path.append(parent)
        current = parent
    
    # reverse to get path from source to destination - excluding destination
    return ''.join(reversed(path))

