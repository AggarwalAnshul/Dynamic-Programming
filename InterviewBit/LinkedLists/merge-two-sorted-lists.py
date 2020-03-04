"""
Merge Two Sorted Lists
Asked in:
Microsoft
Yahoo
Amazon
Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists, and should also be sorted.

For example, given following linked lists :

  5 -> 8 -> 20
  4 -> 11 -> 15
The merged list should be :

4 -> 5 -> 8 -> 11 -> 15 -> 20

[+]Temporal marker           : Mon, 17:43 | Mar 02, 20
[+]Temporal marker untethered: Wed, 11:26 | Mar 04, 20
[+]Comments                  : Took a whole lot of time on Monday. Dropped after an hours
                                Yesterday I was too worked out to code
                                Today code this in an hour. approach was clear in my mind.
                                This matter is finally closed now!
[+]Space Complexity          : O(N)
[+]Time Complexity           : O(N)
[+]Level                     : EASY
[+]Tread Speed               : Relaxed
[+]LINK                      : https://www.interviewbit.com/problems/new
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
        count = 0
        while current:
            count += 1
            print(str(current.val), end=" -> ")
            current = current.next
        print("total elements: "+str(count))

    # @param one_head : head of first sorted linked List
    # @param two_head: head of second sorted linked list
    # @return the head of the merged sorted list
    # This iteration is much more optimized & efficient
    def merge(self, one_head, two_head):
        current = Node(0)
        save = current
        while one_head and two_head:
            if one_head.val < two_head.val:
                current.next = one_head
                one_head = one_head.next
            else:
                current.next = two_head
                two_head = two_head.next
            current = current.next
        if two_head:
            current.next = two_head
            two_head = None
        if one_head:
            current.next = one_head
            one_head = None
        self.head = save.next
        self.print()





if __name__ == '__main__':
    lis = [[[5, 8, 20], [4, 11, 15]]]
    for test_case in lis:
        one = LinkedList()
        two = LinkedList()
        for index in range(len(test_case[0])):
            if index == 0:
                one.head = Node(test_case[0][index])
                previous = one.head
            else:
                previous.next = Node(test_case[0][index])
                previous = previous.next
        for index in range(len(test_case[1])):
            if index == 0:
                two.head = Node(test_case[1][index])
                previous = two.head
            else:
                previous.next = Node(test_case[1][index])
                previous = previous.next

        one.print()
        print(" >> two",end=" " )
        two.print()
        print("\nMERGING>>>")
        merged = LinkedList()
        merged.merge(one.head, two.head)
        print("\nmerged: >> ")
        # linkedList.reverse()
        # linkedList.print()
