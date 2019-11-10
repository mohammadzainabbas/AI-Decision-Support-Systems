#Task No. 5

def FindPath(graph,start,end,path=[]):
    path = path + [start]

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

graph_3 = {7:[11,8],
           2:[],
           3:[8,10],
           11:[2,9,10],
           5:[11],
           9:[],
           8:[9]}

print(FindPath(graph_3,7,9,[]))
