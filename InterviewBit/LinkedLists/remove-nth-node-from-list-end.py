"""
Remove Nth Node from List End
Asked in:
HCL
Amazon
Given a linked list, remove the nth node from the end of list and return its head.

For example,
Given linked list: 1->2->3->4->5, and n = 2.
After removing the second node from the end, the linked list becomes 1->2->3->5.

 Note:
If n is greater than the size of the list, remove the first node of the list.
Try doing it using constant additional space.


[+]Temporal marker           : Wed, 17:34 | Mar 04, 20
[+]Temporal marker untethered: Wed, 17:44 | Mar 04, 20
[+]Comments                  : EASY
[+]Space Complexity          : O(1)
[+]Time Complexity           : O(N)
[+]Level                     : EASY
[+]Tread Speed               : PACED
[+]LINK                      : https://www.interviewbit.com/problems/remove-nth-node-from-list-end
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

    # @param head: head of the lis
    # return Head of the modified lis
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
        current = head
        count = 0
        previous = None
        while current:
            count += 1
            if count == n:
                previous.next = current.next
                break
            previous = current
            current = current.next


if __name__ == '__main__':
    lis = [
        [1,2,3,454,6]
    ]
    for test_case in lis:
        for num in range(1, 7):
            linkedList = LinkedList()
            for index in range(len(test_case)):
                if index == 0:
                    linkedList.head = Node(test_case[index])
                    previous = linkedList.head
                else:
                    previous.next = Node(test_case[index])
                    previous = previous.next
            print("\nnum: "+str(num), end = " >> ")
            linkedList.print()
            linkedList.remove_nth_node(linkedList.head, num)
            print("output: ", end = " >> ")
            linkedList.print()
