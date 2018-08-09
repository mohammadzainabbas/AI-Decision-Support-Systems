import queue as Q

def GBFS(graph, start_node, goal_node, priority = 0, path = []):
    pq = Q.PriorityQueue()
    pq.put((priority, start_node))

    while(not pq.empty()):
        u = pq.get()
        pq = Q.PriorityQueue()
        if u[1] == goal_node:
            path.append(u[1])
            return path
        else:
            for values in graph[u[1]]:
                for key in values.keys():
                    if key not in path:
                        pq.put((values[key], key))
            path.append(u[1])
    return path

graph_1 = {'A':[{'B':[5]},{'D':[3]}],
           'B':[{'C':5}],
           'C':[{'A':[3]},{'D':[2]},{'E':[4]}],
           'D':[{'F':[6]},{'E':[2]}],
           'E':[{'B':[2]},{'G':[1]}],
           'F':[{'G':[9]}],
           'G':[{}]}

graph_2 = {'Arad':[{'Zerind':75},{'Timisoara':118},{'Sibiu':140}],
           'Zerind':[{'Oradea':71},{'Arad':75}],
           'Timisoara':[{'Lugoj':111},{'Arad':118}],
           'Sibiu':[{'Arad':140},{'Oradea':151},{'Fagaras':99},{'Rimnicu Vilcea':80}],
           'Oradea':[{'Zerind':71},{'Sibiu':151}],
           'Lugoj':[{'Mehadia':70},{'Timisoara':111}],
           'Mehadia':[{'Lugoj':70},{'Dobreta':75}],
           'Dobreta':[{'Mehadia':75},{'Craiova':120}],
           'Rimnicu Vilcea':[{'Craiova':146},{'Pitesti':97},{'Sibiu':80}],
           'Craiova':[{'Dobreta':120},{'Rimnicu Vilcea':146},{'Pitesti':138}],
           'Fagaras':[{'Bucharest':211},{'Sibiu':99}],
           'Pitesti':[{'Craiova':138},{'Rimnicu Vilcea':97},{'Bucharest':101}],
           'Bucharest':[{'Fagaras':211},{'Pitesti':101},{'Giurgiu':90},{'Urziceni':85}],
           'Giurgiu':[{'Bucharest':90}],
           'Urziceni':[{'Bucharest':85},{'Hirsova':98},{'Vaslui':142}],
           'Eforie':[{'Hirsova':86}],
           'Hirsova':[{'Urziceni':98},{'Eforie':86}],
           'Vaslui':[{'Urziceni':142},{'Lasi':92}],
           'Lasi':[{'Vaslui':92},{'Neamt':87}],
           'Neamt':[{'Lasi':87}]};

print(GBFS(graph_1, 'A', 'G'))
print(GBFS(graph_2, 'Arad', 'Bucharest', 0, []))