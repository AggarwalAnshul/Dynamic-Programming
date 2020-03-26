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


[+]Temporal marker           : 13:24 Hours | Tuesday 24, 2020
[+]Temporal marker untethered: 19:51 Hours | Tuesday 24, 2020
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

def generateParenthesis(num):
    #num = data*2
    solution = set()
    solution.add( ("()") )
    for index in range(2, num+1):
        temp = set()
        for item in solution:
            print("Item: "+str(item))
            temp.add("("+item+")")
            temp.add("()"+item)
            temp.add(item+"()")
        solution = temp
    return sorted(solution)

if __name__ == '__main__':
    print(generateParenthesis(4))
