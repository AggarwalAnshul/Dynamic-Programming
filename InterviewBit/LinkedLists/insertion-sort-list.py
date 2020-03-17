"""
Insertion Sort List
Asked in:
Microsoft
Google
Sort a linked list using insertion sort.

We have explained Insertion Sort at Slide 7 of Arrays

Insertion Sort Wiki has some details on Insertion Sort as well.

Example :

Input : 1 -> 3 -> 2

Return 1 -> 2 -> 3


[+]Temporal marker           : Sat, 11:54 | Mar 07, 20
[+]Temporal marker untethered: Sat, 14:00 | Mar 07, 20
[+]Comments                  : I'm not much happy with solution
                                This works but it's too crappy.
                                This has been marked for revisit.
                                JUST TO BE CLEAR< this is accpeted and perfectly functional.
[+]Space Complexity          : O(1)
[+]Time Complexity           : O(N)
[+]Level                     :
[+]Tread Speed               :
[+]LINK                      : https://www.interviewbit.com/problems/insertion-sort-list
[+] Supplement Sources       : N/A
"""


class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None


def print_linked_list(head):
    current = head
    while current:
        print(str(current.val), end=" -> ")
        current = current.next
    print("")


# def insertionSortList(head):
#     def reversed_linked_lis(head):
#         previous, current = None, head
#         while current:
#             temp = current.next
#             current.next = previous
#             previous = current
#             current = temp
#         return previous
#
#     previous, current = head, head.next
#     while current:
#         flag = 0
#         print("opearating on: "+str(current.val))
#         element = current.val
#         save_previous = previous
#         save_current = current
#         previous = current
#         current = current.next
#         while element > current.val:
#             flag = 1
#             previous = current
#             current = current.next
#         if flag == 1:
#             save_previous.next = save_current.next
#             previous.next = save_current
#             save_current.next = current
#             current = save_previous.next
#             previous = save_previous
#         print_linked_list(head)


def insertion_obsolete(head):
    if head.next is None:
        return head
    def reversed_linked_lis(head):
        previous, current = None, head
        while current:
            temp = current.next
            current.next = previous
            previous = current
            current = temp
        return previous
    previous, current = head, head.next
    head.next = None
    sorted_head = None
    while current:
        next_node = current.next
        element = current.val

        # continue the reversed list
        current.next = previous
        previous = current
        sorted_head = previous

        # find the fit position for this
        back_pointer = previous.next
        back_pointer_previous = previous
        save_back_pointer = back_pointer
        while back_pointer and element < back_pointer.val:
            sorted_head = save_back_pointer
            previous = save_back_pointer
            back_pointer_previous = back_pointer
            back_pointer = back_pointer.next
            if back_pointer is None:
                back_pointer_previous.next = current
                back_pointer_previous.next.next = None
            elif back_pointer.val <= element:
                back_pointer_previous.next = current
                back_pointer_previous.next.next = back_pointer

        # continue the reverse linked list
        current = next_node
    return reversed_linked_lis(sorted_head)

def insertion(head):
    previous, current = None, head
    sorted = ListNode(0)
    save = sorted
    while current:
        print("working on: "+str(current.val))
        element = current.val
        temp = current.next
        forward_pointer = current.next
        while element >= forward_pointer.val:
            if forward_pointer.next is None or forward_pointer.next.val >= element:
                tempTwo = forward_pointer.next
                forward_pointer.next = current
                forward_pointer.next.next = tempTwo

                #break this last element form the chain
                break
            else:
                forward_pointer = forward_pointer.next
        current = temp
    return head

if __name__ == '__main__':
    lis = [
        [[1, 4, 3, 2, 5, 2], 3],
        [[1,2],0],
        [[1],0]
    ]

    for test_case in lis:
        one = ListNode(0)
        one_head = one
        for index in range(len(test_case[0])):
            one.next = ListNode(test_case[0][index])
            one = one.next
        one_head = one_head.next
        print("input: ", end=" >> ")
        print_linked_list(one_head)
        print_linked_list(insertion(one_head))
