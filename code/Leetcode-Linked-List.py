class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def list_to_linked_list(self, list):
        the_head_node = ListNode(list[0])
        the_head = the_head_node

        for value in list[1:]:
            the_head.next = ListNode(value)
            the_head = the_head.next

        return the_head_node
    
    def print_list(self, head):
        the_head = head
        while the_head:
            print(the_head.val)
            the_head = the_head.next

    def mergeTwoLists(self, l1, l2):
        dumby = ListNode(0)
        tail = dumby

        while l1 and l2:
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next

            tail = tail.next

        if l1:
            tail.next = l1
            l1 = l1.next
        if l2:
            tail.next = l2
            l2 = l2.next

        return dumby.next

    def deleteDuplicates(self, head):
        the_head = head
        prev_node = None
        dup = {}

        while the_head:
            if the_head.val in dup:
                prev_node.next = the_head.next
                the_head = None
            else:
                dup[the_head.val] = 1
                prev_node = the_head
            the_head = prev_node.next

        return head
    
    def hasCycle(self, head):
        fast, slow = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if slow == fast:
                return True
            
        return False
    
    def getIntersectionNode(self, headA, headB):
        l1, l2 = headA, headB
        if l1 != l2:
            l1 = l1.next if l1 else headB
            l2 - l2.next if l2 else headA
        return l1
    
    def removeElements(self, head, val):
        [1,2,6,3,4,5,6]
        if not head:
            return head
        
        dumby = ListNode(next=head)
        the_head = dumby

        while the_head.next:
            if the_head.next.val == val:
                the_head.next = the_head.next.next
            else:
                the_head = the_head.next

        return dumby.next
    
    def reverseList(self, head):
        if not head:
            return head
        the_head = head
        prev_node = None
        while the_head:
            next_node = the_head.next
            the_head.next = prev_node
            prev_node = the_head
            the_head = next_node

        head = prev_node

    def isPalindrome(self, head):
        if not head:
            return head
        fast, slow = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        prev_node = None
        while slow:
            next_node = slow.next
            slow.next = prev_node
            prev_node = slow
            slow = next_node

        right, left = head, prev_node

        while right:
            if right.val != left.val:
                return False
            left = left.next
            right = right.next

        return True


sol = Solution()

# l1 = sol.list_to_linked_list([1, 2, 4])
# l2 = sol.list_to_linked_list([1, 3, 4])
# print(l1)

# merged_list = sol.mergeTwoLists(l1, l2)
# sol.print_list(merged_list)


# head = [1,1,2]
# ss = sol.list_to_linked_list(head)
# su = sol.deleteDuplicates(ss)
# sol.print_list(su)


# ss = sol.list_to_linked_list()
# sol.hasCycle(ss)

# sol.getIntersectionNode(headA, headB)

# head = [1,2,6,3,4,5,6]
# ss = sol.list_to_linked_list(head)
# val = 6
# sol.removeElements(ss, val)


# ss = sol.list_to_linked_list(head)
# sol.reverseList()

# sol.isPalindrome()



# class LinkedNode:
#     def __init__(self, key):
#         self.key = key
#         self.next = None

# class MyHashSet:
#     def __init__(self):
#         self.set = [LinkedNode(0) for i in range(10**4)]   

#     def add(self, key):
#         the_head = self.set[key % len(self.set)]
#         while the_head.next:
#             if the_head.next.key == key:
#                 return
#             the_head = the_head.next
#         the_head.next = LinkedNode(key)

#     def remove(self, key):
#         the_head = self.set[key % len(self.set)]
#         while the_head.next:
#             if the_head.next.key == key:
#                 the_head.next = the_head.next.next
#                 break 
#             the_head = the_head.next

#     def contains(self, key):
#         the_head = self.set[key % len(self.set)]
#         while the_head.next:
#             if the_head.next.key == key:
#                 return True
#             the_head = the_head.next
#         return False
    


# class MyHashSet(object):
#     def __init__(self):
#         self.map = {}

#     def add(self, key):
#         self.map[key] = 1
        
#     def remove(self, key):
#         if key in self.map:
#             del self.map[key]

#     def contains(self, key):
#         if key in self.map:
#             return True
#         return False
        


# class MyHashMap:
#     def __init__(self):
#         self.map = {}

#     def put(self, key, value):
#         self.map[key] = value

#     def get(self, key):
#         return self.map.get(key, -1)

#     def remove(self, key):
#         if key in self.map:
#             del self.map[key]
        


# class ListNode(object):
#     def __init__(self, val):
#         self.val = val
#         self.next = None

# class Solution(object):
#     def middleNode(self, head):
#         if not head:
#             return None
#         if not head.next:
#             return head
#         if not head.next.next:
#             return head.next
        
#         fast, slow = head, head

#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next

#         return slow


# head = [1,2,3,4,5,6]
# head = [1,2,3,4,5]

