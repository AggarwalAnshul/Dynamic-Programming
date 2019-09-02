"""
#95
Size of array after repeated deletion of LIS
Given an array arr[0..n-1] of positive element. The task is to print remaining
elements of arr[] after repeated deletion of LIS (of size greater than 1).
If there are multiple LIS with same length, we need to choose the LIS that ends first.

Examples:

Input : arr[] = {1, 2, 5, 3, 6, 4, 1}
Output : 1
Explanation : 
{1, 2, 5, 3, 6, 4, 1} - {1, 2, 5, 6} = {3, 4, 1}
{3, 4, 1} - {3, 4} = {1}

Input : arr[] = {1, 2, 3, 1, 5, 2}
Output : -1
Explanation : 
{1, 2, 3, 1, 5, 2} - {1, 2, 3, 5} = {1, 2}
{1, 2} - {1, 2} = {}

Input : arr[] = {5, 3, 2}
Output : 3
[+]Temporal marker            : 12:15 Hours | Sept02, 2019
[+]Temporal marker untethered : 13:20 Hours | Sept02, 2019
[+]Comments                   : *LIS finding algo produced in record time
                                *LIS Printing algo also produced in record time
                                *Time took a hit during deletion of LIS form list and
                                *creating a driver function to repeat the process until the
                                *condition is satisfied
[+]LINK                       : https://www.geeksforgeeks.org/size-array-repeated-deletion-lis/
"""
#A function that prints the LIS from a lis
#input: DP, index of the LIS's last element, original list(array)
#Action: Prints the LIS from the lis(array)
#returns: None
def printLis(dp, index, lis):
    count = dp[index][0]
    LIS = []
    while(count>0):
        LIS.append(lis[index])
        index = dp[index][1]
        count-=1
    LIS.reverse()
    print("LIS is: "+str((LIS)))

#A Function that deletes the LIS from the original array(lis)
#input: dp, index of the last element of the LIS, original list(array)
#retursn: modified list i.e., list after deleting LIS from it
def deleteLis(dp, index, lis):
    count = dp[index][0]
    i = len(lis)-1
    tempLis = []
    while(count>0):
        if(i == index):
            index = dp[index][1]
            count-=1
        else:
            tempLis.insert(0, lis[i])
        i-=1
    #print(tempLis)
    return tempLis

#A function that finds the LIS in an array
#input: original array
#returns: [length of LIS, Index of the LIS's last element, dp]
def findLis(lis):
    length = len(lis)
    dp = [[1,0] for x in range(length)]
    dp[0 ] = [1,-1]
    globalMax = 0
    print("list is: "+str(lis))
    for i in range(length):
        localMax = 0
        for j in range(i):
            if(lis[j]<lis[i]):
                if(dp[j][0]+ 1 > dp[i][0]):
                    dp[i][0] = dp[j][0]+1
                    dp[i][1] = j
        if(dp[i][0] > dp[globalMax][0]):
            globalMax = i
    return [dp[globalMax][0], globalMax, dp]

#The driver function that consolidates all the action
#input: Original list(Array)
#output: Length of the modified list, i.e., after repeatedly deleting LIS from it
def findSolution(lis):
    flag = 0
    while(flag!=1 and len(lis)>0):
        data = findLis(lis)
        length = data[0]
        globalMax = data[1]
        dp = data[2]
        if(length > 1):
            printLis(dp, globalMax, lis)
            lis = deleteLis(dp, globalMax, lis)
            print("list after deletion is: "+str(lis))
        else:
            flag=1
    return len(lis)

#THE DRIVER FUNCTION      
if __name__ == "__main__":
    lis = [10, 9, 8, 7]
    lis = [5, 3, 2]
    lis = [1, 2, 5, 3, 6, 4, 1]
    lis = [1, 2, 3, 1, 5, 2]
    lis = [ 1, 2, 5, 3, 4 ]
    print("\nLength of the final modified list is: \n>> "+str(findSolution(lis)))

