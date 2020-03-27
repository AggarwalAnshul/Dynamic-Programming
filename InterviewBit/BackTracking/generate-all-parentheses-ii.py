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
[+]Temporal marker untethered: 12:43 Hours | Friday 27m, 2020
[+]Comments                  : >>The logic behind this was pretty nify
                                >> mine solution was generating partial answer
                                >> breakthrough was editoral hint
                                >> "NUMBER OF CLOSE BRACE MUST NOT EXCEED OPEN BRACKET AT ANY GIVEN TIME"
                                >> after reading this hint i knew i got the solutino
                                >> the pity is i couldn't come up to this observation
                                >> I did crack that ")" cannot exceed "N" at any given time
                                >> Failed to observe the condition for ")" also
                                >> Anyhow, matter is officially closed now.
[+]Space Complexity          : O(2^n)
[+]Time Complexity           : O(2^n)
[+]Level                     : MEDIUM
[+]Tread Speed               : Relaxed
[+]LINK                      : https://www.interviewbit.com/problems/nearest-smaller-element
[+] Supplement Sources       : N/A

"""

# GARBAGE/INCOMPLETE/PARTIAL/INCORRECT SOLUTIONS
"""
def generateParenthesis_abandoned(num):
    def enclose(string):
        stack = []
        solution = []
        temp = 0
        # print("enclsoing on: "+string)
        for index in range(len(string)):
            brace = string[index]
            if brace == "(":
                stack.append(index)
            if brace == ")":
                while True:
                    temp = stack[-1]
                    if string[stack.pop()] == "(":
                        break
            if not stack:
                solution.append(string[0:temp] + "(" + string[temp:index + 1] + ")" + string[index + 1:])
        return solution

    #num = data*2
    solution = set()
    solution.add( ("()") )
    for index in range(2, num+1):
        temp = set()
        for item in solution:
            print("Item: "+str(item))
            temp.add("("+item+")")
            temp.add("()"+item)
            for x in enclose(item):
                temp.add(x)
        solution = temp
    return sorted(solution)
def enclose(string):
        stack = []
        solution = []
        temp = 0
        # print("enclsoing on: "+string)
        for index in range(len(string)):
            brace = string[index]
            if brace == "(":
                stack.append(index)
            if brace == ")":
                while True:
                    temp = stack[-1]
                    if string[stack.pop()] == "(":
                        break
            if not stack:
                solution.append(string[0:temp] + "(" + string[temp:index + 1] + ")" + string[index + 1:])
        return solution
def invert(string):
    temp = ""
    for char in reversed(string):
        temp += ")" if char == "(" else "("
    return string+temp


def generateParenthesis_partialAnswer(slots):
    if slots < 1:
        return []
    if slots == 1:
        return ["()"]
        return [ "()()", "(())"]
    generations = set()
    for pattern in generateParenthesis(slots-1):
        generations.add("()"+pattern)
        generations.add(pattern+"()")
        generations.add("("+pattern+")")
    for pattern in generateParenthesis(slots-2):
        generations.add("(())" + pattern)
        generations.add(pattern + "(())")
        generations.add("((" + pattern + "))")
    return sorted(list(generations))

def generateParenthesis_partialAnswer(slots):
    frontier = [ (1, "()")]
    solution = set()
    while frontier:
        slots_filled, generations = frontier.pop()
        if slots_filled == slots:
            solution.add(generations)
            continue
        frontier.append((slots_filled+1, "()"+generations))
        frontier.append((slots_filled+1, generations+"()"))
        frontier.append((slots_filled+1, "("+generations+")"))
    return sorted(list(solution))
"""

#ACCEPTED SOLUTION
# @param slots: number of pair of parenthesis
# returns list, containing all valid permutation of parenthesis
# APPROACH:
# at any given point of time
#   ")" must not exceed "N"
#   "(" must be less than number of ")"
def generateParenthesis(slots):
    frontier, solution = [(0, 0, "")], []
    while frontier:
        open_braces, close_braces, pattern = frontier.pop()
        if open_braces == slots and close_braces == slots:
            solution.append(pattern)
            continue
        if open_braces + 1 <= slots:
            frontier.append((open_braces + 1, close_braces, pattern + "("))
        if close_braces + 1 <= open_braces:
            frontier.append((open_braces, close_braces + 1, pattern + ")"))
    return solution[::-1]

if __name__ == '__main__':
    print(generateParenthesis(4))