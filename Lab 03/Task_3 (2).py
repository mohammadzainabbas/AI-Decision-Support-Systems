#Task No. 3

def FindPath(graph,start,end,path=[]):
    path = path + [start];

    if (start == end):
        return path
    if (start not in graph):
        return None
    
    for node in graph[start]:
            if node not in path:
                path = FindPath(graph,node,end,path)
            if path:
                return path
    return None

graph_1 = {1:[2,5],2:[1,3,5],3:[2,4],4:[3,5,6],5:[1,2,4],6:[4]}
print(FindPath(graph_1,6,1,[]))