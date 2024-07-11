
import collections

def bfs_of_graph(graph,start):
    
    queue = collections.deque()
    visited=[]
    results=[]
    queue.append(start)
    visited.append(start)
    
    while queue:
        node = queue.popleft()
        results.append(node)
        # print("----------")
        # print(node)
        
        for ng in graph[node]:
            if ng not in visited:
                # print(ng)
                visited.append(ng)
                queue.append(ng)
    # print(visited)
    # print(queue)
    return results
            
        
    
graph={
    0:[1,2,3],
    1:[0,2],
    2:[0,1,4],
    3:[0],
    4:[2]
    }
print(bfs_of_graph(graph,4))

# O(N),O(N)
