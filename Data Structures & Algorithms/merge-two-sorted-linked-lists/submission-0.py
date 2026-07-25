# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newList = None
        head = None

        while list1 != None and list2 != None:
            chosen_node = None
            
            if list1.val <= list2.val:
                chosen_node = list1
                list1 = list1.next
            else:
                chosen_node = list2
                list2 = list2.next

            if newList == None:
                newList = chosen_node
                head = newList
            else:
                newList.next = chosen_node
                newList = newList.next
            
        if list1 != None:
            if newList == None:
                head = list1  
            else:
                newList.next = list1
        elif list2 != None:
            if newList == None:
                head = list2  
            else:
                newList.next = list2

        return head