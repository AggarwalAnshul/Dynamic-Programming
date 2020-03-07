"""
Partition List
Asked in:
Microsoft
Given a linked list and a value x, partition it such that all nodes less than x come
before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.


[+]Temporal marker           : Sat, 11:41 | Mar 07, 20
[+]Temporal marker untethered: Sat, 11:51 Mar 07, 20
[+]Comments                  : SUPER EASY
[+]Space Complexity          : O(1)
[+]Time Complexity           : O(N)
[+]Level                     : EASY
[+]Tread Speed               : PACED
[+]LINK                      : https://www.interviewbit.com/problems/partition-list
[+] Supplement Sources       : N/A
"""


class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None


def print_linked_list(head):
    current = head
    while current:
        print(str(current.val), end=" -> ")
        current = current.next
    print("\n")


# @parameter head: head of the linked list
# return Manipulated linked list as per the aforementioned problem statement
def partition(head, x):
    current = head
    left_partition = ListNode(0)
    save_left = left_partition
    right_partition = ListNode(0)
    save_right = right_partition

    while current:
        temp = current.next

        if current.val < x:
            left_partition.next = current
            left_partition = left_partition.next
            left_partition.next = None
        else:
            right_partition.next = current
            right_partition = right_partition.next
            right_partition.next = None
        current = temp
    left_partition.next = save_right.next
    return save_left.next


if __name__ == '__main__':
    lis = [
        [[1, 4, 3, 2, 5, 2], 3]
    ]

    for test_case in lis:
        one = ListNode(0)
        one_head = one
        for index in range(len(test_case[0])):
            one.next = ListNode(test_case[0][index])
            one = one.next
        one_head = one_head.next
        print("input: ", end=" >> ")
        print_linked_list(one_head)
        print_linked_list(partition(one_head, test_case[1]))
