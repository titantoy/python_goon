# -*- coding: utf-8 -*-

class Node:#create a Node
    data='o'
    def __init__(self):
#        self.data=data#given data
        self.next=None#given next to None
        
        
class Linked_List:
    def __init__(self):
        pass
#    
    def insert_tail(self, Head,data):
        if(Head.next is None):
            Head.next = Node()
            Head.next.data = data
        else:
            self.insert_tail(Head.next, data)

    def insert_head(self, Head,data):
        tamp = Head
        if (tamp == None):
            newNod = Node()#create a new Node
            newNod.data = data
            newNod.next = None
            Head = newNod#make new node to Head       
        else:
            newNod = Node()
            newNod.data = data
            newNod.next = Head#put the Head at NewNode Next
            Head=newNod#make a NewNode to Head
        return Head   
    
    def printList(self, Head):#print every node data
        tamp=Head
      
        while tamp!=None:
            print("enter while:")
            print(tamp.data)
            tamp=tamp.next
    
    def delete_head(self, Head):#delete from head
        if Head!=None:
            Head=Head.next
        return Head#return new Head
    
    def delete_tail(self, Head):#delete from tail
        if Head!=None:
            tamp = Node()
            tamp = Head
            while (tamp.next).next!= None:#find the 2nd last element
                tamp = tamp.next
            tamp.next=None#delete the last element by give next None to 2nd last Element
        return Head

    def isEmpty(self, Head):
        return Head is None #Return if Head is none
    
    def reverse(self, Head):
        prev = None
        current = Head
        
        while(current):
            # Store the current node's next node. 
            next_node = current.next
            # Make the current node's next point backwards
            current.next = prev
            # Make the previous node be the current node
            prev = current
            # Make the current node the next node (to progress iteration)
            current = next_node
        # Return prev in order to put the head at the end 
#        Head = prev
        return prev

plist=Linked_List()
#phead = Node()
phead = plist.insert_head(None, 'oui')
print(phead.data)
plist.insert_tail(phead, "good")
plist.insert_tail(phead, 'no one live')
#plist.insert_tail(phead, "get")
plist.printList(phead)
print(plist.isEmpty(phead))
#phead = plist.delete_head(phead)
#plist.printList(phead)
phead=plist.reverse(phead)
plist.printList(phead)


