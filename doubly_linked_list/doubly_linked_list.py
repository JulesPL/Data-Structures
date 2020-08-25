"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        new_node = ListNode(value)
        if self.length == 0:
          self.head = self.tail = new_node
        else:
          new_node.next = self.head
          self.head.prev = new_node
          self.head = new_node
        self.length += 1
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if self.length >= 1:
          value = self.head.value
          if self.length == 1:
            self.head = self.tail = None
          else:
            self.head.next.prev = None
            self.head = self.head.next
          self.length -= 1
          return value
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_node = ListNode(value)
        if self.length == 0:
          self.head = self.tail = new_node
        else:
          new_node.prev = self.tail
          self.tail.next = new_node
          self.tail = new_node
        self.length += 1
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if self.length >= 1:
          value = self.tail.value
          if self.length == 1:
            self.head = self.tail = None
          else:
            self.tail.prev.next = None
            self.tail = self.tail.prev
          self.length -= 1
          return value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if self.length > 1:
          prev_node = node.prev
          next_node = node.next
          
          if prev_node:
            prev_node.next = next_node
          else:
            self.head = next_node
          if next_node:
            next_node.prev = prev_node
          else:
            self.tail = prev_node

          node.prev = None
          node.next = self.head if node != self.head else self.head.next
          self.head = node

        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if self.length > 1:
          prev_node = node.prev
          next_node = node.next

          if prev_node:
            prev_node.next = next_node
          else:
            self.head = next_node
          if next_node:
            next_node.prev = prev_node
          else:
            self.tail = prev_node

          node.next = None
          if node != self.tail:
            node.prev = self.tail
            self.tail.next = node
          else:
            node.prev = self.tail.prev
          self.tail = node

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        prev_node = node.prev
        next_node = node.next
        if prev_node:
          prev_node.next = next_node
        else:
          self.head = next_node
        if next_node:
          next_node.prev = prev_node
        else:
          self.tail = prev_node
        self.length -= 1

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        node  = self.head
        value = -999999999999
        for i in range(self.length):
          if node.value > value:
            value = node.value
          node = node.next
        return value