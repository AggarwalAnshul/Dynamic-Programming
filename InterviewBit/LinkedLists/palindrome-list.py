"""
Programming Linked Lists Palindrome List
Palindrome List
Asked in:
Amazon
Microsoft
Given a singly linked list, determine if its a palindrome. Return 1 or 0 denoting i
f its a palindrome or not, respectively.

Notes:

Expected solution is linear in time and constant in space.
For example,

List 1-->2-->1 is a palindrome.
List 1-->2-->3 is not a palindrome.


[+]Temporal marker           : Sun, 17:28 | Mar 01, 20
[+]Temporal marker untethered: Sun, 10:09 | Mar 02, 20
[+]Comments                  :
[+]Space Complexity          : O(1)
[+]Time Complexity           : O(N)
[+]Level                     :
[+]Tread Speed               :
[+]LINK                      : https://www.interviewbit.com/problems/palindrome-list
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

    def reverse(self):
        head = self.head
        current = head
        previous = None
        while not current is None:
            temp = current.next
            current.next = previous
            previous = current
            current = temp
        self.head = previous
        print("reversal is complete...")

    def is_palindrome(self):
        head = self.head
        count = 0
        current = head
        while current is not None:
            current = current.next
            count += 1
        mid_position = (count + 1) // 2
        if count == 1:
            return 1
        current = head
        previous = None
        mid = None
        while current is not None:
            if current.next is None:
                return 0
            mid_position -= 1
            if mid_position == 0:
                mid = current
                break
            else:
                temp = current.next
                current.next = previous
                previous = current
                current = temp

        # Check if it's a palindrome
        if count % 2 == 0:
            right = mid.next
            mid.next = previous
            left = mid
        else:
            left = previous
            right = mid.next
        while left is not None and right is not None:
            if left.value == right.value:
                left = left.next
                right = right.next
            else:
                return 0
        return 1


# go to the half of the lis
# start again from two points simulatneously to check if it's a palindrome
# it it's acbca
# if it's abba
# either the preivous is equal to next or | current == next


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
           [1,2,3,4]]
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
        print(" | " + str(linkedList.is_palindrome()))
        # linkedList.reverse()
        # linkedList.print()
