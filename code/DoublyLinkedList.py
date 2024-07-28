class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def remove_dup(self):
        if not self.head:
            return None
        the_head = self.head
        prev_node = None
        dup = {}
        while the_head:
            if the_head.data in dup:
                prev_node.next = the_head.next
                the_head.next.prev = prev_node
                the_head = None
            else:
                dup[the_head.data] = 1
                prev_node = the_head
            the_head = prev_node.next
            

    def reverse(self):
        the_head = self.head
        prev_node = None
        while the_head:
            next_node = the_head.next
            the_head.next = prev_node
            the_head.prev = next_node
            prev_node = the_head
            the_head = next_node
        self.head = prev_node

    def delete_a_node(self, key):
        the_head = self.head
        prev_node = None
        while the_head and the_head.data != key:
            prev_node = the_head
            the_head = the_head.next
        if the_head:
            if prev_node:
                prev_node.next = the_head.next
                the_head.next.prev = prev_node
                the_head = None
            else:
                self.head = the_head.next
                the_head.next.prev = None
                the_head = None
        else:
            raise Exception('data not found...')

    def append_after_node(self, data, key):
        new_node = Node(data)
        the_head = self.head
        prev_node = None
        while the_head and the_head.data != key:
            prev_node = the_head
            the_head = the_head.next

        if the_head:
            if prev_node:
                prev_node.next = new_node
                new_node.next = the_head.next
                new_node.prev = prev_node
                the_head.prev = new_node
            else:
                self.head = new_node
                new_node.next = the_head
                new_node.prev = None
                the_head.prev = new_node
        else:
            raise Exception('Out of range')

    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.prev = None
            return
        the_head = self.head
        self.head = new_node
        new_node.prev = None
        new_node.next = the_head
        the_head.prev = self.head

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.prev = None
            return
        the_head = self.head
        while the_head.next:
            the_head = the_head.next
        the_head.next = new_node
        new_node.prev = the_head

    def print(self):
        the_head = self.head
        while the_head:
            print(the_head.data, end=' -> ')
            the_head = the_head.next
        print('None')

    def print_before(self):
        the_head = self.head
        while the_head.next:
            the_head = the_head.next

        while the_head:
            print(the_head.data, end=' <- ')
            the_head = the_head.prev
        print('None')


dl = DoublyLinkedList()
dl.append(1) 
dl.append(2)
dl.append(3)
dl.append(2)
dl.append(4)
dl.append(1)
dl.append(5)

dl.print()

dl.prepend(0)
dl.print()

dl.append_after_node(6, 0)
dl.print()

dl.delete_a_node(6)
dl.print()

dl.remove_dup()
dl.print()

dl.reverse()
dl.print()

dl.print_before()

