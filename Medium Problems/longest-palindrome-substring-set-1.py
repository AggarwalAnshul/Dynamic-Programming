"""
#M.31

Longest Palindromic Substring | Set 1
Given a string, find the longest substring which is palindrome. For example,
if the given string is “forgeeksskeegfor”, the output should be “geeksskeeg”.

[+]Temporal marker            : N/A  Hours, | Tuesday Sept10, 19
[+]Temporal marker untethered : N/A  Hours  | Wednesday Sept11, 19
[+]Comments                   : *length was found in acceptable timeframe
                                *Printing the solution took some time
                                *Laid it off
                                *Solved next day in under an hour
[+]Tread speed                : Paced
[+]Level                      : Medium
[+]LINK                       : https://www.geeksforg eeks.org/longest-palindrome-substring-set-1/
"""

def printSequence(dp, string, rev, index):
    length = len(dp)
    i = index[0]
    j = index[1]
    ret = ""
    while(dp[i][j]>0):
        #print("i: "+str(i)+" j: "+str(j))
        if(rev[i-1]==string[j-1]):
            ret += rev[i-1]
            #print(rev[i-1], end=" ")
            i-=1
            j-=1
    return ret
    
   
    
def findSolution(string):
    length = len(string)
    rev = string[::-1]
    dp = [[0]*(length+1) for x in range(length+1)]

    index = [0, 0]
    for i in range(1, length+1):
        for j in range(1, length+1):
            if(rev[i-1]==string[j-1]):
                dp[i][j] = 1
                if(i-2>=0):
                    if(rev[i-2]==string[j-2]):
                        dp[i][j] = dp[i-1][j-1]+1
            if(dp[i][j]>dp[index[0]][index[1]]):
                index = [i,j]
    import PrintMatrix as pm
    pm.printss(dp, string, rev)
    answer = printSequence(dp,string, rev, index) 
    print(len(answer))
    return (answer)
if __name__ == "__main__":
    string = "ansisnb"
    string = "forgeeksskeegfor"
    string = "absbpar"
    string = "abcd"
    string = "geeks"
    string = "geeeg"
    string = "geekeg"
    string = "abcbdffb"
    string = "abacdgfdcaba"
    print(findSolution(string))
