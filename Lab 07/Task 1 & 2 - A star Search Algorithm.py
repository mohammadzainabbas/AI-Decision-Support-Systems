import queue as Q

def A_Star(graph, straight_line_distance, start_node, goal_node, priority = 0, path = []):
    pq = Q.PriorityQueue()
    pq.put((priority, (start_node, 0)))
    while(not pq.empty()):
        current = pq.get()
        pq = Q.PriorityQueue()
        if current[1][0] == goal_node:
            path.append(current[1][0])
            return path
        else:
            for value in graph[current[1][0]]:
                if value not in path:
                    edge_cost = graph[current[1][0]][value]
                    pq.put(((current[1][1] + edge_cost + straight_line_distance[value]), (value, current[1][1] + edge_cost)))
            path.append(current[1][0])
    return path

path_1 = { 'Arad':366,
           'Zerind':374,
           'Timisoara':329,
           'Sibiu':253,
           'Oradea':380,
           'Lugoj':244,
           'Mehadia':241,
           'Dobreta':242,
           'Rimnicu Vilcea':193,
           'Craiova':160,
           'Fagaras':178,
           'Pitesti':98,
           'Bucharest':0,
           'Giurgiu':77,
           'Urziceni':80,
           'Eforie':161,
           'Hirsova':151,
           'Vaslui':199,
           'Lasi':226,
           'Neamt':234 }

graph_1= {'Arad': {'Zerind': 75, 'Timisoara': 118, 'Sibiu': 140},
          'Zerind': {'Oradea': 71, 'Arad': 75},
          'Timisoara': {'Lugoj': 111, 'Arad': 118},
          'Sibiu': {'Arad': 140, 'Oradea': 151, 'Fagaras': 99, 'Rimnicu Vilcea': 80},
          'Oradea': {'Zerind': 71, 'Sibiu': 151},
          'Lugoj': {'Mehadia': 70, 'Timisoara': 111},
          'Mehadia': {'Lugoj': 70, 'Dobreta': 75},
          'Dobreta': {'Mehadia': 75, 'Craiova': 120},
          'Rimnicu Vilcea': {'Craiova': 146, 'Pitesti': 97, 'Sibiu': 80},
          'Craiova': {'Dobreta': 120, 'Rimnicu Vilcea': 146, 'Pitesti': 138},
          'Fagaras': {'Bucharest': 211, 'Sibiu': 99},
          'Pitesti': {'Craiova': 138, 'Rimnicu Vilcea': 97, 'Bucharest': 101},
          'Bucharest': {'Fagaras': 211, 'Pitesti': 101, 'Giurgiu': 90, 'Urziceni': 85},
          'Giurgiu': {'Bucharest': 90},
          'Urziceni': {'Bucharest': 85, 'Hirsova': 98, 'Vaslui': 142},
          'Eforie': {'Hirsova': 86},
          'Hirsova': {'Urziceni': 98, 'Eforie': 86},
          'Vaslui': {'Urziceni': 142, 'Lasi': 92},
          'Lasi': {'Vaslui': 92, 'Neamt': 87},
          'Neamt': {'Lasi': 87}};


print(A_Star(graph = graph_1, straight_line_distance = path_1, start_node = 'Arad', goal_node = 'Bucharest', priority = 0, path = []))
##print(A_star(graph_1, 'Arad', 'Bucharest', 0, []))
