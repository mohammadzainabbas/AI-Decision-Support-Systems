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

def main():
    a = LIFO_Queue()
    for i in range(5):
        a.add(2*i)
        a.printQueue()
    #a.printQueue()

    a.remove()
    print('After')
    a.printQueue()

main()
