"""
Implement Singly Linked List
"""

class ListNode:
    """
    A node in a singly-linked list.
    """
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    
class SinglyLinkedList:
    def __init__(self):
        """
        Create a new singly-linked list.
        Takes O(1) time.
        """
        self.head = None

    def isEmpty(self):
        return self.head == None

    def append(self, data):
        """
        Insert a new element at the end of the list.
        Takes O(n) time.
        """
        new_node = ListNode(data)
        if self.isEmpty():
            self.head = new_node
            return

        #Looping over all the n elements in the List to the last node
        temp = self.head
        while temp.next:
            temp = temp.next

        #Last element now points to the new element
        temp.next = new_node
        return        

    def find(self, key):
        """
        Search for the first element with `data` matching
        `key`. Return the element or `None` if not found.
        Takes O(n) time.
        """
        temp = self.head

        #Looping over all the elements in the linkedList
        while temp:
            if temp.data == key:
                return temp
            temp = temp.next
        return None
        
    def remove(self, key):
        """
        Remove the first occurrence of `key` in the list.
        Takes O(n) time.
        """
        #When the list is empty
        if self.isEmpty():
            return None
        
        #When only one node is present 
        if self.head.next is None:
            node = self.head
            self.head = None
            return node

        #Taking two pointers, one points to the previous node and one points to current node
        prev = None
        temp = self.head

        while temp:
            if temp.data == key:
                
                prev.next = temp.next
                return temp
            prev = temp
            temp = temp.next
        return None


ll = SinglyLinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.remove(2)