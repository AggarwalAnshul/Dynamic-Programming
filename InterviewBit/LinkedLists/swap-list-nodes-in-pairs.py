"""
Swap List Nodes in pairs
Asked in:
Microsoft
Amazon
Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the
 values in the list, only nodes itself can be changed.


[+]Temporal marker           : Sat, 7:22 | Mar 07, 20
[+]Temporal marker untethered: Sat, 7:35 | Mar 07, 20
[+]Comments                  : EASY
[+]Space Complexity          : O(1)
[+]Time Complexity           : O(N)
[+]Level                     : EASY
[+]Tread Speed               : PACED
[+]LINK                      : https://www.interviewbit.com/problems/swap-list-nodes-in-pairs
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


def print_linked_lis(head):
    current = head
    while current:
        print(str(current.value), end=" -> ")
        current = current.next
    print("\n")


def swapPairs(head):
    merged = Node(0)
    save = merged
    previous, current = None, head
    count = 0
    while current:
        count += 1
        if count == 1:
            pair_head = current
        temp = current.next
        current.next = previous
        previous = current
        current = temp
        if count == 2:
            save.next = previous
            count = 0
            save = pair_head
            save.next = None
    # when the list have odd number of nodes
    if count == 1:
        save.next = previous
        save.next.next = None
    return merged.next

if __name__ == '__main__':
    lis = [[1,2,3,4,5,6]]
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
        print(" |  ", end = "")
        print_linked_lis( swapPairs(linkedList.head) )