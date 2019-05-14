
class Node:  # create a node
    def __init__(self, data):
        self.data = data  # given data
        self.next = None  # given next to None


class LinkedList:
    def __init__(self):
        self.Head = None  # Initialize Head to None

    def insert_tail(self, data):
        if self.Head is None:
            self.insert_head(data)  # If this is first node, call insert head
        else:
            temp = self.Head
            while temp.next is not None:  # traverse to last node
                temp = temp.next
            temp.next = Node(data)  # create node & link to tail

    def insert_head(self, data):
        newNod = Node(data)  # create a node
        if self.Head is not None:
            newNod.next = self.Head  # link new node to Head
        self.Head = newNod  # make new node as Head

    def print_list(self):  # print every node data
        temp = self.Head
        while temp is not None:
            print(temp.data)
            temp = temp.next

    def delete_head(self):  # delete from head
        temp = self.Head
        if temp is not None:
            self.Head = self.Head.next
            temp.next = None
        return temp

    def delete_tail(self):  # delete from tail
        temp = self.Head
        if temp is not None:
            if self.Head.next is None:  # If head is the only Node in the linked list
                self.Head = None
            else:
                while temp.next.next is not None:  # find the 2nd last element
                    temp = temp.next
                temp.next, temp = None, temp.next  # (2nd last element).next = None and temp = last element to return
        return temp

    def isEmpty(self):
        return self.Head is None  # return true if Head is None

    def resverse(self):
        prev = None
        current = self.Head

        while current:
            # store the current node's next node
            next_node = current.next
            # Make the current node's next point backwards
            current.next = prev
            # Make the previous node be the current node
            prev = current
            # Make the current node be the "next node" (to progress iteration)
            current = next_node
        # return prev in order to put the head at the end
        self.Head = prev


def main():
    A = LinkedList()
    print("Insertint 1st at Head")
    a1 = input()
    A.insert_head(a1)
    print("Inserting 2st at Head")
    a2 = input()
    A.insert_head(a2)
    print("\nprint List : ")
    A.print_list()
    print("Inserting 1st at Tail")
    a3 = input()
    A.insert_tail(a3)
    print("Inserting 2st at Tail")
    a4 = input()
    A.insert_tail(a4)
    print("\nprint List : ")
    A.print_list()
    print("\nDelete Head")
    A.delete_head()
    print("\nDelete Tail")
    A.delete_tail()
    print("\nprint List : ")
    A.print_list()
    print("\nReserve Linked List : ")
    A.resverse()
    print("\nprint List : ")
    A.print_list()


if __name__ == "__main__":
    main()
