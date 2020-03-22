"""
NEXTGREATER
Given an array, find the next greater element G[i] for every element A[i] in the array.
The Next greater Element for an element A[i] is the first greater element on the right side of
A[i] in array.
More formally,

G[i] for an element A[i] = an element A[j] such that
    j is minimum possible AND
    j > i AND
    A[j] > A[i]
Elements for which no greater element exist, consider next greater element as -1.

Example:

Input : A : [4, 5, 2, 10]
Output : [5, 10, 10, -1]

Example 2:

Input : A : [3, 2, 1]
Output : [-1, -1, -1]

[+]Temporal marker           : 16:23 Hours | Sunday 22, 2020
[+]Temporal marker untethered: 16:23 Hours | Sunday 22, 2020
[+]Comments                  : I realized this is practically similar to a previous problem
                                I went to  the problem to check
                                I knew the approach for that problem
                                I just tweaked the approach and voila!
                                This matter is officially closed now.
[+]Space Complexity          : O(N)
[+]Time Complexity           : O(N)
[+]Level                     : MEDIUM
[+]Tread Speed               : Relaxed, on call with Mini
[+]LINK                      : https://www.interviewbit.com/problems/nearest-smaller-element
[+] Supplement Sources       : N/A

"""


# @param A : list of integers
# @return a list of integers
#Accepted
def nextGreater(lis):
    stack, ans = [], []
    for item in reversed(lis):
        while stack and item >= stack[-1]:
            stack.pop()
        if stack:
            ans.insert(0, stack[-1])
        else:
            ans.insert(0, -1)
        stack.append(item)
    return ans

if __name__ == '__main__':
    test_cases = [
        [4, 5, 2, 10],
        [39, 27, 11, 4, 24, 32, 32, 1 ]
    ]
    for test_case in test_cases:
        print(nextGreater(test_case))
