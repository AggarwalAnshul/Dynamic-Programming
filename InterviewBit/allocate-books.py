"""

[+]Temporal marker           : Tue, 22:41 | Feb 04, 20
[+]Temporal marker untethered: Tue, 22:52 | Feb 04, 20
[+]Comments                  : Similar to Painters Partition problem except a minor if condition
                                *Solved in record time with no help
                                *Optimized solution
                                *Matter closed for now
[+]Level                     : Medium
[+]Tread Speed               : paced
[+]Complexity                : O(Log(sum(books)))
[+]LINK                      : https://www.interviewbit.com/problems/allocate-books

"""
import sys


class Solution:

    def books(self, book, students):
        if students > len(book):
            return -1

        def isPossible(mid, book, number_of_student):
            local = 0
            for x in book:
                if local + x <= mid:
                    local += x
                else:
                    local = x
                    number_of_student -= 1
            if number_of_student <= 0:
                return False
            return True

        right = 0
        left = -sys.maxsize + 1
        for x in book:
            left = max(left, x)
            right += x

        while left < right:
            mid = (left + right) // 2
            if (isPossible(mid, book, students)):
                right = mid
            else:
                left = mid + 1
        return left

obj = Solution()
print(obj.books([ 12, 34, 67, 90 ], 2))