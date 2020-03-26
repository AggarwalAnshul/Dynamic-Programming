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
[+]Comments                  : >> The solution was easy per-se
                                >> the desecription was shitty!
                                >> it was literally though i was adding fix for all the corner cases
                                >> finally "12" gave me real idea, what was the expected output!
                                >> really pathetic description

[+]Space Complexity          : O(3^n)
[+]Time Complexity           : O(3^n)
[+]Level                     : EASY
[+]Tread Speed               : Paced
[+]LINK                      : https://www.interviewbit.com/problems/nearest-smaller-element
[+] Supplement Sources       : N/A
"""
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

#Accepted FInally, I'm SO FREKAING HAPPYYYYYYY!!!!!!!!!!!!!!!!!!!!!!
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
        string_so_far, index,partition_so_far = frontier.pop()
        if index == len(string):
            if not string_so_far:
                print("adding >> "+str(partition_so_far))
                solution.append(partition_so_far)
            continue

        if string_so_far:
            new_string_so_far = string_so_far + string[index]
            if isPalindrome(new_string_so_far):
                # 1. add it to the partition
                frontier.append(("", index+1, partition_so_far+[new_string_so_far]))
                # 2. keep on building the palindrome candidate
                frontier.append((new_string_so_far, index+1, partition_so_far))
            else:
                if index+1 == len(string):
                    if isPalindrome(new_string_so_far):
                        solution.append(partition_so_far+[new_string_so_far])
                else:
                    # keep on building the candidate
                    frontier.append((new_string_so_far, index+1, partition_so_far))
        else:
            # 1. build the string
            frontier.append((string[index], index+1, partition_so_far))
            # 2. add to partition
            frontier.append(("", index+1, partition_so_far+[string[index]]))

    # while frontier:
    #     print(str(frontier))
    #     string_so_far, index, partition_so_far = frontier.pop()
    #     if index == len(string):
    #         print("\t\t\tAdding: "+str(partition_so_far))
    #         solution.append(partition_so_far)
    #         continue
    #
    #
    #     # Choice1: This is a palindrome part
    #     if not string_so_far:
    #         frontier.append(("", index + 1, partition_so_far + [string[index]]))
    #
    #     if not string_so_far:
    #         frontier.append((string_so_far + string[index], index + 1, partition_so_far))
    #         if not index + 1 == len(string):
    #             pass
    #             # this builds the palindrome candidate
    #
    #     else:
    #         if isPalindrome(string_so_far+string[index]):
    #             # this adds the palindrome to the partition
    #             frontier.append(("", index+1, partition_so_far+[string_so_far+string[index]]))
    #             frontier.append((string_so_far + string[index], index + 1, partition_so_far))
    #             if not index+1 == len(string):
    #                 pass
    #                 # this builds teh palindrome candidate
    #
    #         else:
    #             continue
    #     # Choice 2: This is not a part of Palindrome

    return sorted(solution)

if __name__ == '__main__':
    test_cases = [
        "cccaacbcaabb",
        "aea",
        "aba",
        "abc",
        "aab",
    ]
    for index in range(1):
        test_case = test_cases[index]
        print("input: "+str(test_case)+ "\nOUTPUT: "+str(partition(test_case)))