import queue as Q
##
##def A_Star(g, s_node, g_node, priority = 0, path = []):
##    pq = queue.PriorityQueue();
##    pq.put((priority, (s_node, 0)));
##    while(not pq.empty()):
##        u = pq.get();
##        pq = queue.PriorityQueue();
##        if u[1][0] == g_node:
##            path.append(g_node);
##            return path;
##        else:
##            for v in g[u[1][0]]:
##                if v not in path:
##                    edge_cost = g[u[1][0]][v];
##                    pq.put(( u[1][1] + edge_cost + heuristic[v], (v, u[1][1] + edge_cost )));
##        path.append(u[1][0]);
##    return path;
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



##
##
##def A_star(graph,start_node, goal_node):
##    pq = Q.PriorityQueue()
##    pq.put((start_node, 0))
##    came_from = {}
##    cost_so_far = {}
##    came_from[start_node] = None
##    cost_so_far[start_node] = 0
##
##    while(not pq.empty()):
##        current = pq.get()
##
##        if current == goal_node:
##            break
##        for next in graph[current[0]]:
##            new_cost = cost_so_far[current] + graph.cost(current, next)
##
##            if next not in cost_so_far or new_cost < cost_so_far[next]:
##                cost_so_far[next] = new_cost
##                priority = new_cost + heuristic(goal, next)
##                pq.put((next, priority))
##                came_from[next] = current
##
##    return Reconstruct_Path(came_from, start_node, goal)
##
##def heuristic(a, b):
##    (x1, y1) = a
##    (x2, y2) = b
##    return (abs(x1 - x2) + abs(y1 - y2))
##    
##def Reconstruct_Path(came_from,start_node, goal):
##
##    current_node = goal
##    path = []
##    
##    while (current_node != start_node):
##        path.append(current_node)
##        current_node = came_from[current_node]
##
##    path.append(start_node)
##    path.reverse()
##
##    return path

graph_t = {'A':[{'B':[5]},{'D':[3]}],
           'B':[{'C':5}],
           'C':[{'A':[3]},{'D':[2]},{'E':[4]}],
           'D':[{'F':[6]},{'E':[2]}],
           'E':[{'B':[2]},{'G':[1]}],
           'F':[{'G':[9]}],
           'G':[{}]}

path_1 = {'Arad':366,
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
           'Neamt':234}
##
##graph_1 = {'Arad':[{'Zerind':75},{'Timisoara':118},{'Sibiu':140}],
##           'Zerind':[{'Oradea':71},{'Arad':75}],
##           'Timisoara':[{'Lugoj':111},{'Arad':118}],
##           'Sibiu':[{'Arad':140},{'Oradea':151},{'Fagaras':99},{'Rimnicu Vilcea':80}],
##           'Oradea':[{'Zerind':71},{'Sibiu':151}],
##           'Lugoj':[{'Mehadia':70},{'Timisoara':111}],
##           'Mehadia':[{'Lugoj':70},{'Dobreta':75}],
##           'Dobreta':[{'Mehadia':75},{'Craiova':120}],
##           'Rimnicu Vilcea':[{'Craiova':146},{'Pitesti':97},{'Sibiu':80}],
##           'Craiova':[{'Dobreta':120},{'Rimnicu Vilcea':146},{'Pitesti':138}],
##           'Fagaras':[{'Bucharest':211},{'Sibiu':99}],
##           'Pitesti':[{'Craiova':138},{'Rimnicu Vilcea':97},{'Bucharest':101}],
##           'Bucharest':[{'Fagaras':211},{'Pitesti':101},{'Giurgiu':90},{'Urziceni':85}],
##           'Giurgiu':[{'Bucharest':90}],
##           'Urziceni':[{'Bucharest':85},{'Hirsova':98},{'Vaslui':142}],
##           'Eforie':[{'Hirsova':86}],
##           'Hirsova':[{'Urziceni':98},{'Eforie':86}],
##           'Vaslui':[{'Urziceni':142},{'Lasi':92}],
##           'Lasi':[{'Vaslui':92},{'Neamt':87}],
##           'Neamt':[{'Lasi':87}]};

graph_1 = {'Arad': {'Zerind': 75, 'Timisoara': 118, 'Sibiu': 140},
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

