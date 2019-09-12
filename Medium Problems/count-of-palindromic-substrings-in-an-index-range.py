"""
#M.36
Count of Palindromic substrings in an Index range
Given a string str of small alphabetic characters other than this we will be
given many substrings of this string in form of index tuples.
We need to find out the count of the palindromic substrings in given substring range.
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

[+]Temporal marker            : 12:25  Hours, | Thursday  Sept12, 19
[+]Temporal marker untethered : 12:28  Hours  | Thursday  Sept12, 19
[+]Comments                   : *Problem similar to find no. of palindromic substrings
                                *For the ranges just split the string as per range
                                *Rest of the algo is same
                                *Also the problem requires substring of length=1 also
                                *So jsut added the length of the string in the final ans also
                                *Problem is now solved
                                *Don't let go of that transgression acquired last night[+]Tread speed                : Relaxed
[+]Level                      : Easy
[+]Tread speead               : Paced
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
    return count-1+len(string)

if __name__ == "__main__":
    string = "aaaa"
    string = "aab"
    string = "abibs"
    string = "abcb"
    string = "abbaeae"
    string = "abaab"
    string = "xyaabax"
    ranges = [3, 5] #inclusive
    ranges = [2, 3]
    #string = "dsisbaafajih" #Manual Test case verified for integrity, Topic is closed:D
    length = len(string)
    print(findSolution(string[ranges[0]:ranges[1]+1]))
    #print(findSolution(string, 0, len(string)-1, 0))
