#M.68

"""
 Count all increasing subsequences
We are given an array of digits (values lie in range from 0 to 9). The task is to count all the sub sequences possible in array such that in each subsequence every digit is greater than its previous digits in the subsequence.

Examples:

Input : arr[] = {1, 2, 3, 4}
Output: 15
There are total increasing subsequences
{1}, {2}, {3}, {4}, {1,2}, {1,3}, {1,4},
{2,3}, {2,4}, {3,4}, {1,2,3}, {1,2,4},
{1,3,4}, {2,3,4}, {1,2,3,4}

Input : arr[] = {4, 3, 6, 5}
Output: 8
Sub-sequences are {4}, {3}, {6}, {5},
{4,6}, {4,5}, {3,6}, {3,5}

Input : arr[] = {3, 2, 4, 5, 4}
Output : 14
Sub-sequences are {3}, {2}, {4}, {3,4},
{2,4}, {5}, {3,5}, {2,5}, {4,5}, {3,2,5}
{3,4,5}, {4}, {3,4}, {2,4}

[+]Temporal marker            :  Tue, 16:29 | Sep 24, 19
[+]Temporal marker untethered :  Tue, 16:50(Obsolete) 16:58(Efficient) | Sep 24, 19
[+]Comments                   : *
                                *
                                *
[+]Level                      :
[+]Tread speed                :
[+]LINK                       : https://www.geeksforgeeks.org/count-all-increasing-subsequences
"""

#S-Complexity: O(N) | T-Complexity: O(N*N)
def findSolution(lis):
    length =len(lis)
    dp = [1]*length
    answer = 0
    for i in range(1, length):
        for j in range(i):
            if(lis[i]>lis[j]):
                dp[i]+=dp[j]
        answer += dp[i]
    print(dp)
    return answer+1

#S-Complexity: O(N) | T-Complexity: O(N*N*N)
def findSolutionObsolete(lis):
    length = len(lis)
    dp = [0]*length
    count_until_now = 0
    count_for_this_row = 0
    count_for_this_element = 0


    for i in range(length):
        dp[i] = 1
        count_for_this_row = 1
        for j in range(i+1, length):
            count_for_this_element = 0
            for k in range(i, j):
                if(lis[k] < lis[j]):
                    count_for_this_element += dp[k]
            dp[j] = count_for_this_element
            count_for_this_row += count_for_this_element
        #print(dp)
        dp = [0]*length
        count_until_now += count_for_this_row

    return count_until_now

if __name__ == "__main__":

    lis = [1, 2, 3, 4]
    lis = [4, 3, 6, 5]
    lis = [3, 2 ,4, 5, 4]

    print(findSolution(lis))
    print("computing using obsolete technique...")
    print(findSolutionObsolete(lis))
