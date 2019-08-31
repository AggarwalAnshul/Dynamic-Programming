"""
Count number of ways to fill a “n x 4” grid using “1 x 4” tiles
Given a number n, count number of ways to fill a n x 4 grid using 1 x 4 tiles.
Examples:

Input : n = 1
Output : 1

Input : n = 2
Output : 1
We can only place both tiles horizontally

Input : n = 3
Output : 1
We can only place all tiles horizontally.

Input : n = 4
Output : 2
The two ways are : 
  1) Place all tiles horizontally 
  2) Place all tiles vertically.

Input : n = 5
Output : 3
We can fill a 5 x 4 grid in following ways : 
  1) Place all 5 tiles horizontally
  2) Place first 4 vertically and 1 horizontally.
  3) Place first 1 horizontally and 4 horizontally.

LINK: https://www.geeksforgeeks.org/count-number-of-ways-to-fill-a-n-x-4-grid-using-1-x-4-tiles/
"""

def CountNumberOfWaysToFillANX4GridUsing1X4Tiles(n):
    if(n<0):
        return 0
    if(n>=0 and n<4):
        return 1
    if(n==4):
        return 2
    return ( CountNumberOfWaysToFillANX4GridUsing1X4Tiles(n-1) +
             CountNumberOfWaysToFillANX4GridUsing1X4Tiles(n-4) )

if __name__ == "__main__":
    print(CountNumberOfWaysToFillANX4GridUsing1X4Tiles(8))
