class Queue:
    def __init__(self):
        self.size=5
        self.queue=list(range(self.size))
        self.i=0
        self.o=0

        self.isEmpty=True
        self.isFull=False

    def _increment(self,val):
        if val+1==self.size:
            return 0
        else:
            return val+1
    
    def enqueue(self,val):
        if self.isFull:
            raise IndexError("Queue is Full")
        self.queue[self.i]=val
        self.i=self._increment(self.i)

        if self.i==self.o:
            self.isFull=True
        self.isEmpty=False
    def dequeue(self):
            if self.isEmpty:
                raise IndexError("Queue is empty")
            
            ret=self.queue[self.o]
            self.o=self._increment(self.o)
            if self.i==self.o:
                self.isEmpty=True
            self.isFull=False
          
            return ret
    def __str__(self):
            return str(self.queue)

q=Queue()
q.enqueue(100)
q.enqueue(60)
q.enqueue(100)
q.enqueue(60)
q.enqueue(100)
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()



