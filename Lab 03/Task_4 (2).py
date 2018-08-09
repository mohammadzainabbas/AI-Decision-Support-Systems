#Task No. 4

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

graph_2 = {'A':['B','D','E'],'B':['D','E','A'],'C':['D'],'D':['A','B','C'],'E':['A','B']}
print(FindPath(graph_2,'E','C',[]))
