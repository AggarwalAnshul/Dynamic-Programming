"""

Asked in:
VMWare
Amazon
You are given with an array of 1s and 0s. And you are given with an integer M, which signifies number of flips allowed.
Find the position of zeros which when flipped will produce maximum continuous series of 1s.

For this problem, return the indices of maximum continuous series of 1s in order.

Example:

Input :
Array = {1 1 0 1 1 0 0 1 1 1 }
M = 1

Output :
[0, 1, 2, 3, 4]


[+]Temporal marker           : Mon, 21:4 | Feb 24, 20
[+]Temporal marker untethered: Tue, 14:18 | Feb 25, 20
[+]Comments                  : Finally solved on my own
                                Matter is closed now
[+]Space Complexity          : O(N)
[+]Time Complexity           : O(N)
[+]Level                     : MEDIUM
[+]Tread Speed               : Intermittent
[+]LINK                      : https://www.interviewbit.com/problems/max-continuous-series-of-1s
[+] Supplement Sources       : N/A
"""


# Accepted
def experimental(lis, flips):
    length = len(lis)
    aux = [0 for x in range(length)]
    answer, start, end = 0, 0, 0
    j = 0
    for index in range(length):
        if index > 0:
            flips += aux[index - 1]
        j = index if j < index else j
        while j < length:
            if lis[j] == 0:
                if flips == 0:
                    break
                else:
                    aux[j] = 1
                    flips -= 1
            j += 1
        if answer < j - index:
            start, end = index, j
            answer = j - index
    return list(range(start, end))
    #
    # for index in range(length):
    #     flag = 0
    #     if j > 0:
    #         flips_left += aux[index - 1]
    #     if j < index:
    #         j = index
    #     while flag != 1 and j < length:
    #         if lis[j] == 1:
    #             streak += 1
    #             j += 1
    #         else:
    #             if flips_left == 0:
    #                 flag = 1
    #             else:
    #                 aux[j] = 1
    #                 auxValue += 1
    #                 streak += 1
    #                 flips_left -= 1
    #                 j += 1
    #     if ans < j - index:
    #         start = index
    #         end = j
    #         ans = j - index
    # return [x for x in range(start, end)]

# OBSOLETE
def findSolution(lis, flips):
    ans = 0
    length = len(lis)
    streak = 0
    flops = flips
    breakpoint = 0
    for index in range(length):
        if lis[index] == 1:
            streak += 1
        else:
            if flops == flips and flips > 0:
                breakpoint = index
                streak += 1
                flops -= 1
            elif flops > 0:
                streak += 1
                flops -= 1
            elif flops == 0:
                ans = max(ans, streak)
                streak = index - breakpoint
                flops = flips
                flops -= 1
                breakpoint = index

    return max(ans, streak)


if __name__ == "__main__":
    data = [[[1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0], 4],
            [[0, 1, 1, 1], 0],

            [[1, 1, 0, 1, 1, 0, 0, 1, 1, 1], 1],
            [[1, 1, 0], 2], ]
    for x in data:
        print("input: " + str(x) + " >> " + str(experimental(x[0], x[1])))
