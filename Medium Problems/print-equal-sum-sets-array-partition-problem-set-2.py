"""
#M.23

Print equal sum sets of array (Partition problem) | Set 1
Given an array arr[]. Determine whether it is possible to split the array into
two sets such that the sum of elements in both the sets is equal. If it is possible,
then print both the sets. If it is not possible then output -1.

Examples :

 
Input : arr = {5, 5, 1, 11}
Output : Set 1 = {5, 5, 1}, 
         Set 2 = {11}
Sum of both the sets is 11 and equal.

Input : arr = {1, 5, 3}
Output : -1
No partitioning results in equal sum sets.

[+]Temporal marker            : 19:34    Hours, | Monday Sept09, 19
[+]Temporal marker untethered : 19:40    Hours  | Monday Sept09, 19
[+]Comments                   : Knew the approach, just implemented 
[+]Tread speed                : Paced
[+]Level                      : Easy
[+]LINK                       : https://www.geeksforg eeks.org/partition-problem-dp-18/
"""

#S-Complexity: O(sum*lis size) | T-Complexity: O(sum*lis size)
def findSolution(lis):
    halfSum = 0
    for x in lis:
        halfSum += x
    if(halfSum%2!=0):
        return False
    halfSum = int(halfSum/2)
    length = len(lis)
    dp = [[0]*(length+1) for x in range(halfSum+1)]
    dp[0] = [1]*(length+1)

    for i in range(1, halfSum+1):
        for j in range(1, length+1):
            dp[i][j] = dp[i][j-1]
            if(i>=lis[j-1]):
                dp[i][j] += dp[i-lis[j-1]][j-1]
    import PrintMatrix as pm
    pm.printss(dp)

    if (dp[halfSum][length]>=1):
           #Reading the set
        stack =  []
        sumCount = halfSum
        while(sumCount!=0):
            for x in range(1, length):
                if(dp[sumCount][x]==1):
                    stack.append(lis[x-1])
                    sumCount -= lis[x-1]
                    break
        for x in stack:
            lis.remove(x)
        print("first set is: "+str(lis))
        print("second set is: :"+str(stack))     
        return True
    return False

if __name__ == "__main__":
    lis = [1, 5, 13, 5]
    lis = [1,5,3]
    lis = [1, 5, 11, 5]
    Lis = [3, 1, 1, 2, 2, 1]
    print(findSolution(lis))
