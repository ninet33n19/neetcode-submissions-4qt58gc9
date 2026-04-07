class ListNode:
    def __init__(self, val, next_node = None):
        self.val = val
        self.next = next_node

class LinkedList:
    def __init__(self):
        self.head = ListNode(-1) # dummy node
        self.tail = self.head

    def get(self, index: int):
        curr = self.head.next # as we are ignoring the dummy node at the start
        i = 0
        while curr:
            if i == index:
                return curr.val
            i += 1
            curr = curr.next
        return -1 # the index is out of bounds
    
    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)  # Create a new ListNode object with the given value
        new_node.next = self.head.next  # Set the 'next' attribute of the new node to the current 'next' node of the head
        self.head.next = new_node  # Set the 'next' attribute of the head to the new node, making it the new first node in the linked list

        if not new_node.next:
            # if and only if the list is empty before inserting
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        self.tail.next = ListNode(val=val)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        i = 0
        curr = self.head
        while i < index and curr:
            # move curr to the node before target node
            i += 1
            curr = curr.next

        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
        return False
    
    def getValues(self) -> List[int]:
        curr = self.head.next
        res = []
        
        while curr:
            res.append(curr.val)
            curr = curr.next
        
        return res