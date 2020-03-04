"""

Programming Linked Lists Rotate List
Rotate List
Asked in:
Amazon
Given a list, rotate the list to the right by k places, where k is non-negative.

For example:

Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.

[+]Temporal marker           : Wed, 18:14 | Mar 04, 20
[+]Temporal marker untethered: Wed, 18:54 | Mar 04, 20
[+]Comments                  : EASY
[+]Space Complexity          : O(1)
[+]Time Complexity           : O(N)
[+]Level                     : EASY
[+]Tread Speed               : Relaxed
[+]LINK                      : https://www.interviewbit.com/problems/rotate-list
[+] Supplement Sources       : N/A
"""


class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        current = self.head
        while current:
            print(str(current.val), end=" -> ")
            current = current.next

    def remove_nth_node(self, head, n):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        if n + 1 >= count:
            self.head = self.head.next
            return
        n = count - n + 1
        current, count, previous = head, 0, None
        while current:
            count += 1
            if count == n:
                previous.next = current.next
                break
            previous, current = current, current.next
        current = head
        while current:
            print(str(current.val), end=" - > ")
            current = current.next


# @param head: head of the LinkedList to be rotated
# return head of the rotated list
def rotate_the_lis(head, offset):
    # finding the length of the linked list
    current, length, last_node = head, 0, None
    while current:
        last_node = current
        length += 1
        current = current.next

    offset %= length
    offset = length - offset
    if offset == length:
        return head

    # rotating the array
    current, new_head, count = head, None, 0
    while current:
        count += 1
        if count == offset:
            new_head = current.next
            current.next = None
            current = new_head
            last_node.next = head
            return new_head
        current = current.next


if __name__ == "__main__":
    lis = [
        [1, 2, 3, 4, 6],
        [68, 86, 36, 16, 5, 75]
    ]
    for test_case in lis:
        for num in range(1, len(test_case)+2):
            linkedList = LinkedList()
            for index in range(len(test_case)):
                if index == 0:
                    linkedList.head = Node(test_case[index])
                    previous = linkedList.head
                else:
                    previous.next = Node(test_case[index])
                    previous = previous.next
            print("\nnum: " + str(num), end="|| ")
            linkedList.print()
            print("| output: >> ", end="")
            current = rotate_the_lis(linkedList.head, num)
            while current:
                print(str(current.val), end = " - > ")
                current = current.next