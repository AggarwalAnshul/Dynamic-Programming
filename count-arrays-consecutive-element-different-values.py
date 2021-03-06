"""
#88
Count of arrays having consecutive element with different values
Given three positive integers n, k and x. The task is to count the number of different array that can be formed of size n such that each element is between 1 to k and two consecutive element are different. Also, the first and last elements of each array should be 1 and x respectively.

Examples :

Input : n = 4, k = 3, x = 2
Output : 3



[+]Temporal marker            : Didnt' Tether N/A     | N/A
[+]Temporal marker untethered : N/A Took several days | Sept03, 2019, Tuesday
[+]Comments                   : This was one of the toughest problem from GFG BProblems.
                                Took several days, but didnt' even peeked at the GFG solution.
                                I had this feeling in the back of my mind that i can crack this
                                after some brainstorming, and was in relentless pursuit of it. laid
                                it off for somme time and solved several other problems in the midst
                                and tried it over and over again. Ultimately when i was just to give up
                                i Tried reading the apporach on GFG, and after reading this line a new
                                approach struck me, basically what a state can be here"""
                                #First of all, notice that the answer is same for all x from
                                #2 to k. Can easily be proved. This will be useful later on.
                                #Let the state f(i) denote the number of ways to fill the range
                                #[1, i] of array A such that A1 = 1 and Ai ≠ 1.
"""                             Initial cold pressing showed prospective and significant results
                                ,tried for over and hour until I finally devised the algorithm,
                                thought it starkly differes from the GFG Solution yet, its correct
                                and i can bet my life on its correctness, has been passed through
                                comprehensive scrutiny.
                                HENCE FROM THE POWER VESTED IN ME BY THE GOD I, HEREBY SENTENCE
                                THIS MATTER CLOSED HENCEFORTH!
                                Damn, that was a long comment! like really really long, i've to
                                work on the length!!!!!!!!
[+]Level                      : HARD AF :( Phew!
[+]LINK                       : https://www.geeksforgeeks.org/count-arrays-consecutive-element-different-values/
"""


def findSolution(length, nodes, last):
    dp = [[0]*2 for x in range(length)]
    dp[0] = [1,0]

    #one is the node(array) with 1 as the last element
    #diff is the node(array) with any other number as the last number other than 1
    for i in range(1, length):
        one = dp[i-1][1] #diff nodes produces this
        diffOne = dp[i-1][0]*(nodes-1)#generated by one nodes
        diffTwo = dp[i-1][1]*(nodes-2) #generated by diff nodes, excluding the one node prod.
        diff = diffOne + diffTwo
        dp[i] = [one, diff]
    if(last==1):
        return dp[length-1][0]
    return int(dp[length-1][1]/(nodes-1))

if __name__ == "__main__":
    #lis = [length, nodes, lastNodeValue]
    lis = [10, 8, 2]
    lis = [8, 5, 2]
    print(findSolution(lis[0], lis[1], lis[2]))
    #print(countarray(lis[0], lis[1], lis[2])) The GFG Algo, for checking my solution
