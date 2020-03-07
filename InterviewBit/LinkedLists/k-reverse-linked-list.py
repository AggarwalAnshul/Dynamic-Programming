"""
K reverse linked list
Asked in:
Microsoft
Amazon
Problem Setter: mihai.gheorghe Problem Tester: yashpal1995
Given a singly linked list and an integer K, reverses the nodes of the

list K at a time and returns modified linked list.

 NOTE : The length of the list is divisible by K
Example :

Given linked list 1 -> 2 -> 3 -> 4 -> 5 -> 6 and K=2,

You should return 2 -> 1 -> 4 -> 3 -> 6 -> 5

Try to solve the problem using constant extra space.


[+]Temporal marker           : Fri, 14:42 | Mar 06, 20
[+]Temporal marker untethered: Fri, 15:22 | Mar 06, 20
[+]Comments                  : Could have solved it like 20 minutes before,
                                I wrote a BAD function to print LINKED LIST!!!!! LOL!!!!!! WTH Is wrong with me :O
                                Anyway, problem is now solved
                                easy peasy
[+]Space Complexity          : O(1)
[+]Time Complexity           : O(N)
[+]Level                     : EASY
[+]Tread Speed               : Relaxed
[+]LINK                      : https://www.interviewbit.com/problems/k-reverse-linked-list
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
        print(str(current.value), end = " -> ")
        current = current.next
    print()

def reverseList(head, k):
    print()
    merged = Node(0)
    saved = merged
    merged_end = saved
    previous, current = None, head
    counter = 0
    reversed_end = head
    attach_to = head
    while current:
        print("on node: "+str(current.value))
        counter = counter + 1
        print("\tCounter is: "+str(counter))
        if counter == 1:
            reversed_end = current
        temp = current.next
        current.next = previous
        previous = current
        current = temp
        if counter == k:
            # attach this to the merged list
            print("linked list so far: \t",end=" >> ")
            print_linked_lis(previous)
            counter = 0
            print("previosu is: "+str(previous.value))
            merged_end.next = previous
            merged_end = reversed_end
            merged_end.next = None
            reversed_end.next = None
            print("Printing merged so far...")
            print_linked_lis(merged)
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
        print(" |  ",end="")
        print("printing outpu...")

        print_linked_lis(reverseList(linkedList.head, 1))
        # linkedList.reverse()
        # linkedList.print()

