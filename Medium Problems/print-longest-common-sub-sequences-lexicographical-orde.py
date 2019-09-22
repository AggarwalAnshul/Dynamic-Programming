"""
#M.55
Print all longest common sub-sequences in lexicographical order

You are given two strings.Now you have to print all longest common sub-sequences in lexicographical order?

Examples:

Input : str1 = "abcabcaa", str2 = "acbacba"
Output: ababa
        abaca
        abcba
        acaba
        acaca
        acbaa
        acbca
        
 
[+]Temporal marker            : 09:30, | Sunday Sept22, 19
[+]Temporal marker untethered : 09:15  | Sunday Sept22, 19
[+]Comments                   : *had a clear apporach in my mind
                                *Record time to implement the solution
                                *Problem is now closed
[+]Level                      : Baisc
[+]Tread speead               : Paced
[+]LINK                       : https://www.geeksforgeeks.org/find-distinct-subset-subsequence-sums-array/
"""
#S-Complexity: O(Sum(N)) | T-Complexity: O(N*sum(N))
def printLCS(dp, one, two, i, j, string):
    ans = string
    lis =[]
    while(i>0 and j>0):
        if(one[j-1] == two[i-1]):
            ans = two[i-1]+ans
            i-=1
            j-=1
        elif(dp[i-1][j] == dp[i][j-1]):
            print(printLCS(dp, one, two, i-1, j, ans))
            print(printLCS(dp, one, two, i, j-1, ans))
            i = 0
            j = 0
        elif(dp[i-1][j] > dp[i][j-1]):
            i-=1
        else:
            j-=1
    return ans
def append(lis, a):
    print("appendding: "+a+" in the lis: "+str(lis))
    length = len(lis)
    new = []
    for i in range(length):
        new.append(lis[i]+a)
    print("returning the lis: "+str(lis))
    return new

def findSolution(one, two):
    lenOne = len(one)
    lenTwo = len(two)
    dp = [ [ [0,[""]] for y in range(lenOne+1)] for x in range(lenTwo+1)]

    for i in range(1, lenTwo+1):
        for j in range(1, lenOne+1):
            if(one[j-1]==two[i-1]):
                dp[i][j][0] = dp[i-1][j-1][0] + 1
                dp[i][j][1] = append(dp[i-1][j][1], two[i-1]) + append(dp[i][j-1][1], two[i-1])
            elif(dp[i-1][j][0] > dp[i][j-1][0]):
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i][j-1]
    import PrintMatrix as pm
    pm.printss(dp, one, two)
    print(dp[lenTwo][lenOne])
    print(set(dp[lenTwo][lenOne][1]))
if __name__ == "__main__":

    lis = ["abcabcaa", "acbacba"]
    print(findSolution(lis[0], lis[1]))

    
