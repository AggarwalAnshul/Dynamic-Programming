"""
Given an array S of n integers, find three integers in S such that the sum is closest
 to a given number, target.
Return the sum of the three integers.

Assume that there will only be one solution

Example:
given array S = {-1 2 1 -4},
and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2)



[+]Temporal marker           : Sat, 18:23 | Feb 22, 20
[+]Temporal marker untethered: Sat, 16:26 | Feb 23, 20
[+]Comments                  : Couldn't solve on my own with efficiency
                               Implemented the solution approach form iB
                               Matter is now closed
[+]Space Complexity          : O(1)
[+]Time Complexity           : O(N*N)
[+]Level                     : MEDIUM
[+]Tread Speed               : relaxed
[+]LINK                      : https://www.interviewbit.com/problems/3-sum
[+] Supplement Sources       : N/A
"""


def findSolution(lis, target):
    lis.sort()
    length = len(lis) - 1
    import sys
    answer = sys.maxsize
    print("sorted: "+str(lis))
    for index in range(length):
        print("index: " +str(index))
        minimum = lis[index]
        left = index + 1
        right = length

        while left < right:
            print("\tleft: "+str(left)+" right: "+str(right))
            if abs(target - lis[left] - lis[right] - minimum) < abs(target - answer):
                answer = lis[left] + lis[right] + minimum
                print("\tanswer is: " + str(answer))
            if lis[left] + lis[right] + minimum > target:
                right -= 1
            elif lis[left] + lis[right] + minimum < target:
                left += 1
            else:
                print("returning: "+str(lis[left] + lis[right] + minimum))
                return lis[left] + lis[right] + minimum
        print('best is: '+str(answer))
    return answer


if __name__ == "__main__":
    data = [[[-1, 4, 2, 1], 5],
            [[-5, 1, 4, -7, 10, -7, 0, 7, 3, 0, -2, -5, -3, -6, 4, -7, -8, 0, 4, 9, 4, 1, -8, -6, -6, 0, -9, 5, 3, -9,
              -5, -9, 6, 3, 8, -10, 1, -2, 2, 1, -9, 2, -3, 9, 9, -10, 0, -9, -2, 7, 0, -4, -3, 1, 6, -3], -1],
            [[-5, 1, 4, -7, 10], 1],
            [[-3, 0, 0, 1, 2], -1],
            [[-10, -10, -10], -5],
            [[-4, -8, -10, -9, -1, 1, -2, 0, -8, -2], 0],
            [[ 2, 1, -9, -7, -8, 2, -8, 2, 3, -8 ], -1]]
    dataone= [[[ 2, 1, -9, -7, -8, 2, -8, 2, 3, -8 ], -1]]
    for x in dataone:
        print("input: " + str(x) + " >> " + str(findSolution(x[0], x[1])))
