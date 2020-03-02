"""

[+]Temporal marker           : Mon, 10:44 | Mar 02, 20
[+]Temporal marker untethered: Mon, 10:44 | Mar 02, 20
[+]Comments                  :
[+]Space Complexity          : O()
[+]Time Complexity           : O()
[+]Level                     :
[+]Tread Speed               :
[+]LINK                      : https://www.interviewbit.com/problems/__init__
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
        print(" | " + str())
        # linkedList.reverse()
        # linkedList.print()

