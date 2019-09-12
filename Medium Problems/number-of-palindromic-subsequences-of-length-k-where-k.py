"""
#M.34
Number of palindromic subsequences of length k where k <= 3
Given a string S of length n and a positive integer k. The task is to find
number of Palindromic Subsequences of length k where k <= 3.

Examples:

Input : s = "aabab", k = 2
Output : 4


Input : s = "aaa", k = 3
Output : 1



[+]Temporal marker            : N/A  Hours, | Wednesday Sept11, 19
[+]Temporal marker untethered : N/A  Hours  | Wednesday Sept11, 19
[+]Comments                   : *Couldn't solve on my own
                                *Solution help from GFG
                                *Didn't try beyond 1 hour
                                *Gave up too early
                                *Was restricted to tabulization approach
[+]Tread speed                : Relaxed
[+]Level                      : Medium
[+]LINK                       : https://www.geeksforg eeks.org/number-of-palindromic-subsequences-of-length-k-where-k/
"""
k =3
count = 0
def findSolution(string, k):
    dp = [[0]*(length+1) for x in range(length+1)]
    rev  = string[::-1]
    flag = 0
    index = [0, 0]
    for i in range(1, length+1):
        for j in range(1, length+1):
            if(rev[i-1]==string[j-1]):
                dp[i][j] = dp[i-1][j-1]+1
                if(dp[i][j]==3):
                    if(flag==0):
                        flag = 1
                        index[0] = i                
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])
                if(dp[i][j]==3):
                    index[1] = j
    import PrintMatrix as pm
    pm.printss(dp, string, rev)

    #print(index)
    a = set()
    for i in range(index[0], length+1):
        for j in range(index[1], length+1):
            #print("i: "+str(i)+" j: "+str(j))
            if(dp[i][j]==3):
                x = i
                y = j
                temp = ""
                while(x>0 and y>0):
                    if(rev[x-1]==string[y-1]):
                        temp+=rev[x-1]
                        x-=1
                        y-=1
                    else:
                        if(dp[x-1][y]>dp[x][y-1]):
                            x-=1
                        else:
                            y-=1
                
                a.add(temp)
    print(a)
    return len(a)
                    
if __name__ == "__main__":
    string = "aaaa"
    string = "aab"
    string = "abibs"
    string = "abcb"
    string = "aabab"
    string = "aaa"
    k = 3
    length = len(string)
    dp = [[-1]*(length) for x in range(length)]
    print(findSolution(string, k))
