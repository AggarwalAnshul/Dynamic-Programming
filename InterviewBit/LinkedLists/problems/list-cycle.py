"""

[+]Temporal marker           : Sat, 11:00 | Mar 07, 20
[+]Temporal marker untethered: Sat, 11:33 | Mar 07, 20
[+]Comments                  : I KNew the cycle detection algorithm only
                                I did't knew how to find the first duplicate element
                                Found the logic on a blog when i was seraching Floyds cycle detectino algo
                                I've now fully understood the approach
                                Matter is closed now
[+]Space Complexity          : O(1)
[+]Time Complexity           : O(N)
[+]Level                     : MEDIUM
[+]Tread Speed               : I was playing PUBG IN THE AMIDST
[+]LINK                      : https://www.interviewbit.com/problems/list-cycle
[+] Supplement Sources       : N/A
"""


class LisNode:
    def __init__(self, value):
        self.val = value
        self.next = None


def print_linked_lis(head):
    current = head
    while current:
        print(str(current.val), end=" -> ")
        current = current.next
    print("\n")


# @param head: head of the linked list
# return the first element that is duplicate
def detectCycle(head):
    hare = head
    tortoise = head
    while hare and tortoise and tortoise.next:
        hare = hare.next
        tortoise = tortoise.next.next
        if hare == tortoise:
            tortoise = head
            while True:
                if tortoise == hare:
                    return hare
                tortoise = tortoise.next
                hare = hare.next
    return None


if __name__ == '__main__':
    pass
