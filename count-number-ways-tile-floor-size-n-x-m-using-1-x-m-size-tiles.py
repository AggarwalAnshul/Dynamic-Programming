"""
#90
We are back in business Baby!
Count the number of ways to tile the floor of size n x m using 1 x m size tiles
Given a floor of size n x m and tiles of size 1 x m. The problem is to count the number of ways to tile the given floor using 1 x m tiles. A tile can either be placed horizontally or vertically.
Both n and m are positive integers and 2 < = m.

Examples:

Input : n = 2, m = 3
Output : 1
Only one combination to place 
two tiles of size 1 x 3 horizontally
on the floor of size 2 x 3. 

Input :  n = 4, m = 4
Output : 2
1st combination:
All tiles are placed horizontally
2nd combination:
All tiles are placed vertically.

[+]Temporal marker            : 10:05 Hours | Sept02, 2019
[+]Temporal marker untethered : 10:07 Hours | Sept02, 2019
[+]Comments                   : Already knew the apporch, just implemented, I can
                                Use tabulization but the truth is i'm too lazy to
                                use it, However it's a piece of case
[+]LINK                       : https://www.geeksforgeeks.org/count-number-ways-tile-floor-size-n-x-m-using-1-x-m-size-tiles/    
"""

def tileTheFloor(n, m):
    if(n<0):
        return 0
    if(n==0):
        return 1
    return tileTheFloor(n-1, m)+tileTheFloor(n-m, m)

if __name__ == "__main__":
    lis = [4, 4]
    lis = [2, 3]
    lis = [5, 5]
    lis = [7, 4]
    print(tileTheFloor(lis[0], lis[1]))
