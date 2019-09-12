"""
#M.31
Count All Palindrome Sub-Strings in a String | Set 1
Given a string, the task is to count all palindrome sub
string in a given string. Length of palindrome sub string is greater than or equal to 2.

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
[+]LINK                       : https://www.geeksforg eeks.org/count-palindrome-sub-strings-string/
"""

#S-Complexity: O(N*N) | T-Complexity: O(N*N)
def findSolution(string):
    #init
    length = len(string)
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
    length = len(string)
    print(findSolution(string))
    #print(findSolution(string, 0, len(string)-1, 0))
