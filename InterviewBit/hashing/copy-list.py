"""
Programming Hashing Copy List
Copy List
Asked in:  
Amazon
Microsoft
A linked list is given such that each node contains an additional random pointer which could point
 to any node in the list or NULL.

Return a deep copy of the list.

Example

Given list

   1 -> 2 -> 3
with random pointers going from

  1 -> 3
  2 -> 1
  3 -> 1
You should return a deep copy of the list. The returned answer should not contain the same node as the original list, but a copy of them. The pointers in the returned list should not link to any node in the original input list.
"""

"""
[+]Temporal marker            :1329 Hours | Monday 06, 2020
[+]Temporal marker Untethered :1343 Hours | Monday 06, 2020
[+]Comments                   : POOR DESCRIPTION / UNABLE TO COMPREHEND, SUSPENDING THE PROBLEM INDEFINITELY
[+]Space Complexity           : O()
[+]Time Complexity            : O()
[+]Level                      : 
[+]Tread Speed                :
[+]LINK                      : https://www.interviewbit.com/problems/copy-list.py
[+] Supplement Sources       : N/A

"""

"""
# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):

"""

class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

def copyRandomList(head):
    hashmap = {}
    current = head
    new_head = RandomListNode(0)
    current_new = new_head
    while current:
        current_new.next = RandomListNode(current_new.label)
        current_new = current_new.next
        first_pointer = current.next
        second_pointer = current.random
        current = current_new.next
    return new_head.next

if __name__ == "__main__":
    test_cases = [


    ]
    for index in range(len(test_cases)):
        test_case = test_cases[index]
        print("input: "+str(input)+"\n\tOUTPUT: :"+str(fourSum(test_case[0], test_case[1])))