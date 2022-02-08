# Dijkstra

from queue import PriorityQueue

def dijkstra(graph, start):
    distances = {}
    visited = [start]

    half_known = PriorityQueue()
    half_known.put((0, start))
    while not half_known.empty():
        (dist, current) = half_known.get() 
        visited += [current]

        for neighbor, cost in enumerate(graph[current]):
            if neighbor in visited:
                continue
            if neighbor not in distances.keys() or \
               cost + dist < distances[neighbor]:
                distances[neighbor] = cost + dist
                half_known.put((cost + dist, neighbor))
    return distances
                
    





graph = [[ 10000, 10,  3,  100000],
         [10,  100000,  2,  1],
         [ 3,  2,  100000,  100000],
         [ 100000,  1,  100000,  100000]]

start = 0

print (dijkstra(graph, start))
