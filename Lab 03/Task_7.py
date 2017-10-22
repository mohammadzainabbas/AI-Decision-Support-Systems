#Task No. 07

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

graph_1 = {1:[2,5],
           2:[1,3,5],
           3:[2,4],
           4:[3,5,6],
           5:[1,2,4],
           6:[4]}
graph_t = {1:[2,3],
           2:[1,3],
           3:[2,1]}
print(FindAllPath(graph_1,6,1,[]))