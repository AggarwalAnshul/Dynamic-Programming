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
    def merges(self, one, two):
        one_head = one.head
        two_head = two.head
        merged_head = self.head
        merged_current = self.head
        while one.head or two.head:
            if one.head and two.head:
                #print("both one & two | one: "+str(one.head.value)+" two: >> "+str(two.head.value))
                if one.head.value < two.head.value:
                    #print("\tchoosing one form both...")
                    temp = one.head.next
                    if merged.head is None:
                        self.head = one.head
                        merged_current = self.head
                    else:
                        merged_current.next = one.head
                        merged_current = merged_current.next
                    one.head.next = None
                    one.head = temp
                    #print("oneHead is now: "+str(one.head.value))
                else:
                    #print("\tchoosing two from both...")
                    temp = two.head.next
                    if merged.head is None:
                        self.head = two.head
                        merged_current = self.head
                    else:
                        merged_current.next = two.head
                        merged_current = merged_current.next
                    two.head.next = None
                    two.head = temp
                    #print("twohead is now: "+str(two.head.value))
            elif two.head:
                #print("only two...")
                merged_current.next = two.head
                two.head = None
            else:
                #print("only one...")
                merged_current.next = one.head
                one.head = None
            #print("merged: >> "+str(self.print()))
        print("merging is complete...")
        self.print()
    def merge(self, one_head, two_head):
        current = None
        while one_head or two_head:
            if one_head and two_head:
                if one_head.val < two_head.val:
                    temp = one_head.next
                    if current is None:
                        self.head = one_head
                        current = self.head
                    else:
                        current.next = one_head
                        current = current.next
                    one_head.next = None
                    one_head = temp
                else:
                    temp = two_head.next
                    if current is None:
                        self.head = two_head
                        current = self.head
                    else:
                        current.next = two_head
                        current = current.next
                    two_head.next = None
                    two_head = temp
            elif two_head:
                current.next = two_head
                two_head = None
            else:
                current.next = one_head
                one_head = None
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
