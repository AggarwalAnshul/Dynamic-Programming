#M.

"""
Maximum profit from sale of wines
Given n wines in a row, with integers denoting the cost of each wine respectively.
Each year you can sale the first or the last wine in the row. However, the price of wines increases
over time. Let the initial profits from the wines be P1, P2, P3…Pn. On the Yth year,
 the profit from the ith wine will be Y*Pi. For each year, your task is to print “beg” or “end”
 denoting whether first or last wine should be sold. Also, calculate the maximum profit from all
 the wines.

Examples :

Input: Price of wines: 2 4 6 2 5
Output: beg end end beg beg
         64
Explanation :

[+]Temporal marker            :  Sat, 10:25 | Jan 11, 20
[+]Temporal marker untethered :  Sat, 10:30(R*) 11:36(DP*)  | Jan 11, 20
[+]Comments                   : *DP(ying) of this solution was easy
                                *i was incorrectly passing the money variable in the recursion
                                *instead of putting the money calculated by this current state
                                *i was putting the all_the_money_yet in the recursion which
                                *actually nullified the benefit of pre-computed results since choosing
                                *this
                                    *would give the precomputed result for this state
                                    *it would also remove the benefit of choice taken before it to reach
                                    this state
[+]Level                      :
[+]Tread speed                :
[+]LINK                       : https://www.geeksforgeeks.org/maximum-profit-sale-wines
"""

""" THE WRONG DP VERSION THAT I WAS DOING FOR OVER AN HOUR  
def findSolution(wine, start, end, year, money, dp):
    if(end < start):
        return money
    if(dp[start][end][year] == -1):
        dp[start][end][year] = max(
        findSolution(wine, start+1, end, year+1, money + (year * wine[start]), dp),
        findSolution(wine, start, end-1, year+1, money + (year * wine[end]), dp,)
                                   )
    return dp[start][end][year]
#KEYLEARNING: DO NOT PASS THE ANSWER AS A WHOLE INTO THE RECURSION, YOU HAVE TO RETURN IT NO DOUBT,
              BUT PASS ONLY THE ANSWER COMPUTED FOR THIS STATE, SO THAT IT CAN BE STORED
              THE WHOLE ANSWER CAN BE RETURNED BY, ADDING (1. + 2.) 
                1. ANSWER TILL THIS STATE
                2. ANSWER AFTER THIS STATE
"""
def findSolution(wine, start, end, year, money, dp):
    if(end < start):
        return money
    if(dp[start][end][year] == -1):
        dp[start][end][year] = max(findSolution(wine, start+1, end, year+1, year*wine[start], dp),
                                   findSolution(wine, start, end - 1, year + 1, year * wine[end], dp,)
                                   )
    return dp[start][end][year] + money

def findSolutionRecursive(wine, year, money):
    if(len(wine)==0):
        return money
    return max(findSolutionRecursive(wine[1:], year + 1, money + (year * wine[0])),
               findSolutionRecursive(wine[:-1], year + 1, money + (year * wine[-1]))
               )



if __name__ == "__main__":
    wine = [2, 4, 6,2]
    length = len(wine)
    #dp[i][j][year]
    dp = [[[-1 for x in range(length+1)] for y in range(length+1)] for k in range(length)]
    print(findSolution(wine, 0, length-1, 1, 0, dp))
    print(findSolutionRecursive(wine, 1, 0))