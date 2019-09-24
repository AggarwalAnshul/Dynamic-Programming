#M.

"""
Count number of ways to jump to reach end
Given an array of numbers where each element represents the max number of jumps that can be made forward from that element. For each array element, count number of ways jumps can be made from that element to reach the end of the array. If an element is 0, then move cannot be made through that element. The element that cannot reach to the end should have a count “-1”.

Examples:

Input : {3, 2, 0, 1}
Output : 2 1 -1 0
For 3 number of steps or jumps that
can be taken are 1, 2 or 3. The different ways are:
3 -> 2 -> 1
3 -> 1

For 2 number of steps or jumps that
can be taken are 1, or 2. The different ways are:
2 -> 1

For 0 number of steps or jumps that
can be taken are 0.
One cannot move forward from this point.

For 1 number of steps or jumps that
can be taken are 1. But the element is at
the end so no jump is required.

Input : {1, 3, 5, 8, 9, 1, 0, 7, 6, 8, 9}
Output : 52 52 28 16 8 -1 -1 4 2 1 0

[+]Temporal marker            :  Tue, 20:42 | Sep 24, 19
[+]Temporal marker untethered :  Tue, 20:55 | Sep 24, 19
[+]Comments                   : * Concepted the apporach as soon as i read the problem
                                * Implementation took 8 mins
                                * rest of the time in debuggin
                                * Problem is closed now
[+]Level                      : Easy
[+]Tread speed                : paced
[+]LINK                       : https://www.geeksforgeeks.org/count-number-ways-jump-reach-end
"""
def findSolution(lis):
    length_of_lis = len(lis)

    #THE DP TABLE | AUX SPACE
    dp = [-1]*length_of_lis
    dp[length_of_lis-1] = 0

    #THE MEAT
    for x in range(length_of_lis-2, -1, -1):
        number_of_steps = lis[x]
        number_of_ways_to_reach_end = 0

        for y in range(x+1, x+number_of_steps+1): #Checking if there's a path through each forward mem permitted
            if(y < length_of_lis):
                if(y==length_of_lis-1): #Reached end, add 1 way (Since the dp of this index has to remain 0)
                    number_of_ways_to_reach_end += 1
                elif(dp[y] != -1):  #this is not an obstacle, add it's possible ways to count
                    number_of_ways_to_reach_end += dp[y]

        if(number_of_ways_to_reach_end>0): #There is an existent path to reach the end
            dp[x] = number_of_ways_to_reach_end

    return dp

if __name__ == "__main__":
    lis = [1, 3, 5, 8, 9, 1, 0, 7, 6, 8, 9]
    lis = [3, 2, 0, 1]
    print(findSolution(lis))