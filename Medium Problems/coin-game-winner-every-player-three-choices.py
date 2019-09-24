#M.66

"""
A and B are playing a game. At the beginning there are n coins. Given two more numbers x and y.
In each move a player can pick x or y or l coins. A always starts the game. The player who picks
the last coin wins the game. For a given value of n, find whether A will win the game or not if
both are playing optimally.

Examples:

Input :  n = 5, x = 3, y = 4
Output : A
There are 5 coins, every player can pick 1 or
3 or 4 coins on his/her turn.
A can win by picking 3 coins in first chance.
Now 2 coins will be left so B will pick one
coin and now A can win by picking the last coin.

Input : 2 3 4
Output : B

[+]Temporal marker            :  Tue, 9:15                  | Sep 24, 19
[+]Temporal marker untethered :  Tue, 9:24(R*) 10:30(DP*)  | Sep 24, 19
[+]Comments                   : * Recursive solution in acceptable time frame
                                * DP Solution took about an hour in inception
                                * max 10 mins in implementation
                                *Delayed due to Address verification
                                *GFG has much more optimized, simpler and elegant solution
[+]Level                      : Medium
[+]Tread speed                : Relaxed
[+]LINK                       : https://www.geeksforgeeks.org/coin-game-winner-every-player-three-choices
"""
#S-Complexity: O(N) | T-Complexity: O(N)
def findSolution(coins, choices):
    dp = [0]*(coins+1)
    dp[1] = 1

    for i in range(2, coins+1):
        for choice in choices:
            if(i-choice>=0 and dp[i-choice]==1):
                dp[i] = 1
    if(dp[coins]==1):
        return "A"
    return "B"

#S-Complexity: O(Coins*choices) | T-Complexity: O(coins*choices)
def findSolutionObsolete(coins, choices):
    number_of_choices = len(choices)

    dp = [[-1]*(number_of_choices+1) for x in range(coins+1)]
    dp[0] = [0]*(number_of_choices+1)

    for i in range(1, coins+1):
        for j in range(1, number_of_choices+1):
            last = dp[i][j-1]
            dp[i][j] = last
            if(i>=choices[j-1] and dp[i-choices[j-1]][number_of_choices-1]>-1):
                previous_computed_value = dp[i-choices[j-1]][number_of_choices]
                if(previous_computed_value%2==0 and last%2==0):
                    dp[i][j] = min(previous_computed_value, last)+1
                elif(previous_computed_value%2==0):
                    dp[i][j] = previous_computed_value+1
                else:
                    dp[i][j] = previous_computed_value+1
    for x in range(1, number_of_choices+1):
        if(dp[coins][x]%2!=0):
            return "A"
    return "B"


#turn --> who picked the last coin
def findSolutionRecursive(coins, x, y, turn):
    if(coins<0):
        return 0
    if(coins==0):
        if(turn==1): #Last coin picked by A
            return 1
        return 0
    return max(findSolutionRecursive(coins-x, x, y, turn*-1),
               findSolutionRecursive(coins-y, x, y, turn*-1),
               findSolutionRecursive(coins-1, x, y, turn*-1)
               )

if __name__ == "__main__":
    lis = [2, [1, 3, 4]]
    lis = [5, [1, 3, 4]]

    print(findSolutionObsolete(lis[0], lis[1]))
    """
    if( findSolutionRecursive(lis[0], lis[1], lis[2], -1)==1):
        print("A")
    else:
        print("B")
    """