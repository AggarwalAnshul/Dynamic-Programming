"""
Remove Duplicates from Sorted List
Asked in:
Microsoft
VMWare
Add to bookmarks (can be accessed from dashboard)
Suggest edits in problem statement.
Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.

[+]Temporal marker           : Mon, 14:17 | Mar 02, 20
[+]Temporal marker untethered: Mon, 14:27 | Mar 02, 20
[+]Comments                  : EASY
[+]Space Complexity          : O(1)
[+]Time Complexity           : O(N)
[+]Level                     : EASY
[+]Tread Speed               : PACED
[+]LINK                      : https://www.interviewbit.com/problems/remove-duplicates-from-sorted-list
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

    def removeDuplicates(self):
        head = self.head
        current = head.next
        previous = head
        while current is not None:
            #print("current: "+str(current.value))
            if current.value == previous.value:
                previous.next = current.next
                temp = current.next
                current.next = None
                current = temp
            else:
                previous = current
                current = current.next


if __name__ == '__main__':
    lis = [["a", "b", "c", "d", "c", "b", "a"]
        , ["a", "b", "a", "d", "s", "e", "a"]
        , ["a"]
        , ["a", "a", "a"]
        , ["a", "b", "b", "a"]
        , ["a", "b", "c", "d", "c", "b", "a"]
        , [1, 2, 1]
        , [1, 1]
        , [1, 2, 1]
        , [1, 2, 2, 1]
        , ["a", "b", "b", "a"]
        , ["a", "a"]
        , [1, 8]
        , [2, 2],
           [1,2,2,1],
           [1,2,3,4],
           [1,1,2,3,3]]
    for test_case in lis:
        linkedList = LinkedList()
        for index in range(len(test_case)):
            if index == 0:
                linkedList.head = Node(test_case[index])
                previous = linkedList.head
            else:
                previous.next = Node(test_case[index])
                previous = previous.next
        print("input: ",end = " >> ")
        linkedList.print()
        linkedList.removeDuplicates()
        print("output: ",end = " >>" )
        linkedList.print()
        print("\n")


