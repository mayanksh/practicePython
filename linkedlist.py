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

        # linked list Traversal(print any given list)
        #this function prints the contents of linked list
        #starting from head
    def printList(self):
        temp= self.head
        while (temp):
            print (temp.data,  end=" ")   #, end=" " is used to print out put in same line
            temp = temp.next


#creating simple Linked List with 3 nodes

#code Execution

if __name__== '__main__' :     #it will assign hard coded string '__main__' to the __name__ variable(it's a special variable)
    firstlist = LinkedList()    #start with empty list

    firstlist.head=Node(1)
    second= Node(2)
    third = Node(3)     #3 Nodes have been created. Head,second and third

    firstlist.head.next = second;
    second.next= third;


    firstlist.printList()

