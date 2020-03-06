"""
Reverse Link List II
Asked in:
Facebook
Microsoft
Amazon
Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

 Note:
Given m, n satisfy the following condition:
1 ≤ m ≤ n ≤ length of list. Note 2:
Usually the version often seen in the i


[+]Temporal marker           : Fri, 8:18 | Mar 06, 20
[+]Temporal marker untethered: Fri, 8:50 | Mar 06, 20
[+]Comments                  : EASY
[+]Space Complexity          : O(1)
[+]Time Complexity           : O(N)
[+]Level                     : EASY
[+]Tread Speed               : PACED
[+]LINK                      : https://www.interviewbit.com/problems/reverse-link-list-ii
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


# @param head: head pointer of the linked list to be operated upon
# @param start: starting index from where linked list is to be reversed
# @param end: ending index up-to where linked list is to be reversed
# return the head pointer of the linked list
def reverseBetween(head, start, end):
    if start == end:
        return head
    current, length, previous = head, 1, None

    # Go to the starting element
    while length <= start:
        if length == start:
            save_start_pointer = previous
            save_start = current
        previous = current
        current = current.next
        length += 1

    #start operating upon the list
    while length <= end:
        temp = current.next
        current.next = previous
        previous = current
        current = temp
        length += 1
    if start == 1:
        head = previous
    else:
        save_start_pointer.next = previous
    save_start.next = temp
    return head


if __name__ == '__main__':
    lis = [
        [1, 2, 3, 4, 5]
    ]
    for test_case in lis:
        linkedList = LinkedList()
        for index in range(len(test_case)):
            if index == 0:
                linkedList.head = Node(test_case[index])
                previous = linkedList.head
            else:
                previous.next = Node(test_case[index])
                previous = previous.next
        linkedList.print()
        copy = linkedList
        print(" |  ", end="")
        current = reverseBetween(copy.head, 1, 4)
        while current:
            print(str(current.value), end = " -> ")
            current = current.next
        # linkedList.reverse()
        # linkedList.print()
