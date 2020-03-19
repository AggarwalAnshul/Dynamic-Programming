"""
Largest Rectangle in Histogram
Asked in:
Google
Facebook
Amazon
Given an array of integers A of size N. A represents a histogram i.e A[i] denotes height of
the ith histogram’s bar. Width of each bar is 1.

Largest Rectangle in Histogram: Example 1

Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].

Largest Rectangle in Histogram: Example 2

The largest rectangle is shown in the shaded area, which has area = 10 unit.

Find the area of largest rectangle in the histogram.



Input Format

The only argument given is the integer array A.
Output Format

Return the area of largest rectangle in the histogram.
For Example

Input 1:
    A = [2, 1, 5, 6, 2, 3]
Output 1:
    10
    Explanation 1:
        The largest rectangle is shown in the shaded area, which has area = 10 unit.

[+]Temporal marker           : Wed, 11:41 | Mar 18, 20
[+]Temporal marker untethered: Wed, 21:33 | Mar 18, 20
[+]Comments                  : Suspending at 13:41, I am trying another problem
                                naive solution has been devised
                                couldn't solve optimized on my own
                                breakthrough was Tushar Roy's YT Video
                                Matter is close now
[+]Space Complexity          : O(N)
[+]Time Complexity           : O(N)
[+]Level                     : MEDIUM
[+]Tread Speed               : Relaxed
[+]LINK                      : https://www.interviewbit.com/problems/largest-rectangle-in-histogram
[+] Supplement Sources       : https://www.youtube.com/watch?v=ZmnqCZp9bBs
"""


# TLE, Accepted
def findSolution_naive(input):
    length = len(input)
    ans = 0
    for x in range(length):
        area = 0
        height = input[x]
        for y in range(x, length):
            if input[y] < height:
                height = input[y]
                area = height * (y - x + 1)
                ans = max(ans, area)
            else:
                area += height
                ans = max(ans, area)
            # print(str(input[x]) + " , " + str(input[y]) + " >> " + str(area) + " ans: " + str(ans))
    return ans


def findSolution_obsolete(input):
    length = len(input)
    area, stack = 0, []
    for index in range(length):
        if not stack or input[stack[-1]] <= input[index]:
            stack.append(index)
        else:
            # keep on popping until a smaller histogram than current is found
            while stack and input[stack[-1]] >= input[index]:
                # calculate the area with this histogram
                right = index
                height = input[stack[-1]]
                if len(stack) >= 2:
                    left = stack[-2]
                    temp_area = height * (right - left - 1)
                else:
                    temp_area = height * right
                area = max(area, temp_area)
                stack.pop()
            stack.append(index)
    while stack:
        # calculate the area with this histogram
        # print("\t\t" + str(input[stack[-1]]) + " will be popped")
        height = input[stack[-1]]
        if len(stack) >= 2:
            left = stack[-2]
            temp_area = height * (length - left - 1)
        else:
            temp_area = height * length
        # print("\t\t left: " + str(left) + " right: " + str(right) + " area: " + str(temp_area))
        area = max(area, temp_area)
        stack.pop()
    return area


# MOST EFFICIENT * ACCEPTED
def findSolution(input):
    length, stack, area = len(input), [], 0

    for index in range(length):
        histogram = input[index]
        while stack and input[stack[-1]] > histogram:
            # pop the top histogram and calculate the area formed by it form this until the second top histogram
            height = input[stack[-1]]
            if len(stack) == 1:
                temp_area = height * index
                # This is the minimum histogram until this index, all other would be >= than this.
                # Hence it can form area will all other histograms until this point hence length would be = index
            else:
                # there are other histograms smaller than this available.
                # it can only form area with only those histograms that are >= than this one
                # since the stack[-2] will hold the histogram smaller than this, the length for the area would be
                # left --> index of the second top histogram
                # right --> current index (index of the next histogram, which is smaller than this one)
                # length of area --> left - right - 1
                temp_area = height * (index - stack[-2] - 1)
            area = max(area, temp_area)
            # remove this histogram as we have to accommodate the input[index] histo which is smaller than this
            stack.pop()
        # insert this histogram, as all others in the stack are <= , to this histogram.
        stack.append(index)

    # Empty the stack & calculate the area formed by all histograms present in the stack
    while stack:
        height = input[stack[-1]]
        if len(stack) == 1:
            temp_area = height * length
        else:
            temp_area = height * (length - stack[-2] - 1)
        area = max(temp_area, area)
        stack.pop()
    return area


if __name__ == "__main__":
    test_cases = [
        [2, 1, 5, 6, 2, 3],
        [90, 58, 69, 70, 82, 100, 13, 57, 47, 18],
        [17, 91, 27, 4, 80, 78]
    ]
    for x in range(len(test_cases)):
        test_case = test_cases[x]
        print("input: " + str(test_case)
              + "\n\t\t NAIVE     >> " + str(findSolution_naive(test_case))
              + "\n\t\t optimized >> " + str(findSolution(test_case)))
