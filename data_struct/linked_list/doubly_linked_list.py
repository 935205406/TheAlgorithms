'''
- A linked list is similar to an array, it holds values. However, links in a linked list do not have indexes.
- This is an example of a double ended, doubly linked list.
- Each link references the next link and the previous one.
- A Doubly Linked List (DLL) contains an extra pointer, typically called previous pointer, together with next pointer and data which are there in singly linked list.
 - Advantages over SLL - IT can be traversed in both forward and backward direction.,Delete operation is more efficent'''


class Link:
    next = None
    previous = None

    def __init__(self, x):
        self.value = x

    def displayLink(self):
        print("{}".format(self.value), end=" ")


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_head(self, x):
        new_link = Link(x)  # create a new Link with a value attached to it
        if self.is_empty():  # set the first element to be the tail
            self.tail = new_link
        else:
            self.head.previous = new_link  # new_link <-- currenthead(head)
        new_link.next = self.head  # new_link <--> currenthead(head)
        self.head = new_link  # new_link(head) <--> oldhead

    def delete_head(self):
        temp = self.head
        self.head = self.head.next
        if self.head is None:  # 说明就一个元素，该元素已经删除了
            self.tail = None  # 需要清除tail的内容
        else:
            self.head.previous = None
        return temp

    def insert_tail(self, x):
        if self.is_empty():
            self.insert_head(x)
        else:
            new_link = Link(x)
            self.tail.next = new_link
            new_link.previous = self.tail
            self.tail = new_link

    def delete_tail(self):
        temp = self.tail
        self.tail = temp.previous
        if self.tail is None:  # 说明就一个元素，该元素还被删除了
            self.head = None
        else:
            self.tail.next = None
        return temp

    def delete(self, x):
        current = self.head
        while current.value != x:
            current = current.next
        if current == self.head:
            self.delete_head()
        elif current == self.tail:
            self.delete_tail()
        else:
            current.previous.next = current.next
            current.next.previous = current.previous

    def is_empty(self):
        return self.head is None

    def display(self):
        current = self.head
        while current is not None:
            current.displayLink()
            current = current.next
        print()


def main():
    l = LinkedList()
    a1 = input("insert head")
    l.insert_head(a1)
    a2 = input("insert head")
    l.insert_head(a2)
    print("打印列表")
    l.display()
    a3 = input("insert tail")
    l.insert_tail(a3)
    a4 = input("insert tail")
    l.insert_tail(a4)
    print("打印列表")
    l.display()
    print("\n删除head")
    l.delete_head()
    print("打印列表")
    l.display()
    print("\n删除tail")
    l.delete_tail()
    print("打印列表")
    l.display()
    print("插入大量数据")
    l.insert_tail("9")
    l.insert_tail("4")
    l.insert_tail("6")
    l.insert_tail("8")
    print("打印最新列表")
    l.display()
    a5 = input("要删除的数据是")
    l.delete(a5)
    print("删除后，列表为")
    l.display()


if __name__ == '__main__':
    main()
