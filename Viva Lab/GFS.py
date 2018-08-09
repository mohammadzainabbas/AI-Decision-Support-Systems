import time as t
import queue as Q

#Greedy best first search algorithm
def GFS(graph, start_node, goal_node, priority = 0, path = []):
    #Initializing priority queue
    pq = Q.PriorityQueue()
    #Putting start node with lowest priority
    pq.put((start_node, priority))

    #Loop till queue is not empty
    while(not pq.empty()):
        #Pop from queue
        current = pq.get()
        pq = Q.PriorityQueue()

        #Goal check (current[0] -> current-node) 
        if current[0] == goal_node:
            path.append(current[0])
            return path
        else:
            for values in graph[current[0]]:    #Node's childs -> values
                for key in values.keys():       #Checking each child's keys
                    if key not in path:         #If key not in path. key -> child-node
                        pq.put((key, values[key]))  #put in priority queue -> (child-node, child-node's value)
            path.append(current[0])                 #append(current-node) in path
    return path

graph = {'v1':[{'v2':[1]},{'v3':[3]},{'v5':[6]}],
           'v2':[{'v1':[1]},{'v3':[2]},{'v4':[3]},{'v5':[5]}],
           'v3':[{'v1':[3]},{'v2':[2]},{'v4':[5]},{'v6':[2]}],
           'v4':[{'v2':[3]},{'v3':[5]},{'v5':[2]},{'v6':[4]}],
           'v5':[{'v1':[6]},{'v2':[5]},{'v4':[2]},{'v6':[1]}],
           'v6':[{'v3':[2]},{'v4':[4]},{'v5':[1]}]}
a = t.clock()
print(GFS(graph, 'v1', 'v5'))
b = t.clock()
print('Total time taken by algorithm is ' + str(b-a))
