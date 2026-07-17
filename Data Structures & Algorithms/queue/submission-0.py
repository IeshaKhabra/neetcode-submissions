class Node:
    def __init__(self,value):
        self.value = value
        self.prev = None
        self.next = None

class Deque:
    
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self) -> bool:
        return self.head is None

    def append(self, value: int) -> None: # adds to the right
        # create new node
        new_node = Node(value)

        # if deque is empty then new node becomes both first and last node
        if self.isEmpty():
            self.head = new_node
            self.tail = new_node
            return
        else:
            # new node will come after the current tail
            # so its prev node is the current tail 
            new_node.prev = self.tail

            # connect current tail to new node
            self.tail.next = new_node

            # update tail so it points to new final node
            self.tail = new_node


    def appendleft(self, value: int) -> None:
        new_node = Node(value)
        if self.isEmpty():
            self.head = new_node
            self.tail = new_node
            return
        # new node comes before the current head 
        # so its next node is the current head
        new_node.next = self.head

        # connect the current head back to the new node
        self.head.prev = new_node

        # update head to point to new first
        self.head = new_node

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        
        # set the value before removing the tail node
        removed_value = self.tail.value

        # if head and tail are the same node
        # there is only one node in the deque 
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return removed_value

        # move tail to previous node
        self.tail = self.tail.prev

        self.tail.next = None

        return removed_value

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        
        removed_value = self.head.value
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return removed_value

        # move head to next node
        self.head = self.head.next

        # new head should not point back to the removed node
        self.head.prev = None
        return removed_value


"""
double ended queue also known as deque
    allows us insertion and deletion from both ends
    original queue follows fifo 
    deque follows
        appendLeft()
        append() from right
        pop() from right
        popLeft() 
        isEmpty() 
    all of these need to be O(1)

in doubly linked list
value, next, prev
head, tail



"""
        
