#M.

"""
Maximum subarray sum in O(n) using prefix sum
Given an Array of Positive and Negative Integers, find out the Maximum Subarray Sum in that Array.

Examples:

Input1 : arr = {-2, -3, 4, -1, -2, 1, 5, -3}
Output1 : 7

Input2 : arr = {4, -8, 9, -4, 1, -8, -1, 6}
Output2 : 9
 
[+]Temporal marker            :  Sat, 12:14 | Jan 11, 20
[+]Temporal marker untethered :  Sat, 12:16:50- | Jan 11, 20
[+]Comments                   : *
                                *
                                *
[+]Level                      : 
[+]Tread speed                : 
[+]LINK                       : https://www.geeksforgeeks.org/maximum-subarray-sum-using-prefix-sum
"""
def findSolution(array):
    length = len(array)
    prev = array[0]
    ans = array[0]
    for x in range(1, length):
        prev = max(prev + array[x], array[x])
        ans = max(ans, prev)
    return ans

if __name__ == "__main__":
    array = [4, -8, 9, -4, 1, -8, -1, 6]
    array = [-2, -3, 4, -1, -2, 1, 5, -3]
    print(findSolution(array))
