"""
Sliding Window Maximum
Asked in:
Google
Chronus
Walmart labs
Amazon
Given an array of integers A. There is a sliding window of size B which
is moving from the very left of the array to the very right.
You can only see the w numbers in the window. Each time the sliding window moves
rightwards by one position. You have to find the maximum for each window.
The following example will give you more clarity.

The array A is [1 3 -1 -3 5 3 6 7], and B is 3.

Window position	Max
———————————-	————————-
[1 3 -1] -3 5 3 6 7	3
1 [3 -1 -3] 5 3 6 7	3
1 3 [-1 -3 5] 3 6 7	5
1 3 -1 [-3 5 3] 6 7	5
1 3 -1 -3 [5 3 6] 7	6
1 3 -1 -3 5 [3 6 7]	7
Return an array C, where C[i] is the maximum value of from A[i] to A[i+B-1].

Note: If B > length of the array, return 1 element with the max of the array.



Input Format

The first argument given is the integer array A.
The second argument given is the integer B.
Output Format

Return an array C, where C[i] is the maximum value of from A[i] to A[i+B-1]
For Example

Input 1:
    A = [1, 3, -1, -3, 5, 3, 6, 7]
    B = 3
Output 1:
    C = [3, 3, 5, 5, 6, 7]


[+]Temporal marker           : Wed, 13:50 | Mar 18, 20
[+]Temporal marker untethered: Wed, 13:50 | Mar 18, 20
[+]Comments                  :
[+]Space Complexity          : O()
[+]Time Complexity           : O()
[+]Level                     :
[+]Tread Speed               :
[+]LINK                      : https://www.interviewbit.com/problems/sliding-window-maximum
[+] Supplement Sources       : N/A
"""


# TLE, Accepted
def findSolution_naive(lis, window):
    if window > len(lis):
        return max(lis)
    left, right = 0, window - 1
    ans = []
    while left <= len(lis) - window:
        ans.append(max(lis[left:left + window]))
        left += 1
        right += 1
    return ans


def findSolution(lis, window):
    length = len(lis)
    if window >= length:
        return max(lis)
    # find the max and the second max
    first_max, second_max = lis[0], lis[0]
    for x in range(window):
        if first_max > lis[x]:
            second_max = first_max
            first_max = lis[x]

    ans  = [first_max]
    left, right = window, window + window -1
    while left <= length - window:
        if lis[left] == first_max:
            #need to find the next firstMax
            if lis[right] > second_max:
                first_max = lis[right]
            else:
                # need to find the next second_max
                second_max = lis[left]
                for x in range(left, left+window):
                    if second_max < lis[x] < first_max:
                        second_max = lis[x]
        else:
            if lis[right] > first_max:
                second_max = first_max
                first_max = lis[right]
            if lis[right] > second_max:
                second_max = lis[right]
        ans.append(first_max)
        left += 1
        right += 1
    return ans

if __name__ == "__main__":
    test_cases = [
        [[1, 3, -1, -3, 5, 3, 6, 7], 3]
    ]
    for test_case in test_cases:
        print("input: " + str(test_case) + " >> " + str(findSolution(test_case[0], test_case[1])))
