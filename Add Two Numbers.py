# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 21:39:12 2023

@author: varsh
"""
Add Two Numbers
l1 = [2,4,3]
l2 = [5,6,4]
#l1 = l1[::-1]
#l2 = l2[::-1]

9 9 9 9 9 9 9
9 9 9 9
------------------
8 9 9 9 0 0 0 1

l1 = [9,9,9,9,9,9,6]
l2 = [9,9,9,8]

## list to link list
#l1=[2,4,3]
def createLinkedList(lst):
    head = None
    for val in reversed(lst):
        head = ListNode(val, head)
    return head

l1 = createLinkedList(l1)
l2 = createLinkedList(l2)
print(l1)

## reverse link list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
#https://www.google.com/search?q=reverse+linked+list+python&sxsrf=AJOqlzUdXSt0Eg3y2iobbjQFiq6M4TeB7Q%3A1674433821106&source=hp&ei=HdXNY8aKBKTk5NoP_cWbqAg&iflsig=AK50M_UAAAAAY83jLduuyfx5PiNQLpWAbZFKEp4VqPZ6&ved=0ahUKEwiGjeuIuNz8AhUkMlkFHf3iBoUQ4dUDCAs&uact=5&oq=reverse+linked+list+python&gs_lcp=Cgdnd3Mtd2l6EAMyBAgjECcyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgkIABAWEB4Q8QQyBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjoHCCMQ6gIQJzoLCC4QgAQQsQMQgwE6EQguEIAEELEDEIMBEMcBENEDOggIABCxAxCDAToECAAQQzoOCC4QgAQQsQMQxwEQ0QM6CggAELEDEIMBEEM6EQguEIMBEMcBELEDENEDEIAEOgsIABCABBCxAxCDAToLCC4QgAQQxwEQ0QM6CwguEIAEEMcBEK8BOgUILhCABDoFCAAQkQI6CAgAEIAEELEDOggILhCABBDUAjoNCAAQgAQQFBCHAhCxAzoHCAAQsQMQQzoKCAAQgAQQFBCHAjoKCAAQgAQQsQMQClDUA1jIYmCwZGgJcAB4AIABbYgBtxSSAQQzMi4ymAEAoAEBsAEK&sclient=gws-wiz#fpstate=ive&vld=cid:5a75fbcd,vid:G0_I-ZF0S38
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
         if head == None or head.next == None:
            return head
         prev, curr = None, head
         print(curr.val)
         while curr:
               next_node = curr.next
               curr.next = prev
               prev = curr
               curr = next_node
         return prev

o = Solution()
lst = o.reverseList(l1)
#reverse pointers


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode()
        curr = head
        #print(curr.val)
        carry = 0
        
        while l1 or l2:
            print(curr.val)
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            s = x + y + carry
            carry = s // 10
            curr.next = ListNode(s % 10)
            curr = curr.next
            if l1:
                l1 = l1.next  
            if l2:
                l2 = l2.next
        
        if carry > 0:
            curr.next = ListNode(carry)
        
        return head.next
o = Solution()
res = o.addTwoNumbers(l1,l2)
print(res)


curr = res
values = []
while curr:
    values.append(str(curr.val))
    curr = curr.next
print(" ".join(values))



result = ""
i = 0
temp = 0
while i < max(len(l1),len(l2)):
    x = int(l1[i]) if i < len(l1) else 0
    y = int(l2[i]) if i < len(l2) else 0
    s = x+y+temp
    print('s:',s)
    result += str(s % 10)
    temp = s // 10
    i += 1
if temp > 0:
    result += str(temp)
    print(result[::-1])      
print(result[::-1])