class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def spilit_list(self):
        the_head = self.head
        count = 0
        prev_node = None
        while the_head:
            count += 1
            the_head = the_head.next
            if the_head == self.head:
                break
        if count:
            newCount = count // 2
            while the_head and newCount != count:
                prev_node = the_head
                newCount += 1
                the_head = the_head.next
            prev_node.next = self.head
            split_list = CircularLinkedList()
            while the_head.next != self.head:
                split_list.append(the_head.data)
                the_head = the_head.next
            split_list.append(the_head.data)
            self.print()
            # print("\n")
            split_list.print()

    def delete_with_key(self, key):
        the_head = self.head
        prev_node = None
        while the_head and the_head.data != key:
            prev_node = the_head
            the_head = the_head.next
        if the_head:
            if prev_node:
                prev_node.next = the_head.next
                the_head = None
            else:
                while the_head.next != self.head:
                    the_head = the_head.next
                the_head.next = self.head.next
                self.head = the_head.next
        else:
            raise Exception('data not found')


    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return
        the_head = self.head
        ## 1 2 3 4 and the new_node is 0
        new_node.next = self.head
        ## new_node ka next yani 0 ka next is head mtlb
        ## 0 1 2 3 4  
        while the_head.next != self.head:
            the_head = the_head.next
        the_head.next = new_node
        self.head = new_node

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        the_head = self.head
        while the_head.next != self.head:
            the_head = the_head.next
        the_head.next = new_node
        new_node.next = self.head

    def print(self):
        the_head = self.head
        while the_head:
            print(the_head.data, end=' -> ')
            the_head = the_head.next
            if the_head == self.head:
                break
        print(self.head.data)
    




cl = CircularLinkedList()
cl.append(1)
cl.append(2)
cl.append(3)
cl.append(4)
cl.append(5)
cl.append(6)
cl.print()

cl.spilit_list()