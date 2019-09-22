"""
#M.57

Length of Longest Balanced Subsequence
Given a string S, find the length of longest balanced subsequence in it. A balanced string is defined as:-

A Null string is a balanced string.
If X and Y are balanced strings, then (X)Y and XY are balanced strings.
Examples :

Input : S = "()())"
Output : 4

()() is the longest balanced subsequence 
of length 4.

Input : s = "()(((((()"
Output : 4
 
[+]Temporal marker            : 11:05, | Sunday Sept22, 19
[+]Temporal marker untethered : 11:19  | Sunday Sept22, 19
[+]Comments                   : *had a clear apporach in my mind
                                *Record time to implement the solution
                                *Problem is now closed
[+]Level                      : Baisc
[+]Tread speead               : Paced
[+]LINK                       : https://www.geeksforgeeks.org/length-longest-balanced-subsequence/
"""
#S-Complexity: O(1) | T-Complexity: O(N)
def findSolution(lis):
    length = len(lis)
    balanced_length = 0
    number_of_open_braces = 0
    if(length>0 and lis[0]=="("):
        number_of_open_braces = 1

    for i in range(1, length):
        if(lis[i]=="("):
            number_of_open_braces +=1
        elif(number_of_open_braces>0 ):
            number_of_open_braces -=1
            balanced_length += 2
    return balanced_length

#S-Complexity: O(N) | T-Complexity: O(N)
def findSolutionOb(lis):
    length = len(lis)
    dp = [0]*length
    count = 0
    if(len(lis)>0 and lis[0]=="("):
        dp[0] = 1
    for i in range(1, length):
        if(lis[i]==")"):
            if(dp[i-1]>0):
                dp[i] = dp[i-1]-1
                count+=2
        else:
            dp[i] = dp[i-1]+1
    return count

if __name__ == "__main__":
    string = "()())"
    string = "())))((("
    string = "((("
    string = "()(((((()"

    print("Balanced string length is: "+str(findSolution(string)))
