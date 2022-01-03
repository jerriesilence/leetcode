# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # digit by digit add
        current_digit = l1.val
        l1 = l1.next
        
        current_digit += l2.val
        l2 = l2.next
        
        plus_one = False
        
        if current_digit > 9:
            result = tail = ListNode(current_digit-10)
            plus_one = True
        else:
            result = tail = ListNode(current_digit)
        
        
        while l1 or l2:
            
            current_digit = 0
            
            if l1:
                current_digit = l1.val
                l1 = l1.next
                
            if l2:
                current_digit += l2.val
                l2 = l2.next
            
            if plus_one:
                current_digit += 1
                plus_one = False
                
            if current_digit > 9:
                tail.next = ListNode(current_digit-10)
                plus_one = True
            else:
                tail.next = ListNode(current_digit)
            
            tail = tail.next
            
        if plus_one:
            tail.next = ListNode(1)
            
        return result
