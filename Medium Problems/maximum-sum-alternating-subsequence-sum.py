"""
#M.38
Maximum sum alternating subsequence
Given an array, the task is to find sum of maximum sum alternating subsequence starting with first element. Here alternating sequence means first decreasing, then increasing, then decreasing, … For example 10, 5, 14, 3 is an alternating sequence.

Note that the reverse type of sequence (increasing – decreasing – increasing -…) is not considered alternating here.

Examples:

Input :  arr[] = {4, 3, 8, 5, 3, 8}  
Output :  28
Explanation:
The alternating subsequence (starting with first element) 
that has above maximum sum is {4, 3, 8, 5, 8}

Input : arr[] = {4, 8, 2, 5, 6, 8} 
Output :  14
The alternating subsequence (starting with first element) 
that has above maximum sum is {4, 2, 8}

[+]Temporal marker            : N/A, | Saturday Sept14, 19
[+]Temporal marker untethered : N/A  | Saturday Sept14, 19
[+]Comments                   : Took a couple of hour
                                Developed the recursive algo on my own
                                Recursion looks good
                                DP Solution is not understandable
                                Laying off for now
[+]Level                      : Medium
[+]Tread speead               : Relaxed / Paced
[+]LINK                       : https://www.geeksforg eeks.org/maximum-sum-alternating-subsequence-sum/
"""

def findSolutionDP(lis):
    length = len(lis)
    #init
    dp = [[0]*length for x in range(2)]
    dp[0][0] = dp[1][0] = lis[0]
    flag = 0
    ans = 0
    for x in range(1, length):
        for y in range(x):
            if(lis[y]>lis[x]):
                dp[1][x] = max(dp[1][x], dp[0][y]+lis[x])
                flag = 1
            if(lis[y]<lis[x] and flag==1):
                dp[0][x] = max(dp[0][x], dp[1][y]+lis[x])    
        #print(dp)
    ans = max(ans, dp[0][x], dp[1][x])
    return ans
def findSolution(index, last, save, polarity, lis):
    if(index>=len(lis)):
        return save
    curPolarity = -1
    if(lis[index]>last):
        curPolarity = 1
    if(curPolarity==polarity):
        return findSolution(index+1, lis[index], save+lis[index], polarity*-1, lis)
    else:
        if(index==1):
            return findSolution(index+1, last, save, polarity, lis)
        return max(findSolution(index+1, last, save, polarity, lis),
                   findSolution(index+1, lis[index], save-last+lis[index], polarity, lis))

if __name__ == "__main__":
    lis = [4, 8, 2, 5, 6, 8]
    lis = [4, 3, 8, 5, 3, 8]
  
    print(findSolutionDP(lis))
    print("computing using recursive solution...")
    print(findSolution(1, lis[0], lis[0], -1, lis))
