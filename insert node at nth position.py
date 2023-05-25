# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 18:28:08 2023

@author: varsh
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
l1 = [9,9,9,9,9,9,6]

def createLinkedList(lst):
    head = None
    for val in reversed(lst):
        head = ListNode(val, head)
    return head

l1 = createLinkedList(l1)

        
def insertNodeAtPosition(head, data, position):
    # create a new node
    new = ListNode(data)
    # set a pointer to head in case our initial position is not 0
    pointer = head
    # set our counter so we can traverse through SLL
    counter = 1
    # if our given position is 0
    if position == 0:
        # our new node will point to the head
        new.next = head
        # now head will point to the new node
        head = new
        # we then return head as requested
        return head
    # while the next node away from the head node is not None
    while pointer.next is not None:
        # and if our counter is equal to the position given
        if counter == position:
            # our new node will point to pointer.next
            new.next = pointer.next
            # and our pointer.next will be equal to our new node
            pointer.next = new
            break
        # we traverse the list one position at a time until counter 
        # == position
        counter += 1
        pointer = pointer.next
    # we return the head as requested
    return head

val = insertNodeAtPosition(head=l1, data=3, position=2)
curr = val
values = []
while curr:
    values.append(str(curr.val))
    curr = curr.next
print(" ".join(values))


def removenode(head,position):
   
    curr = head
    
    if position == 0:
        curr.next = head
        return head
    
    i = 0
    while curr is not None:
        print('current',curr.val)
        print('i',i)
        if i == position-1:
            curr.next = curr.next.next
        else:
            curr = curr.next
        i +=1

          
    return head
   
position = 2
lst = removenode(val,position)

curr = lst
values = []
while curr:
    values.append(str(curr.val))
    curr = curr.next
print(" ".join(values))

