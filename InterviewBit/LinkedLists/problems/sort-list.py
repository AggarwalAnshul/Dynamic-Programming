"""

Programming Linked Lists Sort List
Sort List
Asked in:
Google
Sort a linked list in O(n log n) time using constant space complexity.

Example :

Input : 1 , 5 , 4 , 3

Returned list : 1 , 3 , 4 , 5

[+]Temporal marker           : Tue, 14:17 | Mar 17, 20
[+]Temporal marker untethered: Tue, 18:00 | Mar 17, 20
[+]Comments                  : Pretty complex problem
                                Learned Merged sort to solve this problem
                                Execution was a bit tricky, but i got this.
                                Entire implementation is mine
                                breakthrough was when i cold pressed the technique
[+]Space Complexity          : O(1)
[+]Time Complexity           : O(N logN)
[+]Level                     : MEDIUM
[+]Tread Speed               : Relaxed
[+]LINK                      : https://www.interviewbit.com/problems/sort-list
[+] Supplement Sources       : N/A
"""


class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None


def print_linked_list(head):
    current = head
    while current:
        print(str(current.val), end=" , ")
        current = current.next
    print("\n")


# ACCEPTED!
# @param A : head node of linked list
# @return the head node in the linked list
def sortList(head):
    if head.next:
        # find the middle point
        slow = head
        fast = head
        while slow.next and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        left, right, slow.next = head, slow.next, None
        left = sortList(left)
        right = sortList(right)

        # merging back the split sub-arrays
        merged_head = ListNode(0)
        saved_head = merged_head
        while left and right:
            if left.val <= right.val:
                saved_head.next = left
                left = left.next
            else:
                saved_head.next = right
                right = right.next
            saved_head = saved_head.next
            saved_head.next = None
        if left:
            saved_head.next = left
        if right:
            saved_head.next = right

        return merged_head.next
    return head


if __name__ == '__main__':
    lis = [
        [[1, 4, 3, 2, 5, 2], 3],
        [[1], 1],
        [[1, 78, 4, 5, 67, 23, 5, 3, 2, 7, 9, 6], 2],
        [[5, 66, 68, 42, 73, 25, 84, 63, 72, 20, 77, 38, 8, 99, 92, 49, 74, 45, 30, 51,
          50, 95, 56, 19, 31, 26, 98, 67, 100, 2, 24, 6, 37, 69, 11, 16, 61, 23, 78, 27,
          64, 87, 3, 85, 55, 22, 33, 62]]
    ]

    for x in range(len(lis)):
        test_case = lis[x]
        one = ListNode(0)
        one_head = one
        for index in range(len(test_case[0])):
            one.next = ListNode(test_case[0][index])
            one = one.next
        one_head = one_head.next
        print("input: ", end=" >> ")
        print_linked_list(one_head)
        print("output: ", end=" >> ")

        print_linked_list(sortList(one_head))
