"""
Diffk
Asked in:
Facebook
Given an array ‘A’ of sorted integers and another non negative integer k,
find if there exists 2 indices i and j such that A[i] - A[j] = k, i != j.

 Example: Input :
    A : [1 3 5]
    k : 4
 Output : YES as 5 - 1 = 4
Return 0 / 1 ( 0 for false, 1 for true ) for this problem

Try doing this in less than linear space complexity.

[+]Temporal marker           : Mon, 15:8 | Feb 24, 20
[+]Temporal marker untethered: Mon, 15:16 | Feb 24, 20
[+]Comments                  : EASY
[+]Space Complexity          : O(1)
[+]Time Complexity           : O(N)
[+]Level                     : EASY
[+]Tread Speed               : PACED
[+]LINK                      : https://www.interviewbit.com/problems/diffk
[+] Supplement Sources       : N/A
"""

def findSolution(lis, k):
    length = len(lis)
    for index in range(length):
        left = index
        right = length - 1
        while left < right:
            if lis[left] + lis[right] == k:
                return 1
            elif lis[left] + lis[right] < k:
                left += 1
            else:
                right -= 1
        return 0



if __name__ == "__main__":
    data = [[[1,3,5],4]]
    for x in data:
        print("input: " + str(x) + " >> " + str(findSolution(x[0], x[1])))