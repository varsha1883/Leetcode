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

