"""
#M.36
Count of Palindromic substrings in an Index range
Given a string str of small alphabetic characters other than this we will be given many substrings of this string in form of index tuples. We need to find out the count of the palindromic substrings in given substring range.
Examples:

Input : String str = "xyaabax"
           Range1 = (3, 5)   
           Range2 = (2, 3) 
Output : 4
         3
For Range1,  substring is "aba"
Count of palindromic substring in "aba" is 
four : "a", "b", "aba", "a"
For Range2,  substring is "aa"
Count of palindromic substring in "aa" is 
3 : "a", "a", "aa"

[+]Temporal marker            : 15:06  Hours, | Wednesday Sept11, 19
[+]Temporal marker untethered : 10:40  Hours  | Thursday  Sept12, 19
[+]Comments                   : *Laid it off for the day
                                *yesterday was pretty drowsy and low
                                *Solved in about an hour today
                                *Tried recursive apporach, redundant solution was computing up
                                *Tabulization worked fine
                                *One step closer to know LCS category inside out
                                *Matter is closed now
                                *Don't let go of that transgression acquired last night[+]Tread speed                : Relaxed
[+]Level                      : Medium
[+]LINK                       : https://www.geeksforg eeks.org/count-of-palindromic-substrings-in-an-index-range/
"""

#S-Complexity: O(N*N) | T-Complexity: O(N*N)
def findSolution(string):
    #init
    length = len(string)
    #dp[i][j] > 0 iff string[i:j+1] is a palindrome
    
    dp = [[0]*(length+1) for x in range(length+1)]
    for x in range(length):
        dp[x+1][x+1] = 1

    count = 1
    for i in range(length-1, 0, -1):
        for j in range(i, length+1):
            if(string[i-1]==string[j-1]):
                if(j-i==1):
                    dp[i][j] = count+1
                    count+=1
                elif(dp[i+1][j-1]>0):
                    dp[i][j] = count+1
                    count+=1
    
    import PrintMatrix as pm
    pm.printss(dp, string, string)
    return count-1

if __name__ == "__main__":
    string = "aaaa"
    string = "aab"
    string = "abibs"
    string = "abcb"
    string = "abbaeae"
    string = "abaab"
    string = "dsisbaafajih" #Manual Test case verified for integrity, Topic is closed:D
    length = len(string)
    print(findSolution(string))
    #print(findSolution(string, 0, len(string)-1, 0))
