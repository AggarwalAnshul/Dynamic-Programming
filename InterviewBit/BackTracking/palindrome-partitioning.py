"""
Programming Backtracking Palindrome Partitioning
Palindrome Partitioning
Asked in:
Amazon
Google
Given a string s, partition s such that every string of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

  [
    ["a","a","b"]
    ["aa","b"],
  ]
 Ordering the results in the answer : Entry i will come before Entry j if :
len(Entryi[0]) < len(Entryj[0]) OR
(len(Entryi[0]) == len(Entryj[0]) AND len(Entryi[1]) < len(Entryj[1])) OR
*
*
*
(len(Entryi[0]) == len(Entryj[0]) AND … len(Entryi[k] < len(Entryj[k]))
In the given example,


[+]Temporal marker           : 10:04 Hours | Tuesday 24, 2020
[+]Temporal marker untethered: 12:00 Hours | Thursday 26, 2020
[+]Comments                  : >>Took some real time to solve the problems
                                >>temporal markers are exagerrated
                                >>Didn't worked after 12 on Wednesday
                                >>Solved in around 1.5 - 2 hours today on Thursday
                                >>SOlved this solution w/o any hint or google whatsoever
                                >>This problem is making me feel real good
                                >> Editorial solution is much more elegant conceptually
                                >>Editorial solution has been flashed
                                >> Matter is closed now

[+]Space Complexity          : O(2^n)
[+]Time Complexity           : O(2^n)
[+]Level                     : MEDIUM
[+]Tread Speed               : Relaxed
[+]LINK                      : https://www.interviewbit.com/problems/nearest-smaller-element
[+] Supplement Sources       : N/A
"""
""" Obsolete Incorrect developments
def partition_obsolete(string):

    def driver(start, end, string, partition):
        if start == end:
            partition.append(string[start])
            print("return: "+str(partition))
            return partition
        elif (start+1== end and string[start]!=string[end]):
            partition.append(string[start])
            partition.append(string[end])
            print("return: "+str(partition))
            return partition
        elif string[start] == string[end]:
            partition.append(string[start:end+1])
            print("return: "+str(partition))
            return partition
        else:
            c = []
            a = driver(start+1, end, string, partition+[string[start]])
            b = driver(start, end-1, string, partition+[string[end]])
            if a:
                 c += [a]
            if b:
                c += [b]
            print("return: "+str(c))
            return c
    ans = driver(0, len(string)-1, string, [])
    return ans

def partition_partial(string):
    solution = []
    frontier = [ (0, len(string)-1, []) ]
    def isPalindrome(string):
        left, right = 0, len(string)-1
        while left < right:
            if not string[left] == string[right]:
                return 0
            left += 1
            right -= 1
        return 1
    while frontier:
        #print(str(frontier))
        left, right, partitions_so_far = frontier.pop()
        if left == right:
            partitions_so_far.append(string[right])
            solution.append(partitions_so_far)
            continue
        if isPalindrome(string[left:right+1]):
            print("adding: "+str(string[left : right+1]))
            solution.append(partitions_so_far+[string[left : right+1]])
        frontier.append((left, right-1, partitions_so_far+[string[right]]))
        frontier.append((left+1, right, partitions_so_far+[string[left]]))

    return (list(set(tuple((x)) for x in solution)))
"""

#Accepted Finally, I'm SO FREKAING HAPPYYYYYYY!!!!!!!!!!!!!!!!!!!!!!#
#   if it's palindrome:
#       if it's last element
#          add to solution and continue
#       add this to the partition
#  keep on building the palindrome candidate
def partition(string):
    frontier = [ ("", 0, [])]
    def isPalindrome(string):
        start, end = 0, len(string)-1
        while start <= end:
            if not string[start] == string[end]:
                return 0
            start, end = start+1, end-1
        return 1
    solution = []

    while frontier:
        print(frontier)
        string_so_far, index, partition_so_far = frontier.pop()

        if index == len(string):
            if not string_so_far or string_so_far and isPalindrome(string_so_far):
                solution.append(partition_so_far)
            continue

        new_string_so_far = string_so_far + string[index]
        if isPalindrome(new_string_so_far):
            if index+1 == len(string):
                solution.append(partition_so_far+[new_string_so_far])
                continue
            frontier.append(("", index+1, partition_so_far+[new_string_so_far]))
        frontier.append((new_string_so_far, index + 1, partition_so_far))

    return sorted(solution)

# Editorial Inspired
def partition_experimental(string):
    def driver(string, solution, partition):
        if len(string) == 0:
            solution.append(partition)
        for index in range(1, len(string)+1):
            if string[:index]==string[index-1::-1]:
                driver(string[index:], solution, partition+[string[:index]])
        return solution
    return driver(string, [], [])

if __name__ == '__main__':
    test_cases = [
        "cccaacbcaabb",
        "aea",
        "aba",
        "abc",
        "aab",
    ]
    for index in range(len(test_cases)):
        test_case = test_cases[index]
        print("input: "+str(test_case)+ "\nOUTPUT: "+str(partition_experimental(test_case)))