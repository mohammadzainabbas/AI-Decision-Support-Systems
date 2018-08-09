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

    img = [[150,2,5],
           [80,145,45],
           [74,102,165]]

    print(img)
    graph = {5:[2,145,45],
             2:[150,80,145,45,5],
             145:[150,2,5,80,45,74,102,165],
             45:[5,2,145,102,165],
             150:[2,80,145],
             80:[150,2,145,102,74],
             74:[80,145,102],
             102:[74,80,145,45,165],
             165:[102,145,45]}

    print(BFS(graph,5))
    
main()
