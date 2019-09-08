"""
#M.13
Temple Offerings
Consider a devotee wishing to give offerings to temples along a mountain range. The temples are located in a row at different heights. Each temple should receive at least one offering. If two adjacent temples are at different altitudes, then the temple that is higher up should receive more offerings than the one that is lower down. If two adjacent temples are at the same height, then their offerings relative to each other does not matter. Given the number of temples and the heights of the temples in order, find the minimum number of offerings to bring.

Examples:

Input  : 3
         1 2 2
Output : 4
All temples must receive at-least one offering.
Now, the second temple is at a higher altitude
compared to the first one. Thus it receives one
extra offering. 
The second temple and third temple are at the 
same height, so we do not need to modify the 
offerings. Offerings given are therefore: 1, 2,
1 giving a total of 4.

Input  : 6
         1 4 3 6 2 1
Output : 10
We can distribute the offerings in the following
way, 1, 2, 1, 3, 2, 1. The second temple has to 
receive more offerings than the first due to its 
height being higher. The fourth must receive more
than the fifth, which in turn must receive more 
than the sixth. Thus the total becomes 10.

[+]Temporal marker            : 11:59 Hours | Thursday, Sept05, 19
[+]Temporal marker untethered : 12:19(N) Hours | Thursday, Sept05, 19
[+]Comments                   : DP Solution not understood, wasn't able to derive
                                Laying off the prob. until further light on the matter
[+]Tread speed                : Relaxed
[+]Level                      : Medium
[+]LINK                       : https://www.geeksforgeeks.org/temple-offerings/
"""

def findSolution(lis):
    length = len(lis)
    dp = [0]*length
    dp[0] = 1
    count = 0
    for i in range(1, length):
        if(lis[i]>lis[i-1]):
            dp[i] = dp[i-1]+1
        elif(lis[i]<=lis[i-1]):
            dp[i] = dp[i-1]-1
        if(dp[i]==0):
            x = i
            y = i-1
            while(lis[y]>lis[x]):
                dp[x]+=1
                y-=1
                x-=1
            dp[y]+=1
    for x in dp:
        count+=x
    #print(dp)
    return count

if __name__ == "__main__":
    lis = [1,2,2]
    lis = [1,4,3,6,7,98,4,3,0,2,1]
    print(findSolution(lis))
   
