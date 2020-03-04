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
[+]Temporal marker untethered: Mon, 16:0 | Mar 02, 20
[+]Comments                  :
[+]Space Complexity          : O()
[+]Time Complexity           : O()
[+]Level                     :
[+]Tread Speed               :
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
            print(str(current.val), end = " -> ")
            current = current.next

    def removeDuplicates(self):
        previous = None
        current = self.head
        last = None
        while current:
            if current.next is not None and current.val == current.next.val:
                last = current.val
                temp = current.next.next
                if previous == None:
                    self.head = temp
                else:
                    previous.next = temp
                print("HEAD value changed to: "+str(self.head.val))
                current.next.next = None
                current = temp

            else:
                if current.val == last:
                    previous.next = current.next
                    temp = current.next
                    current.next = None
                    current = temp
                else:
                    last = None
                    if current.next and current.next.next and not current.next.val == current.next.next.val:
                        previous = current
                    #print("previous is: "+str(previous.val))
                    current = current.next
        print("printing the new lis...")
        current = self.head
        while current:
            print(str(current.val), end = " -> ")
            current = current.next


   
if __name__ == '__main__':
    lis = [ ["a"]
        , ["a", "a", "a"]
        , ["a", "b", "b", "f"]
        , ["a", "b", "c", "c", "c", "e", "a"]
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
        print("input: >> ", end = " ")
        linkedList.print()
        print(" Output: >> ", end = " ")
        linkedList.removeDuplicates()
        print("\n\t")