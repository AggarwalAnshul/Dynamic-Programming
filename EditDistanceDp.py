"""
Edit Distance | DP-5
Given two strings str1 and str2 and below operations that can performed on str1. Find minimum number of edits (operations) required to convert ‘str1’ into ‘str2’.

Insert
Remove
Replace
All of the above operations are of equal cost.

Examples:

Input:   str1 = "geek", str2 = "gesek"
Output:  1
We can convert str1 into str2 by inserting a 's'.

Input:   str1 = "cat", str2 = "cut"
Output:  1
We can convert str1 into str2 by replacing 'a' with 'u'.

Input:   str1 = "sunday", str2 = "saturday"
Output:  3
Last three and first characters are same.  We basically
need to convert "un" to "atur".  This can be done using
below three operations. 
Replace 'n' with 'r', insert t, insert a
[+]Temporal marker            : Solved in acceptable time frames
[+]Temporal marker untethered :
[+]Tread speed                : Relaxed
[+]Comments                   : Didnt' expected to solve, trying an apporach led to the solution
                                However, the code couldnot be verfied from GFG
                                All Test cases passed succesfully,
                                Approach derived using LCS
[+]LINK: https://www.geeksforgeeks.org/edit-distance-dp-5/
"""
def reverseString(string):
    reverse = ""
    for x in range(len(string)-1,-1,-1):
        reverse+=string[x]
    return reverse

def printLCS(dp):
    i = len(dp)-1
    j = len(dp[0])-1
    string=""
    while(i!=0 and j!=0):
        if(two[i-1]==one[j-1]):
            string+=two[i-1]
            i-=1
            j-=1
        elif(dp[i-1][j]>dp[i][j-1]):
            i-=1
        else:
            j-=1
    return reverseString(string)
    
def lcs(one, two):
    lenOne = len(one)
    lenTwo = len(two)
    dp = [[0]*(lenOne+1) for x in range(lenTwo+1)]

    dp[0][0] = 0
    for i in range(1, lenTwo+1):
        for j in range(1, lenOne+1):
            #print(str(i)+" : "+str(j))
            if(two[i-1]==one[j-1]):
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    #print(printLCS(dp))
    common = dp[lenTwo][lenOne]
    if(len(one) <= len(two)):
        return(len(one)-common + (len(two)-len(one)))
    else:
        return(len(one)-common)

#one = "sunday"
#two = "saturday"
one = "sunday"
two = "saturday"
print(lcs(one, two))
