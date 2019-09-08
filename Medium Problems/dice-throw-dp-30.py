"""
#M.15

Dice Throw | DP-30
Given n dice each with m faces, numbered from 1 to m, find the number of ways to get
sum X. X is the summation of values on each face when all the dice are thrown.

[+]Temporal marker            : 13:23 Hours,  | Sunday, Sept08, 19
[+]Temporal marker untethered : N/A,          | Sunday, Sept08, 19
[+]Comments                   : Had lunch, Saw The Good Wife, Sat in common areaa,
                                Implementation took 2 hours max i Guess,
                                Initial, Approach was in my head
                                Took some time to fine tune the approach
                                Devised the approach from coin change problem, or atleast i think i did
                                From coin change with Rep to coin change and then finally the current!
                                All test cases passed
                                Matter closed, Pushing now
[+]Tread speed                : Relaxed
[+]Level                      : Easy
[+]LINK                       : https://www.geeksforgeeks.org/dice-throw-dp-30/
"""

import PrintMatrix as pm
import math

#S-Complexity: O(sum*dices*faces) | T-Complexity: O(sumcount*dices*faces)
#Space complexity can be reduces to O(sum*faces) by runnig the loop on the same copy of layer
#Too lazy to implement and honestly i'm tired of debugging this code..PHEW!
def findSolution(sumCount, dices, faces):
    #dp = [sumCount+1][faces+1][dices+1]
    dp = [[[0]*(faces+1) for x in range(sumCount+1)] for k in range(dices)]

    #init
    for dice in range(dices):
        for face in range(faces+1):
            dp[dice][0][face] = 1
    #pm.printsss(dp)
            
    print("Printing the initial last layer")
    for i in range(1, sumCount+1):
        for j in range(1, faces+1):
            dp[dices-1][i][j] = dp[dices-1][i][j-1]
            if(i==j):
                dp[dices-1][i][j] = 1
    pm.printss(dp[dices-1]) #The last layer


    for layer in range(dices-2, -1, -1):
        for i in range(1, sumCount+1):
            print("i: "+str(i))
            for j in range(1, faces+1):
                    print("j: "+str(j)+" looking for: "+str(i-j)+" in layer: "+str(layer+1))
                    dp[layer][i][j] = dp[layer][i][j-1]
                    if(i-j>0):
                        if(dp[layer+1][i-j][faces]>0):
                            dp[layer][i][j] += dp[layer+1][i-j][faces]
                            print("Added value..."+str(dp[layer+1][i-j][faces]))
            pm.printss(dp[layer])

    return dp[0][sumCount][faces] 
if __name__ == "__main__":
    #lis = [sum, dices, faces]
    lis = [8, 3, 6]
    lis = [1, 2, 4]
    lis = [3, 2, 2]
    lis = [5, 2, 4]
    lis = [5, 3, 4]
    print(findSolution(lis[0], lis[1], lis[2]))
    #import DiceThrow
    #print("Fetching solution from GFG for debugging purposes...")  
    #print(DiceThrow.findWays(lis[2], lis[1], lis[0]))

