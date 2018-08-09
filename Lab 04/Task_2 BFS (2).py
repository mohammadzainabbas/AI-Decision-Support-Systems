class FIFO_Queue:
    def __init__(self):
        self.queue = []

    def add(self, value):
        self.queue.insert(0,value)
        
    def remove(self):
        if (len(self.queue) == 0):
            raise indexError
        else:
            return self.queue.pop()
        
    def isEmpty(self):
        return (len(self.queue) == 0)
    
    def PrintQueue(self):
        for i in range(len(self.queue)):
            print(self.queue[i])
    def printQueue(self):
        print(self.queue)

def BFS_SearchPath(graph, start, end, queue):
    temp_path = [start]

    queue.add(temp_path)

    while queue.isEmpty() == False:
        temp = queue.remove()

        last_node = temp[len(temp) - 1]

        if last_node == end:
            print("Path is: ",temp)

        for link_node in graph[last_node]:
            if link_node not in temp:
                new_path = []
                new_path = temp + [link_node]
                queue.add(new_path)

# visits all the nodes of a graph (connected component) using BFS
def BFS(graph, start):
    # keep track of all visited nodes
    explored = []
    # keep track of nodes to be checked
    queue = FIFO_Queue()
    queue.add(start)
 
    # keep looping until there are nodes still to be checked
    while queue.isEmpty() == False:
        # pop shallowest node (first node) from queue
        node = queue.remove()
        if node not in explored:
            # add node to list of checked nodes
            explored.append(node)
            neighbours = graph[node]
 
            # add neighbours of node to queue
            for neighbour in neighbours:
                queue.add(neighbour)
    return explored

def main():
##    a = FIFO_Queue()
##    for i in range(5):
##        a.add(2*i)
##        a.printQueue()
##    #a.printQueue()
##
##    a.remove()
##    print('After')
##    a.printQueue()

    graph = {'A': ['B', 'C','E'],
             'B': ['A','C', 'D'],
             'C': ['D'],
             'D': ['C'],
             'E': ['F','D'],
             'F': ['C']}
    graph_1 = {6:[4],
               4:[6,3,5],
               3:[4,2],
               5:[4,2,1],
               2:[5,3,1],
               1:[2,5]
               }
    Tree_1 = {1: [2, 3, 4],
              2: [1, 5, 6],
              3: [1],
              4: [1, 7, 8],
              5: [2, 9, 10],
              6: [2],
              7: [4, 11, 12],
              8: [4],
              9: [5],
              10:[5],
              11:[7],
              12:[7]}
    Tree_2 = {'Frankfurt':['Mannheim', 'Wurzburg', 'Kassel'],
              'Mannheim':['Karlsruhe'],
              'Wurzburg':['Nurnberg','Erfurt'],
              'Kassel':['Munchen'],
              'Karlsruhe':['Augsburg'],
              'Nurnberg':['Stuttgart'],
              'Erfurt':[],
              'Munchen':[],
              'Augsburg':[],
              'Stuttgart':[]}

    b = FIFO_Queue()
    #BFS_SearchPath(Tree_1, 1, 10,b)
    print(BFS(Tree_1, 1))
    print(BFS(Tree_2, 'Frankfurt'))
    print(BFS(graph,'A'))
    print(BFS(graph_1,6))

main()
