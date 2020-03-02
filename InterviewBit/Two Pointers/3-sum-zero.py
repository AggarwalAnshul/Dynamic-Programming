
"""
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Note:

 Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
The solution set must not contain duplicate triplets. For example, given array S = {-1 0 1 2 -1 -4},
A solution set is:
(-1, 0, 1)
(-1, -1, 2)


[+]Temporal marker           : Sun, 19:40 | Feb 23, 20
[+]Temporal marker untethered: Sun, 19:40 | Feb 23, 20
[+]Comments                  :THIS PROBLEM IS A JOKE OR AT LEAST IB COMPILER
                            *Created the solution withing acceptable time int he first place
                            *The solution was giving TLE Error
                            *The solution was actively finding duplicates w/o additional loop
                                & giving correct answer for the test case
                            *Finally went old school and used a simple O(N) loop to find the
                                duplicates which got accepted.
                            *GOSH THIS WASTED SO MUCH TIME OF MINE!

[+]Space Complexity          : O(N*N)
[+]Time Complexity           : O(N)
[+]Level                     : Medium
[+]Tread Speed               : Relaxed
[+]LINK                      : https://www.interviewbit.com/problems/3-sum-zero
[+] Supplement Sources       : N/A
"""

def editorial(lis):
    lis.sort()
    answer = set()
    length = len(lis)

    for index in range(length):
        left = index + 1
        right = length - 1
        while left < right:
            current_sum = lis[index] + lis[right] + lis[left]
            if current_sum == 0:
                answer.add((lis[index], lis[left], lis[right]))
                left += 1
                right -= 1
            elif current_sum < 0:
                left += 1
            else:
                right -= 1
    return list(answer)


#Accepted Solution
def experimental(lis):
    def compare(lis, a):
        for element in lis:
            if element[0] == a[0] and element[1] == a[1]:
                return False
        return True

    lis.sort()
    answer = []
    length = len(lis)

    for index in range(length):
        if index == 0 or (index > 0 and lis[index] != lis[index - 1]):
            temp = []
            left = index + 1
            right = length - 1
            while left < right:
                current_sum = lis[index] + lis[right] + lis[left]
                if current_sum == 0:
                    if compare(temp, [lis[left], lis[right]]):
                        temp.append([lis[left], lis[right]])
                        answer.append([lis[index], lis[left], lis[right]])
                    left += 1
                    right -= 1
                elif current_sum < 0:
                    left += 1
                else:
                    right -= 1
    return answer


# Accepted but TLE
def findSolution(lis):
    lis.sort()
    triplets_count = 0
    triplets = []
    length = len(lis)

    for index in range(length):
        if index == 0 or (index > 0 and lis[index] != lis[index - 1]):
            left = index + 1
            right = length - 1
            while left < right:
                if (((left > index + 1 and right < length - 1) and (
                        not (lis[left] == lis[left - 1]) or not (lis[right] == lis[right + 1]))) or (
                        left == index + 1 or right == length - 1)):
                    current_sum = lis[index] + lis[left] + lis[right]
                    if lis[index] + lis[left] + lis[right] == 0:
                        triplets_count += 1
                        triplets.append([lis[index], lis[left], lis[right]])
                        left += 1
                        right -= 1
                    elif current_sum > 0:
                        right -= 1
                    else:
                        left += 1
                else:
                    left += 1
                    right -= 1

    return triplets


if __name__ == "__main__":
    data = [[-1, 0, 1, 0, 1, 2, -1, -4],
            [1, -4, 0, 0, 5, -5, 1, 0, -2, 4, -4, 1, -1, -4, 3, 4, -1, -1, -3],
            [-1, -1, -1, -1, 0, 0, 0, 0, 1, 1, 1, 1]]
    for x in data:
        print("input: " + str(sorted(x))
              +"\n\tOriginal >> " + str(findSolution(x))
              + "\n\texperimental >> " + str(experimental(x))
              + "\n\tEditorial >> " + str(editorial(x))
              )
