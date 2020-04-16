"""

Programming Checkpoint: Level 5 Longest Consecutive Sequence
Longest Consecutive Sequence
Asked in:  
Amazon
Google
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Example:
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.

"""
'''

[+]Temporal marker           : 17:41 Hours | Wednesday 15, 2020
[+]Temporal marker untethered: 11:38 Hours | Thursday 16, 2020
[+]Comments                  : Devised the solution in about 10 minutes today
                                *Laid off the problem yesterday after about 30 minutes
                                *No hint used, whatsoever
                                *Happy with the solution
                                *Much shorter | Cleaner than editorial solution
                                *Editorial is understood, but i like mine more
                                *Matter is closed now.

[+]Space Complexity          : O(N)
[+]Time Complexity           : O(N)
[+]Level                     : MEDIUM
[+]Tread Speed               : Relaxed
[+]LINK                      : https://www.interviewbit.com/problems/nearest-smaller-element
[+] Supplement Sources       : N/A

'''

# ACCEPTED!
def longestConsecutive(lis):
    hashset, ans = set(lis), 0
    for value in lis:
        if value+1 in hashset:
            continue
        preceeding_value, count = value-1, 1
        while preceeding_value in hashset:
            preceeding_value, count = preceeding_value-1, count+1
        ans = max(ans, count)
    return ans

if __name__ == '__main__':
    test_cases = [
        [-3, -1, 0, 1, 2, 3, 4, 5, 6, 7, 9, 10, 16],
        [100, 4, 200, 1, 3, 2],
        [-5],
        [7, 9],
        [65, 7, 3, 29, 39, -3, 87, 85, 21, 22, 108, 89, 54, 120, 92, 1, 72, 80, 9, 117, 16, 96, 34, 4, 119, 61, 84, 35, 99, 113, 18, 59, 42, 62, -1, 69, 48, 52, 2, 102, 40, 28, 74, 104, 23, 90, 44, 0, 47, 5, 43, 111, 6, 60, 46, 10, 63, 68],
    ]
    for index in range(len(test_cases)):
        test_case = test_cases[index]
        print("Input; "+str(test_case)+"\n\toutput: "+str(longestConsecutive(test_case)))
