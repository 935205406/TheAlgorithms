"""
循环队列是一种线性数据结构，其操作表现基于 FIFO（先进先出）原则并且队尾被连接在队首之后以形成一个循环。它也被称为“环形缓冲器”。

循环队列的一个好处是我们可以利用这个队列之前用过的空间。在一个普通队列里，一旦一个队列满了，我们就不能插入下一个元素，
即使在队列前面仍有空间。但是使用循环队列，我们能使用这些空间去存储新的值。

你的实现应该支持如下操作：

MyCircularQueue(k): 构造器，设置队列长度为 k 。
Front: 从队首获取元素。如果队列为空，返回 -1 。
Rear: 获取队尾元素。如果队列为空，返回 -1 。
enQueue(value): 向循环队列插入一个元素。如果成功插入则返回真。
deQueue(): 从循环队列中删除一个元素。如果成功删除则返回真。
isEmpty(): 检查循环队列是否为空。
isFull(): 检查循环队列是否已满。
"""


class MyCircularQueue:
    def __init__(self, k):
        """构造器

        :param k:设置队列长度为k
        """
        if not isinstance(k, int) or k <= 0:
            raise TypeError("queue size should be a int value greater than 0")
        self.length = k
        self.queue = [i for i in range(k)]
        self.head = -1  # 表示为空队列
        self.tail = -1  # 表示为空队列

    def en_queue(self, value):
        """向循环队列插入一个元素。如果成功插入则返回真。

        :param value: 要插入的元素，插入队列最后
        :return:
        """
        # 队列已满，返回false
        if self.is_full():
            return False
        # 队列为空，需要初始化head的索引
        if self.is_empty():
            self.head = 0
        # 其他情况，head无需变化，仅需修改tail即可
        self.tail = (self.tail + 1) % self.length  # 更新tail的索引。循环队列，tail的索引使用取模运算获得
        self.queue[self.tail] = value
        return True

    def is_full(self):
        """判断是否已满

        :return:
        """
        return (self.tail + 1) % self.length == self.head

    def de_queue(self):
        """从循环队列中删除一个元素(删除队首元素)。如果成功删除则返回真。

        :return: 如果成功删除则返回真
        """
        # 队列为空，返回false
        if self.is_empty():
            return False
        if self.head == self.tail:
            self.head = self.tail = -1  # 两者指针相同，说明队列只有一个元素，删除后为空
            return True
        else:
            self.head = (self.head + 1) % self.length  # 更新 head 的索引。循环队列，head的索引使用取模运算获得
            return True

    def is_empty(self):
        """检查循环队列是否为空。

        :return:
        """
        return self.head == -1 and self.tail == -1

    def front(self):
        """从队首获取元素。

        :return: 如果队列为空，返回 -1 。
        """
        if self.is_empty():
            return -1
        # 其他情况肯定可以获取出数据
        return self.queue[self.head]

    def rear(self):
        """ 获取队尾元素。

        :return: 如果队列为空，返回 -1 。
        """
        if self.is_empty():
            return -1
        return self.queue[self.tail]


def main():
    circular_queue = MyCircularQueue(3)
    print(circular_queue.en_queue(1))  # 返回true
    print(circular_queue.en_queue(2))  # 返回true
    print(circular_queue.en_queue(3))  # 返回true
    print(circular_queue.en_queue(4))  # 返回false
    print(circular_queue.rear())  # 返回3
    print(circular_queue.is_full())  # 返回true
    print(circular_queue.de_queue())  # 返回true  删除队首元素1
    print(circular_queue.en_queue(4)) # 返回true  剩余元素为 2,3,4
    print(circular_queue.rear())  # 返回4
    print(circular_queue.front())  # 返回2


if __name__ == '__main__':
    main()
