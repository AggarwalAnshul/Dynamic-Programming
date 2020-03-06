"""
Reorder List
Asked in:
Amazon
Microsoft
Given a singly linked list

    L: L0 → L1 → … → Ln-1 → Ln,
reorder it to:

    L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → …
You must do this in-place without altering the nodes’ values.

For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}.


[+]Temporal marker           : Fri, 9:31 | Mar 06, 20
[+]Temporal marker untethered: Fri, 10:51 | Mar 06, 20
[+]Comments                  : EASY
[+]Space Complexity          : O(1)
[+]Time Complexity           : O(N)
[+]Level                     : EASY
[+]Tread Speed               : Intermittent
[+]LINK                      : https://www.interviewbit.com/problems/reorder-list
[+] Supplement Sources       : N/A
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        next = self.head
        while not next is None:
            print(next.value, end=" --> ")
            next = next.next

    def insert(self, value, new_value):
        current = self.head
        previous = current
        if current.val == value:
            temp = self.head
            self.head = Node(new_value)
            self.head.next = temp
            current = temp
            previous = self.head

        while not current is None:
            if current.val == value:
                print("inserting the node here...")
                previous.next = Node(new_value)
                previous.next.next = current
                break
            else:
                previous = current
                current = current.next
        print("the new list  is...")
        self.print()


def prints(current):
    current = current
    while current:
        print(str(current.value), end=" -> ")
        current = current.next


# approach:
# navigate to the mid point, reverse the list onward this point
# start a new list and start adding next value from left and right at each time
def reorderList(head):
    # finding the length of the list
    total_length, current_pointer = 0, head
    while current_pointer:
        total_length += 1
        current_pointer = current_pointer.next
    mid_point = (total_length + 1) // 2

    # Find the midPoint
    previous_pointer, current_pointer, length = None, head, 0
    while length < mid_point:
        length += 1
        last_element = current_pointer
        previous_pointer = current_pointer
        current_pointer = current_pointer.next
    mid_point = previous_pointer

    # start the reversal process, current_pointer: midPointer.next
    previous_pointer = None
    while current_pointer:
        length += 1
        temp = current_pointer.next
        current_pointer.next = previous_pointer
        previous_pointer = current_pointer
        if length == total_length:
            mid_point.next = current_pointer
            break
        current_pointer = temp

    # start the operation
    left = head
    right = mid_point.next
    merged = Node(0)  # the new list to be created
    current_pointer = merged
    while left and right:
        temp = left.next
        current_pointer.next = left
        left = temp
        current_pointer = current_pointer.next
        current_pointer.next = None

        temp = right.next
        current_pointer.next = right
        right = temp
        current_pointer = current_pointer.next
        current_pointer.next = None

    if total_length % 2 != 0:
        current_pointer.next = mid_point
        mid_point.next = None
    return merged.next


if __name__ == '__main__':
    lis = [[1],
           [1, 2, 3, 4, 5],
           [12, 6, 75, 98, 58, 81, 30, 101, 87, 40, 70, 45, 41, 20, 66, 1, 96, 35, 51, 79, 61, 48, 99, 11, 32, 88, 60,
            18,
            42, 29, 13, 91, 85, 10, 33, 52, 84, 4, 94, 46, 23, 82, 59, 38, 97, 17, 14, 90, 54, 69, 57, 74, 73, 39]]
    for test_case in lis:
        linkedList = LinkedList()
        print()
        for index in range(len(test_case)):
            if index == 0:
                linkedList.head = Node(test_case[index])
                previous = linkedList.head
            else:
                previous.next = Node(test_case[index])
                previous = previous.next
        linkedList.print()
        print(" |  ", end="")
        current = reorderList(linkedList.head)
        prints(current)
        # linkedList.reverse()
        # linkedList.print()
