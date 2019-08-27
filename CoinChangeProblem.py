"""
COIN CHANGE PROBLEM
"""

""">>>>> CORRECTED VERSION <<<<<<<<< """
def findCoinChange(coins, money):
    length = len(coins)
    dp =[0]*(money+1)
    dp[0] = 1

    for i in range(0, len(coins)):
        for j in range(coins[i], money+1):
            dp[j] += dp[j-coins[i]]
    return dp[length]
"""
def findCoinChange(coins, money):
    length = len(coins)
    coins.sort()
    maxValue = 0
    
    #matrix creation and initialization
    dp = [0]*(length+1)
    dp = [[0]*(length+1) for x in range(money+1)]
    for x in range(0, length+1):
        dp[0][x] = 1

    #populating the matrix
    for i in range(1, money+1):
        for j in range(1, length+1):
            if(i<coins[j-1]):
                dp[i][j] = 0
            else:
                dp[i][j] += dp[i-coins[j-1]][j] + dp[i][j-1]
            maxValue = max(maxValue, dp[i][j])
   #print(dp)
    print(maxValue)
    #print(dp[money][length])
"""        
coins = [1,2,3]
print(findCoinChange(coins, 3))
