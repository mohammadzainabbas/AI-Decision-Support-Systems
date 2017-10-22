#Task No. 08

def FindAllPath(graph,start,end,path=[]):
    path = path + [start];

    if (start == end):
        return [path]
    if not graph.__contains__(start):
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            new_paths = FindAllPath(graph,node,end,path)
            for new_path in new_paths:
                paths.append(new_path)
    return paths

graph_2 = {'A':['B','D','E'],'B':['D','E','A'],'C':['D'],'D':['A','B','C'],'E':['A','B']}

print(FindAllPath(graph_2,'E','C',[]))
