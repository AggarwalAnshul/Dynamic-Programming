"""
#M.25

Dynamic Programming | High-effort vs. Low-effort Tasks Problem
You are given n days and for each day (di) you could either perform
a high effort tasks (hi) or a low effort tasks (li) or no task with the
constraint that you can choose a high-effort tasks only if you chose no task
on the previous day. Write a program to find the maximum amount of tasks you can
perform within these n days.

Examples:

No. of days (n) = 5
Day      L.E.   H.E
1        1       3
2        5       6
3        4       8
4        5       7
5        3       6
Maximum amount of tasks 
        = 3 + 5 + 4 + 5 + 3 
        = 20
[+]Temporal marker            : 10:03                   Hours, | Tuesday Sept10, 19
[+]Temporal marker untethered : 10:45(*) | 11:52(DP*)   Hours  | Tuesday Sept10, 19
[+]Comments                   : Had a vague sense of the approach
                                wasted time in implementation w/o coldPressing
                                DP Soution took about 30mins to implemented
[+]Tread speed                : Relaxed
[+]Level                      : Easy
[+]LINK                       : https://www.geeksforg eeks.org/dynamic-programming-high-effort-vs-low-effort-tasks-problem/
"""

#S-Complexity: O(N) | T-Complexity: O(N)
def findSolutionDP(low, high):
    length = len(high)
    dp = [[0]*3 for x in range(length)]
    dp[0][0] = low[0]
    dp[0][1] = high[0]
    for i in range(1, length):
        print("i: "+str(i))
        dp[i][0] = max(dp[i-1])+low[i]
        dp[i][1] = dp[i-1][2] + high[i]
        dp[i][2] = max(dp[i-1])
    import PrintMatrix as pm
    pm.printss(dp)
    return max(dp[length-1])

#S-Complexity: Recursive polynomial | T-Complexity: Polynomial Recursive
def findSolution(low, high, day, work):
    if(day >= len(low)):
       return work
    if(day==0):
       return max(findSolution(low, high, day+1, work+low[day]),
                  findSolution(low, high, day+1, work+high[day]),
                  findSolution(low, high, day+2, work))
    branchOne = findSolution(low, high, day+1, work+low[day])
    branchTwo = 0
    if(day+2<len(low)):
       branchTwo = findSolution(low,high, day+2, work+high[day+1])
    return max(branchOne, branchTwo)

if __name__ == "__main__":
    tasks = [[1, 596, 4, 5, 3], [396, 6, 80, 700, 6]]
    tasks = [[1,5,4,5,3], [3,6,8,7,6]]
    tasks = [[1,5,4,5,3], [3,6,80,7,6]]
   
    print(findSolutionDP(tasks[0], tasks[1]))
    print(findSolution(tasks[0], tasks[1], 0, 0))
    #import test
    #print(test.maxTasks(tasks[1], tasks[0], len(tasks[0]))); 
