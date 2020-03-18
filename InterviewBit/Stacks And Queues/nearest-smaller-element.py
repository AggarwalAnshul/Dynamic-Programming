"""
Nearest Smaller Element
Asked in:
Amazon
Microsoft
Given an array, find the nearest smaller element G[i] for every element A[i] in the array such that
the element has an index smaller than i.

More formally,

    G[i] for an element A[i] = an element A[j] such that
    j is maximum possible AND
    j < i AND
    A[j] < A[i]
Elements for which no smaller element exist, consider next smaller element as -1.

Input Format

The only argument given is integer array A.
Output Format

Return the integar array G such that G[i] contains nearest smaller number than A[i].If no such element
 occurs G[i] should be -1.
For Example

Input 1:
    A = [4, 5, 2, 10, 8]
Output 1:
    G = [-1, 4, -1, 2, 2]
Explaination 1:
    index 1: No element less than 4 in left of 4, G[1] = -1
    index 2: A[1] is only element less than A[2], G[2] = A[1]
    index 3: No element less than 2 in left of 2, G[3] = -1
    index 4: A[3] is nearest element which is less than A[4], G[4] = A[3]
    index 4: A[3] is nearest element which is less than A[5], G[5] = A[3]

Input 2:
    A = [3, 2, 1]
Output 2:
    [-1, -1, -1]
Explaination 2:
    index 1: No element less than 3 in left of 3, G[1] = -1
    index 2: No element less than 2 in left of 2, G[2] = -1
    index 3: No element less than 1 in left of 1, G[3] = -1

[+]Temporal marker           : Wed, 9:01  | Mar 18, 20
[+]Temporal marker untethered: Wed, 10:06 | Mar 18, 20
[+]Comments                  :
[+]Space Complexity          : O()
[+]Time Complexity           : O()
[+]Level                     :
[+]Tread Speed               :
[+]LINK                      : https://www.interviewbit.com/problems/nearest-smaller-element
[+] Supplement Sources       : N/A
"""


# TLE but Accepted
# @param array : lis containing elements
def prevSmaller_naive(array):
    length = len(array)
    ans = []
    for x in range(length):
        temp = array[x]
        index = x - 1
        while index >= 0 and array[index] >= array[x]:
            index -= 1
        if index >= 0 and array[index] < array[x]:
            ans.append(array[index])
        else:
            ans.append(-1)
    return ans


# TLE but accepted
# Slightly optimized over the last iteration
def prevSmaller_obsolete(array):
    length = len(array)
    aux = [-1]
    for x in range(1, length):
        element = array[x]
        if array[x - 1] < array[x]:
            aux.append(array[x - 1])
        elif array[x - 1] == array[x]:
            aux.append(aux[-1])
        else:
            index = x - 1
            while index >= 0 and array[index] >= array[x]:
                index -= 1
            if index >= 0 and array[index] < array[x]:
                aux.append(array[index])
            else:
                aux.append(-1)
    return aux


# Accepted
# @param array : lis containing elements
def prevSmaller(array):
    length = len(array)
    stack = [array[0]]
    ans = [-1]
    for x in range(1, length):
        element = array[x]
        if stack[-1] < element:
            ans.append(stack[-1])
        else:
            while len(stack) > 0 and stack[-1] >= element:
                stack.pop()
            if len(stack) > 0 and stack[-1] < element:
                ans.append(stack[-1])
            else:
                ans.append(-1)
        stack.append(element)
    return ans


# Editorial Inspired
# @param array : lis containing elements
def prevSmaller_editorial(array):
    stack, ans = [], []
    for element in array:
        while stack and stack[-1] >= element:
            stack.pop()
        if stack:
            ans.append(stack[-1])
        else:
            ans.append(-1)
        stack.append(element)
    return ans


if __name__ == "__main__":
    data = [
        [3, 2, 1],
        [4, 5, 2, 10, 8],
        [34, 35, 27, 42, 5, 28, 39, 20, 28]
    ]
    for x in data:
        print("input: " + str(x)
              + "\n\t DEVISED   >> " + str(prevSmaller(x))
              + "\n\t Editorial >> " + str(prevSmaller_editorial(x)))
