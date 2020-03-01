"""
NUMRANGE
Given an array of non negative integers A, and a range (B, C),
find the number of continuous subsequences in the array which have sum S in the range [B, C]
or B <= S <= C

Continuous subsequence is defined as all the numbers A[i], A[i + 1], .... A[j]
where 0 <= i <= j < size(A)

Example :

A : [10, 5, 1, 0, 2]
(B, C) : (6, 8)
ans = 3
as [5, 1], [5, 1, 0], [5, 1, 0, 2] are the only 3 continuous subsequence with their sum in
 the range [6, 8]



[+]Temporal marker           : Fri, 22:3 | Feb 28, 20
[+]Temporal marker untethered: Fri, 22:3 | Feb 28, 20
[+]Comments                  : MEDIUM
[+]Space Complexity          : O(1)
[+]Time Complexity           : O(N)
[+]Level                     : MEDIUM
[+]Tread Speed               : Relaxed
[+]LINK                      : https://www.interviewbit.com/problems/numrange
[+] Supplement Sources       : logic behind number of subarrays = j-i+1 is explained by:

number of subarrays for this new end pointer would be:
[end-1, end], [end-2..end], [end-3...end], ...., [start-1...end], [start, end]
@jagzmz
Consider the following:
k = 15 and a subsequence of [1,2,3] in the context of the solution posted
The counts get increased as follows:
count += (1-0 = 1)
count += (2- 0 = 2)
count += (3- 0 = 3)

notice the additional possibilities at each step:
[1] => 1
[1,2] = [2], [1,2]
[1,2,3] = [3], [2,3], [1,2,3]
"""


# Accepted, but i suspect it should be a TLE and i can do better
def findSolution(lis, a, b):
    length = len(lis)
    count = 0
    for index in range(length):
        sum = 0
        for j in range(index, length):
            sum += lis[j]
            if sum > b:
                break
            elif a <= sum <= b:
                count += 1
    return count

# Accepted Solution with T-Compleity O(N)
def experimental(lis, a, b):
    length = len(lis)

    def count_subarrays(lis, k):
        start, end, count = 0, 0, 0
        sum = 0
        length = len(lis)
        while end < length:
            sum += lis[end]
            while sum > k and start <= end:
                sum -= lis[start]
                start += 1
            count += end - start + 1
            end += 1
        return count

    return count_subarrays(lis, b) - count_subarrays(lis, a - 1)


if __name__ == "__main__":
    data = [[[10, 5, 1, 0, 2], 6, 8]]
    for x in data:
        print("input: " + str(x) + "\n\t >> " + str(findSolution(x[0], x[1], x[2])) +
              " Experimental: " + str(experimental(x[0], x[1], x[2])))
