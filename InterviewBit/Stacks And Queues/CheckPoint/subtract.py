'''
Programming Checkpoint: Level 4 Subtract
SUBTRACT
Given a singly linked list, modify the value of first half nodes such that :

1st node’s new value = the last node’s value - first node’s current value
2nd node’s new value = the second last node’s value - 2nd node’s current value,
and so on …

 NOTE :
If the length L of linked list is odd, then the first half implies at first floor(L/2) nodes.
So, if L = 5, the first half refers to first 2 nodes.
If the length L of linked list is even, then the first half implies at first L/2 nodes. So,
 if L = 4, the first half refers to first 2 nodes.
Example :

Given linked list 1 -> 2 -> 3 -> 4 -> 5,

You should return 4 -> 2 -> 3 -> 4 -> 5
as

for first node, 5 - 1 = 4
for second node, 4 - 2 = 2
Try to solve the problem using constant extra space.

[+]Temporal marker           : 13:03 Hours | Sunday 22, 2020
[+]Temporal marker untethered: 13:40 Hours | Sunday 22, 2020
[+]Comments                  :
[+]Space Complexity          : O()
[+]Time Complexity           : O()
[+]Level                     :
[+]Tread Speed               :
[+]LINK                      : https://www.interviewbit.com/problems/nearest-smaller-element
[+] Supplement Sources       : N/A

'''

class ListNode:
    def __init__(self, val):
        self.value = val
        self.next = None

def print_Linked_List(head):
    current = head
    while current:
        print(current.value, end = " -> ")
        current = current.next
    print("\n")


# ACCEPTED!
# Approach:
#     Find the middle half using floyd's cycle detection algorithm O(N/2)
#     Split the second half of linked list & reverse it O(N/2)
#     Operate on first half by traversing simultaneously both halves O(N/2)
#     reverse the second half O(N/2)
#     append first & second half O(1)
#     return the head
# Time: O(2N) | Space: O(1)
def subtract(head):

    # Function to reverse a linked list
    # @param head : head of the linked list to be reversed
    # @return the head of the reversed linked list
    def reverse_linked_list(head):
        current, previous = head, None
        while current:
            temp = current.next
            current.next = previous
            previous = current
            current = temp
        return previous

    #find the middle element and split list into two halves
    slow, fast = head, head
    while slow and fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    second_half = slow.next # Declare the second half
    slow.next = None        # split the first and second half

    # reversing the second half
    second_half = reverse_linked_list(second_half)

    #Operating the list
    current_first, current_second = head, second_half
    while current_first and current_second:
        new_value = current_second.value - current_first.value
        current_first.value = new_value
        if not current_second.next:
            temp = reverse_linked_list(second_half)
            slow.next = temp
            return head
        current_first, current_second = current_first.next, current_second.next


if __name__ == '__main__':

    test_cases = [
        [3, 2],
        [1 , 2 , 3 , 4 , 5],
        [1, 2, 3, 4],
        [ 95 , 59 , 26 , 16 , 31 , 39 , 29 , 8 , 74 , 14 , 41 , 41 , 64 , 88 , 34 , 21 , 67 , 23 , 17 , 41 , 3 , 38 , 4 , 45 , 93 , 92 , 99 , 24 ]
        ]

    for test_case in test_cases:
        Linked_list = ListNode(0)
        next_Node = Linked_list
        for node in test_case:
            next_Node.next = ListNode(node)
            next_Node = next_Node.next
        print("Input: ", end = " >> ")
        print_Linked_List(Linked_list.next)
        print("\tOutput: ", end = " >> ")
        print_Linked_List( subtract(Linked_list.next) )
