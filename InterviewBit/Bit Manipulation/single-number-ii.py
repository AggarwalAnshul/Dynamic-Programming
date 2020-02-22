"""
Given an array of integers, every element appears thrice except for one which occurs once.

Find that element which does not appear thrice.

Note: Your algorithm should have a linear runtime complexity.

Could you implement it without using extra memory?

Input Format:

    First and only argument of input contains an integer array A
Output Format:

    return a single integer.
Constraints:

2 <= N <= 5 000 000
0 <= A[i] <= INT_MAX
For Examples :

Example Input 1:
    A = [1, 2, 4, 3, 3, 2, 2, 3, 1, 1]
Example Output 1:
    4
Explanation:
    4 occur exactly once
Example Input 2:
    A = [0, 0, 0, 1]
Example Output 2:
    1

[+]Temporal marker           : Fri, 20:15 | Feb 21, 20
[+]Temporal marker untethered: Fri, 20:15 | Feb 21, 20
[+]Comments                  : Though i Did solve the problem with T:O(N) | S:O(N)
                                I couldn't devised the most efficient solution
                                iB Hint was not of much help
                                Breakthrough came form GFG Sources, where i read the approach
                                and it donned on me instantly, implemented on my own
                                SUbmitted in first attempt
                                Matter is closed for now
                                Great problem
[+]Space Complexity          : O(N)
[+]Time Complexity           : O(1)
[+]Level                     : MEDIUM
[+]Tread Speed               : Relaxed
[+]LINK                      : https://www.interviewbit.com/problems/single-number-ii
[+] Supplement Sources       : https://www.geeksforgeeks.org/find-the-element-that-appears-once/
"""


def experimental(lis):
    answer = 0
    for bit in range(32):
        count = 0
        for element in lis:
            if element & 1 << bit:
                count += 1
        if count % 3 != 0:
            answer ^= 1 << bit
    return answer


# TLE Solution Time: O(N) | Space: O(N)
def findSolution(lis):
    mask = 0
    flag = 0
    answer = 0
    for element in lis:
        if mask & 1 << element:
            # this has to be second occurrence of the element
            answer ^= element
            flag |= 1 << element
            mask ^= 1 << element
        else:
            # this can be first or third occurrence
            if flag & 1 << element:
                # this is the third occurrence of the element
                pass
            else:
                # this is the first occurrence
                mask ^= 1 << element
                answer ^= element
    return answer


if __name__ == "__main__":
    data = [[1, 2, 4, 3, 3, 2, 2, 3, 1, 1],
            [890, 992, 172, 479, 973, 901, 417, 215, 901, 283, 788, 102, 726, 609, 379, 587, 630, 283, 10, 707, 203,
             417, 382, 601, 713, 290, 489, 374, 203, 680, 108, 463, 290, 290, 382, 886, 584, 406, 809, 601, 176, 11,
             554, 801, 166, 303, 308, 319, 172, 619, 400, 885, 203, 463, 303, 303, 885, 308, 460, 283, 406, 64, 584,
             973, 572, 194, 383, 630, 395, 901, 992, 973, 938, 609, 938, 382, 169, 707, 680, 965, 726, 726, 890, 383,
             172, 102, 10, 308, 10, 102, 587, 809, 460, 379, 713, 890, 463, 108, 108, 811, 176, 169, 313, 886, 400, 319,
             22, 885, 572, 64, 120, 619, 313, 3, 460, 713, 811, 965, 479, 3, 247, 886, 120, 707, 120, 176, 374, 609,
             395, 811, 406, 809, 801, 554, 3, 194, 11, 587, 169, 215, 313, 319, 554, 379, 788, 194, 630, 601, 965, 417,
             788, 479, 64, 22, 22, 489, 166, 938, 66, 801, 374, 66, 619, 489, 215, 584, 383, 66, 680, 395, 400, 166,
             572, 11, 992],
            [10, 20, 10, 30, 10, 30, 30]
            ]
    for x in data:
        print("input: " + str(x) + " >> " + str(findSolution(x)) +
              " | Experimental : "+str(experimental(x)))
