"""
Programming Hashing Points On The Straight Line
Points on the Straight Line
Asked in:  
Google
Amazon
InMobi
Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

Sample Input :

(1, 1)
(2, 2)
Sample Output :

2
You will be given 2 arrays X and Y. Each point is represented by (X[i], Y[i])

Seen this question in a real interview beforeYesNo
"""

"""
[+]Temporal marker            :1509 Hours 0938 Hours| Wednesday 08, 2020
[+]Temporal marker Untethered :1509 Hours | Wednesday 08, 2020
[+]Comments                   :
[+]Space Complexity           : O()
[+]Time Complexity            : O()
[+]Level                      : 
[+]Tread Speed                :
[+]LINK                      : https://www.interviewbit.com/problems/points-on-the-straight-line.py
[+] Supplement Sources       : N/A

starting at 0938 Hours 

"""

def tailorInput(string):
    lis = string.split(' ')
    length = int(lis[0])
    numerator = [int(x) for x in lis[1:length + 1]]
    denominator = [int(x) for x in lis[length + 1:]]
    return [numerator, denominator]


# ACCEPTED!
def maxPoints(Xcordinates, Ycordinates):
    def reduce(y, x):
        def hcf(a, b):
            if b == 0:
                return a
            return hcf(b, a%b)
        factor = hcf(y, x)
        y /= factor
        x /= factor
        return (y, x)

    length = len(Xcordinates)
    if length == 1:
        return 1
    ans = 0
    for i_index in range(length):
        x1, y1 = Xcordinates[i_index], Ycordinates[i_index]
        infinity_slope = 0
        max_points_for_this_point = 0
        seen = {}
        for j_index in range(i_index + 1, length):
            x2, y2 = Xcordinates[j_index], Ycordinates[j_index] 
            y, x = y2 - y1, x2 - x1
            if x == 0:
                infinity_slope += 1
                continue
            if x2 < 0 or y2 < 0:
                y2 *= -1
                x2 *= -1
            slope = reduce(y, x) if y != 0 else 0
            if slope in seen:
                seen[slope] += 1
            else:
                seen[slope] = 1
            max_points_for_this_point = max(max_points_for_this_point, seen[slope])
        ans = max(ans, max_points_for_this_point, infinity_slope)
    return ans+1 if ans != 0 else ans


if __name__ == "__main__":
    test_cases = [
        [[1, 1, 1], [0, 4, -1]],
        [[],[]],
        [[1],[1]],
        [[0, 1, -1], [0, 1, -1]],
        [[1, 2, 1, 3, 4, 5, 6], [1, 4, 1, 3, 1, 5, 3]],
        [[1, 2, 3, 4, 5, 6], [1, 4, 3, 1, 5, 3]],
        [[1, 1], [1, 2]],
        [[-6, 5, -18, 2, 5, -2], [-17, -16, -17, -4, -13, 20]],
        [[-6, -17, 5, -16, -18, -17], [2, -4, 5, -13, -2, 20]],
        tailorInput("96 15 12 9 10 -16 3 -15 15 11 -10 -5 20 -3 -15 -11 -8 -8 -3 3 6 15 -14 -16 -18 -6 -8 14 9 -1 -7 -1 -2 3 11 6 20 10 -7 0 14 19 -18 -10 -15 -17 -1 8 7 20 -18 -4 -9 -9 16 10 14 -14 -15 -2 -10 -18 9 7 -5 -12 11 -17 -6 5 -17 -2 -20 15 -2 -5 -16 1 -20 19 -12 -14 -1 18 10 1 -20 -15 19 -18 13 13 -3 -16 -17 1 0 20 -18 7 19 1 -6 -7 -11 7 1 -15 12 -1 7 -3 -13 -11 2 -17 -5 -12 -14 15 -3 15 -11 7 3 19 7 -15 19 10 -14 -14 5 0 -1 -12 -4 4 18 7 -3 -5 -3 1 -11 1 -1 2 16 6 -6 -17 9 14 3 -13 8 -9 14 -5 -1 -18 -17 9 -10 19 19 16 7 3 7 -18 -12 -11 12 -15 20 -3 4 -18 1 13 17 -16 -15 -9 -9 15 8 19 -9 9 -17")
    ]
    for index in range(len(test_cases)):
        test_case = test_cases[index]
        print("input: "+str(test_case)+"\n\tOUTPUT: :" +
              str(maxPoints(test_case[0], test_case[1])))
