"""
#102
Count Balanced Binary Trees of Height h
Given a height h, count and return the maximum number of balanced binary trees possible with height h. A balanced binary tree is one in which for every node, the difference between heights of left and right subtree is not more than 1.

Examples :

Input : h = 3
Output : 15

Input : h = 4
Output : 315

[+]Temporal marker            : Didn't Tether | Thursday, Sept05, 19
[+]Temporal marker untethered : N/A Took Didn't Tether | Sept05, 2019, Tuesday
[+]Comments                   : Couldn't solve, took help from GFG, too lazy to implement a
                                DP Solution
[+]Tread speed                : Relaxed 
[+]Level                      : Hard
[+]LINK                       : https://www.geeksforgeeks.org/count-balanced-binary-trees-height-h/
"""
def findSolution(h):
    if(h==0 or h==1):
        return 1
    return (findSolution(h-1)*findSolution(h-2) +
            (findSolution(h-2)*findSolution(h-1))+
            (findSolution(h-1)*findSolution(h-1)))

if __name__ == "__main__":
    height = 3
    print(findSolution(height))
