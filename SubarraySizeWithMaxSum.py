"""
Size of The Subarray With Maximum Sum
An array is given, find length of the subarray having maximum sum.

Examples :

Input :  a[] = {1, -2, 1, 1, -2, 1}
Output : Length of the subarray is 2
Explanation: Subarray with consecutive elements 
and maximum sum will be {1, 1}. So length is 2

Input : ar[] = { -2, -3, 4, -1, -2, 1, 5, -3 }
Output : Length of the subarray is 5
Explanation: Subarray with consecutive elements 
and maximum sum will be {4, -1, -2, 1, 5}.

Temporal maker: 14:12 Hours | Aug20, Tuesday

"""

def findSubarraySizeWithMaximumSum(lis):
    length = len(lis)
    count = 0
    sumCount = 0
    maxCount = 0
    for x in range(0, length):
        ele = lis[x]
        if(ele+sumCount<=0):
            maxCount = max(maxCount, count)
            count = 0
            sumCount = 0 
        else:
            if(ele+sumCount < sumCount):
                maxCount = max(maxCount, count)
            count+=1
            sumCount += ele
        print(str(ele)+" count: "+str(count)+" sum:" +str(sumCount))
    maxCount = max(maxCount, count)
    print(maxCount)

#lis = [-2, -3, 4, -1, -2, 1, 5, -3]
lis = [1, -2, 1, 1, -2, 1]
findSubarraySizeWithMaximumSum(lis)
