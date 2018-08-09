#Task No. 06

def FindPath(graph,start,end,path=[]):
    path = path + [start];

    if (start == end):
        return path
    if not graph.__contains__(start):
        return None
    
    for node in graph[start]:
            if node not in path:
                new_path = FindPath(graph,node,end,path)
            if new_path:
                return new_path
    return None

graph_4 = {'A':['B'],'B':['C','D','E'],'C':['E'],'D':['E'],'E':['F'],'F':[],'G':['D']}

print(FindPath(graph_4,'A','F',[]))