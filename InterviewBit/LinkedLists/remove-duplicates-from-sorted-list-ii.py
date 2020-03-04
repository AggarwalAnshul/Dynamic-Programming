"""
Remove Duplicates from Sorted List II
Asked in:
Microsoft
VMWare
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only
 distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.

[+]Temporal marker           : Mon, 16:0 | Mar 02, 20
[+]Temporal marker untethered: Wed, 14:51 | Mar 04, 20
[+]Comments                  : Laid it for the next day
                                Yesterday too worked out to code
                                Solved today in around 30-40 Mins
                                approach was clear to me
[+]Space Complexity          : O(1)
[+]Time Complexity           : O(N)
[+]Level                     : EASY
[+]Tread Speed               : Realxed
[+]LINK                      : https://www.interviewbit.com/problems/remove-duplicates-from-sorted-list-ii
[+] Supplement Sources       : N/A
"""


class Node:
    def __init__(self, val):
        self.next = None
        self.val = val


class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        head = self.head
        current = head
        while current:
            print(str(current.val), end=" -> ")
            current = current.next

    def removeDuplicates(self):
        unique_head = Node(0)
        unique_current = unique_head
        current = self.head
        while current:
            # print("\tcurrent: "+str(current.val))
            temp = current
            if temp.next and temp.val == temp.next.val:
                while temp.next and temp.val == temp.next.val:
                    temp = temp.next
                current = temp.next
            else:
                # print("\t\tadding this to new list...")
                temp = current.next
                unique_current.next = current
                unique_current = unique_current.next
                current.next = None
                current = temp
        current = unique_head.next
        while current:
            print(str(current.val), end=" -> ")
            current = current.next


if __name__ == '__main__':
    lis = [["a"]
        , ["a", "a", "a"]
        , ["a", "b", "b", "f"]
        , ["a", "b", "c", "c", "c", "e", "a"]
        , [1, 2, 1]
        , [1, 1]
        , [1, 2, 2, 1]
        , ["a", "b", "b", "a"]
        , ["a", "a"]
        , [1, 8]
        , [2, 2],
           [1, 2, 2, 1],
           [1, 2, 3, 4]]
    for test_case in lis:
        linkedList = LinkedList()
        for index in range(len(test_case)):
            if index == 0:
                linkedList.head = Node(test_case[index])
                previous = linkedList.head
            else:
                previous.next = Node(test_case[index])
                previous = previous.next
        print("input: >> ", end=" ")
        linkedList.print()
        print(" Output: >> ", end=" ")
        linkedList.removeDuplicates()
        print("\n\t")
