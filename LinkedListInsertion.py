#make a node class
class Node:

    #function to initialize node object
    def __init__(self,data):
        self.data=data
        self.next=None #initialize next as null

class LinkedList:

    #initialize linkedlist object
    def __init__(self):
        self.head=None

#insertion of new node at beginning
# Time complexity of push() is O(1) as it does constant amount of work.

    def push (self, new_data):
        #Allocate the Node & Put in the data
        new_node= Node(new_data)
        #make next of new node as head
        new_node.next = self.head
        #move head to point the new node
        self.head = new_node


# This function is in LinkedList class. Inserts a
    # new node after the given prev_node
    def insertAfter(self, prev_node, new_data):

        #check if the prev_node exists
        if prev_node is None:
            print ("the previvious node must be in linked list")
            return

        #create new node and add data
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node
#Time complexity of insertAfter() is O(1) as it does constant amount of work.

    #This function is defined in Linked List class
    # Appends a new node at the end
    def append(self, new_data):


# 1. Create a new node
# 2. Put in the data
# 3. Set next as None
        new_node= Node(new_data)
        #4. check if linked list is empty then make new node as head
        if self.head is None:
            self.head= new_node
            return
        #5 traverse till last node
        last= self.head
        while (last.next):
            last =last.next
            # 6. Change the next of last node
        last.next = new_node

#Time complexity of append is O(n) where n is the number of nodes in linked list. Since there is a loop from head to end, the function does O(n) work

    # Utility function to print the linked list
    def printList(self):
        temp = self.head
        while (temp):
            print temp.data,
            temp = temp.next


# Code execution starts here
if __name__ == '__main__':
    # Start with the empty list
    llist = LinkedList()

    # Insert 6.  So linked list becomes 6->None
    llist.append(6)

    # Insert 7 at the beginning. So linked list becomes 7->6->None
    llist.push(7);

    # Insert 1 at the beginning. So linked list becomes 1->7->6->None
    llist.push(1);

    # Insert 4 at the end. So linked list becomes 1->7->6->4->None
    llist.append(4)

    # Insert 8, after 7. So linked list becomes 1 -> 7-> 8-> 6-> 4-> None
    llist.insertAfter(llist.head.next, 8)

    print
    'Created linked list is:',
    llist.printList()