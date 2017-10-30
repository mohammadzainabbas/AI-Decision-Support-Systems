class LIFO_Queue:
    def __init__(self):
        self.queue = []

    def add(self, value):
        self.queue.append(value)
        
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

# visits all the nodes of a graph (connected component) using BFS
def DFS(graph, start):
    # keep track of all visited nodes
    explored = []
    # keep track of nodes to be checked
    queue = LIFO_Queue()
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

    graph_1 = {6:[4],
               4:[6,3,5],
               3:[4,2],
               5:[4,2,1],
               2:[5,3,1],
               1:[2,5]
               }
    graph_2 = {'E':['B','A'],
               'B':['E','A'],
               'A':['E','B','D'],
               'D':['A','B','C'],
               'C':['D']}
    Tree_1 = {1: [3, 2],
              2: [5, 4, 1],
              3: [1],
              4: [6, 2],
              5: [8, 7, 2],
              6: [4],
              7: [5],
              8: [5]}
    Tree_2 = {50:[76,17],
              17:[23, 9],
              9:[14],
              14:[12],
              23:[19],
              76:[54],
              54:[72],
              72:[67],
              67:[],
              12:[],
              19:[]}

    print(DFS(Tree_1, 1))
    print(DFS(Tree_2, 50))
    print(DFS(graph_1,1))
    print(DFS(graph_2,'E'))

main()

