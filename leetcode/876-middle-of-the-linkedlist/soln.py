# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #assign temporary header
        tempHead = head

        noel = 0

        while tempHead is not None:
            noel += 1
            tempHead = tempHead.next
        
        for i in range(noel/2):
            head = head.next
        
        return head
