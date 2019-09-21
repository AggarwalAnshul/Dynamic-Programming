"""
#M.50

Printing longest Increasing consecutive subsequence
Given n elements, write a program that prints the longest increasing
subsequence whose adjacent element difference is one.

Examples:

Input : a[] = {3, 10, 3, 11, 4, 5, 6, 7, 8, 12}
Output : 3 4 5 6 7 8
Explanation: 3, 4, 5, 6, 7, 8 is the longest increasing subsequence whose adjacent element differs by one.

Input : a[] = {6, 7, 8, 3, 4, 5, 9, 10}
Output : 6 7 8 9 10
Explanation: 6, 7, 8, 9, 10 is the longest increasing subsequence

Recommended: Please try your approach on {IDE} first, before moving on to the solution.
We have discussed how to find length of Longest Increasing consecutive subsequence. To print the subsequence, we store index of last element. Then we print consecutive elements ending with last element.

Given below is the implementation of the above approach:

[+]Temporal marker            : 18:00, | Saturday Sept21, 19
[+]Temporal marker untethered : 18:20  | Saturday Sept21, 19
[+]Comments                   : *Easy peasy lemon squeezy!
                                *Had a clear approach in my worked that worked flawlessly
                                *Problem is now closed
[+]Level                      : Basic
[+]Tread speead               : Paced
[+]LINK                       : https://www.geeksforgeeks.org/printing-longest-increasing-consecutive-subsequence/
"""

def printLIS(dp, lis, index):
    count = dp[index][0]
    ans = []
    while(count>0):
        ans.insert(0, lis[index])
        index = dp[index][1]
        count-=1
    return ans

def findSolution(lis):
    length = len(lis)
    dp = [[1,-1] for x in range(length)]
    localMax = [0,0]
    index = 0

    for i in range(1, length):
        #print("looking for index: "+ str(lis[i]))
        localMax = [1, -1]
        for j in range(i):
            #print("\tChecking for: "+str(lis[j]))
            if(lis[i]-lis[j]==1):
                #print("\t\tMatch found...")
                if(dp[j][0]+1 >= localMax[0]):
                    localMax[0] = dp[j][0]+1
                    localMax[1] = j
                    #print("\t\t\tValue is incremented to: "+str(localMax[0]))
        dp[i] = [localMax[0], localMax[1]]
        #print(dp)
        if(dp[index][0] < dp[i][0]):
            index = i
    return(printLIS(dp, lis, index))
    
if __name__ == "__main__":
    lis = [3, 10, 3, 11, 4, 5, 6, 7, 8, 12]
    lis = [99, 3, 10, 3, 11, 4, 5, 6, 7, 8, 12]
    lis = [100,101,102,103,6,104,105,106, 7, 8, 3, 4, 5, 9, 10]
   
    print(findSolution(lis))

    
