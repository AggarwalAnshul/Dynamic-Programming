"""
Sort by Color
Asked in:
Facebook
Microsoft
Given an array with n objects colored red, white or blue,
sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: Using library sort function is not allowed.

Example :

Input : [0 1 2 0 1 2]
Modify array so that it becomes : [0 0 1 1 2 2]


[+]Temporal marker           : Fri, 17:9 | Feb 28, 20
[+]Temporal marker untethered: Fri, 17:14 | Feb 28, 20
[+]Comments                  : Cleared in first attempt
[+]Space Complexity          : O(1)
[+]Time Complexity           : O(N)
[+]Level                     : EASY
[+]Tread Speed               : PACED
[+]LINK                      : https://www.interviewbit.com/problems/sort-by-color
[+] Supplement Sources       : N/A
"""

def findSolution(lis):
    red_count = 0
    white_count = 0
    blue_count = 0

    for element in lis:
        if element == 0:
            red_count += 1
        elif element == 1:
            white_count += 1
        else:
            blue_count += 1
    length = len(lis)
    for index in range(length):
        if red_count > 0:
            lis[index] = 0
            red_count -= 1
        elif white_count > 0:
            lis[index] =1
            white_count -=1
        elif blue_count > 0:
            lis[index] = 2
            blue_count -= 1
    return lis

def experimental(lis):
    length = len(lis)
    pointer = [0, 0, 0]
    for element in lis:
        pointer[element] += 1
    for index in range(length):
        if pointer[0] > 0:
            lis[index] =0
            pointer[0] -=1
        elif pointer[1] > 0:
            lis[index] = 1
            pointer[1] -=1
        else:
            lis[index] = 2
    return lis

if __name__ == "__main__":
    data = [[0, 1, 2, 0, 1, 2]]
    for x in data:
        print("input: " + str(x) + " >> " + str(experimental(x)))