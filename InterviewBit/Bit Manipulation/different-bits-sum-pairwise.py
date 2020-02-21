"""

[+]Temporal marker           : Fri, 13:49 | Feb 21, 20
[+]Temporal marker untethered: Fri, 16:28 | 13:56(TLE) | Feb 21, 20
[+]Comments                  : Devised the O(N*N) Solution in record time, Gives TLE
                                *Couldn't have figured out Optimized, on my own
                                *iB Hint was not of much help
                                *learned the efficient approach from GFG
                                *Implemented on my own, Solution is accepted
                                *Significant temporal delay is explained by lunch + office Work
                                *Matter is closed now.
[+]Space Complexity          : O(32 * N)
[+]Time Complexity           : O(1)
[+]Level                     : MEDIUM
[+]Tread Speed               : relaxed
[+]LINK                      : https://www.interviewbit.com/problems/different-bits-sum-pairwise
[+] Supplement Sources       : https://www.geeksforgeeks.org/sum-of-bit-differences-among-all-pairs/
"""


def optimized(lis):
    length = len(lis)
    ans = 0
    for i in range(32):
        count = 0
        for j in range(length):
            if lis[j] & 1 << i:
                count += 1
        ans += (count * (length-count)) << 1
    return ans % (10**9 + 7)


def findSolution(lis):
    def numberOfDifferentBits(a, b):
        c = a ^ b
        count = 0
        while c != 0:
            c &= c - 1
            count += 1
        return count

    length = len(lis)
    ans = 0
    for i in range(length):
        for j in range(i + 1, length):
            ans += numberOfDifferentBits(lis[i], lis[j])
    return ans << 1


if __name__ == "__main__":
    data = [[1, 3, 5], [2, 2, 2], [1, 2, 3, 4]]
    for x in data:
        print("input: " + str(x) + " >> " + str(findSolution(x)))
