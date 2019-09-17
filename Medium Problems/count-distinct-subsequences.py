"""
#M.42
Count Distinct Subsequences
Given a string, find the count of distinct subsequences of it.

Examples:

Input  : str = "gfg"
Output : 7
The seven distinct subsequences are "", "g", "f",
"gf", "fg", "gg" and "gfg" 

Input  : str = "ggg"
Output : 4
The four distinct subsequences are "", "g", "gg"
and "ggg"

[+]Temporal marker            : 11:10, | Monday Sept16, 19
[+]Temporal marker untethered : 10:53  | Monday Sept16, 19
[+]Comments                   : *Took an entire day
                                *Recursive algo developed in acceptable time
                                *Recursive algo is working flawlessly
                                *Took the entire day to devise DP Algo
                                *DP Algo not working
                                *Saw GFG Soln, still can't comeup with a dp algo
                                *Laying off for the time being
[+]Level                      : Medium
[+]Tread speead               : Relaxed / Paced
[+]LINK                       : https://www.geeksforgeeks.org/count-distinct-subsequences/
"""
"""
def findSolutionDP(string):
    length = len(string)
    dp = [0]*(length+2)
    
    dp[length-1] = 1
    count = 1
    lis = []
    lis.append(string[length-1])
 
    for x in range(length-2, -1, -1):
#        print(x)
        print(dp)
        dp[x] = count
        #print(str(string[x])+"storing dp[x]: "+str(dp[x]) + " for x: ")
        if(string[x]==string[x+1]):
            dp[x] = dp[x+1]
        if(string[x] not in lis):
            lis.append(string[x])
            dp[x]+=1
            #print(lis)
        #print(dp)
        count += dp[x]
    print(dp)
    print(lis)
    return count+1

"""
#Recursive Solution
def findSolutionDP(string):
    length = len(string)
    dp = [0]*(length+1)
    dic = {}
    for x in set(string):
        dic[x] = -1
    dp[0] = 1
    for x in range(1, length+1):
        dp[x] = dp[x-1]*2
        if(dic[string[x-1]] == -1):
            dic[string[x-1]] = x
        else:
            dp[x] -= dp[dic[string[x-1]]-1]
            dp[dic[string[x-1]]] = x
        print(dic)
    print(dp)
    

    
def findSolution(index, string, s, lis):
    if(index>=len(string)):
        if(s in lis):
            return 0
        else:
            print(s, end=" ")
            lis.append(s)
            return 1
    one = findSolution(index+1, string, s+string[index], lis)
    two = findSolution(index+1, string, s, lis)
    return one+two

if __name__ == "__main__":
    string = "ideg"
    string = "ggg"
    string = "gge"
    string = "gfg"

    string = "ideir"
    string = "gfgde"
    string = "ideggfir"
    string = "gedgfg"
    print(findSolutionDP(string))
    print(findSolution(0, string, "", []))
