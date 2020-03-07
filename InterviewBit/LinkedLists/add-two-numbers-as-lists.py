"""
Add Two Numbers as Lists
Asked in:
Amazon
Qualcomm
Microsoft
Facebook
You are given two linked lists representing two non-negative numbers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8

    342 + 465 = 807
Make sure there are no trailing zeros in the output list
So, 7 -> 0 -> 8 -> 0 is not a valid response even though the value is still 807.

[+]Temporal marker           : Sat, 7:37 | Mar 07, 20
[+]Temporal marker untethered: Sat, 8:40 | Mar 07, 20
[+]Comments                  : MEDIUM
[+]Space Complexity          : O(1)
[+]Time Complexity           : O(N)
[+]Level                     : MEDIUM
[+]Tread Speed               : PACED
[+]LINK                      : https://www.interviewbit.com/problems/add-two-numbers-as-lists
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
        print(str(current.value), end=" -> ")
        current = current.next
    print("\n")


# TLE
def addTwoNumbers_obsolete(head_one, head_two):
    def find_the_number(head):
        current = head
        offset = 1
        number = 0
        while current:
            number += offset * current.value
            current = current.next
            offset *= 10
        return number

    number = find_the_number(head_one) + find_the_number(head_two)
    merged = Node(0)
    save = merged
    while number > 0:
        merged.next = Node(number % 10)
        number //= 10
        merged = merged.next
    return save.next


# Bonus Approach
def addTwoNumbers_bonus(head_one, head_two):
    # print("one: ")
    # print_linked_lis(head_one)
    # print("two: ")
    # print_linked_lis(head_two)
    current_one = head_one
    current_two = head_two
    merged = Node(0)
    save = merged
    flag = 0

    def length_of_linked_lis(head):
        length = 0
        current = head
        while current:
            current = current.next
            length += 1
        return length

    # equating the number of digits in both the linked list
    length_one = length_of_linked_lis(head_one)
    length_two = length_of_linked_lis(head_two)
    if length_two < length_one:
        return addTwoNumbers(head_two, head_one)
    if length_one < length_two:
        difference = length_two - length_one
        while difference > 0:
            temp = Node(0)
            temp.next = head_one
            head_one = temp
            difference -= 1
    print("the lists have been equated...")
    print_linked_lis(head_one)
    print_linked_lis(head_two)
    current_one = head_one
    current_two = head_two

    while current_one or current_two:
        if current_two and current_one:
            print("currently on: " + str(current_one.val) + " and " + str(current_two.val))
            combined_val = flag + current_one.val + current_two.val
            merged.next = Node(combined_val % 10)
            merged = merged.next
            combined_val //= 10
            flag = combined_val % 10
            current_one = current_one.next
            current_two = current_two.next
        # elif current_two:
        #     print("currently on: "+str(current_two.val))
        #     val = flag + current_two.val
        #     merged.next = ListNode(val % 10)
        #     merged = merged.next
        #     val //= 10
        #     flag = val % 10
        #     current_two = current_two.next
        #
        # elif current_one:
        #     print("currently on : "+str(current_one.val))
        #     val = flag + current_one.val
        #     merged.next = ListNode(val % 10)
        #     merged = merged.next
        #     val //= 10
        #     flag = val % 10
        #     current_one = current_one.next
        else:
            # flag is non zero
            if flag > 0:
                merged.next = Node(flag)
                merged = merged.next
    return save.next


# Memory Exceeded
def addTwoNumbers_memory_exceeded(head_one: object, head_two: object) -> object:
    # print("one: ")
    # print_linked_lis(head_one)
    # print("two: ")
    # print_linked_lis(head_two)
    current_one = head_one
    current_two = head_two
    merged = Node(0)
    save = merged
    flag = 0

    while current_one or current_two:
        if current_two and current_one:
            print("currently on: " + str(current_one.value) + " and " + str(current_two.value))
            combined_value = flag + current_one.value + current_two.value
            merged.next = Node(combined_value % 10)
            merged = merged.next
            combined_value //= 10
            flag = combined_value % 10
            current_one = current_one.next
            current_two = current_two.next

        elif current_two:
            print("currently on: " + str(current_two.value))
            value = flag + current_two.value
            merged.next = Node(value % 10)
            merged = merged.next
            value //= 10
            flag = value % 10
            current_two = current_two.next

        elif current_one:
            print("currently on : " + str(current_one.value))
            value = flag + current_one.value
            merged.next = Node(value % 10)
            merged = merged.next
            value //= 10
            flag = value % 10
            current_one = current_one.next
        else:
            # flag is non zero
            if flag > 0:
                merged.next = Node(flag)
                merged = merged.next
    return save.next


# FINALLY ACCEPTED!
# @param head_one : head of the first linked list
# @param head_two : head of the second linked list
# return, head of the linked list operated upon as per aforementioned problem statement
def addTwoNumbers(head_one, head_two):
    current_one, current_two, flag = head_one, head_two, 0

    def length_of_linked_lis(head):
        current, length = head, 0
        while current:
            current = current.next
            length += 1
        return length

    # With this, I can assume first linked list is the longer one
    if length_of_linked_lis(head_one) < length_of_linked_lis(head_two):
        return addTwoNumbers(head_two, head_one)

    while current_one or current_two or flag != 0:
        if current_two and current_one:
            combined_value = flag + current_one.value + current_two.value

            current_one.value = combined_value % 10
            combined_value //= 10
            flag = combined_value % 10
            current_one = current_one.next
            current_two = current_two.next

        else:  # current_one still exists
            print("currently on : " + str(current_one.value))
            value = flag + current_one.value
            current_one.value = value % 10
            value //= 10
            flag = value % 10
            if current_one.next is None and flag > 0:
                current_one.next = Node(flag)
                return head_one
            else:
                current_one = current_one.next
    return head_one


if __name__ == '__main__':
    lis = [
        [[2, 4, 3], [5, 6, 4]],
        [[9, 9, 1], [1]],
        [[9, 9, 9], [1]]
    ]
    for test_case in lis:
        one = Node(0)
        one_head = one
        for index in range(len(test_case[0])):
            one.next = Node(test_case[0][index])
            one = one.next
        two = Node(0)
        two_head = two
        for index in range(len(test_case[1])):
            two.next = Node(test_case[1][index])
            two = two.next
        one_head = one_head.next
        two_head = two_head.next
        print_linked_lis(one_head)
        print_linked_lis(two_head)
        print("output: ", end=" >> ")
        print_linked_lis(addTwoNumbers(one_head, two_head))
