class MyCircularQueue:

    def __init__(self, k: 'int'):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.queue = [None] * k
        self.size = k
        self.head = 0
        self.tail = 0

    def enQueue(self, value: 'int') -> 'bool':
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.queue[self.tail] is not None:
            nxt = (self.tail + 1) % self.size
            if self.queue[nxt] is None:
                self.queue[nxt] = value
                self.tail = nxt
            else:
                return False
        else:
            self.queue[self.tail] = value
        return True

    def deQueue(self) -> 'bool':
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.queue[self.head] is not None:
            self.queue[self.head] = None
            nxt = (self.head + 1) % self.size
            if self.queue[nxt] is None:
                self.head = 0
                self.tail = 0
            else:
                self.head = nxt
        else:
            return False
        return True

    def Front(self) -> 'int':
        """
        Get the front item from the queue.
        """
        return self.queue[self.head] if self.queue[self.head] is not None else -1

    def Rear(self) -> 'int':
        """
        Get the last item from the queue.
        """
        return self.queue[self.tail] if self.queue[self.tail] is not None else -1

    def isEmpty(self) -> 'bool':
        """
        Checks whether the circular queue is empty or not.
        """
        return True if self.queue[self.head] is None else False

    def isFull(self) -> 'bool':
        """
        Checks whether the circular queue is full or not.
        """
        return True if (self.tail + 1) % self.size == self.head else False


