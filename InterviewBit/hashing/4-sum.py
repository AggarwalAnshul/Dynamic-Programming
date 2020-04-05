"""
ON THE NEW VS-CODE EDITOR! BOY THIS LOOKS SO COOL!

[+]Temporal marker            :1309 Hours | Sunday 05, 2020
[+]Temporal marker Untethered :1831 Hours | Sunday 05, 2020
[+]Comments                   : Did some showstopper fix for office 1440 - 1810 Hours
                                I has a vague sense of idea to solve this question
                                Used the 2 solution approach to bring the complexity from (N^4) --> O(N^2)
                                I'm still using the sorting inside the second for loop, which i think can be further optimizied
                                Matter is still open
                                ALSO I FLASHED THIS PROBLEM USING BACKTRACKING IN ONE-PASS! KUDOS TO AN ITERATIVE-BACKTRACKING SOLUTION
                                Solution at par with the editorial solution
                                It can be much more optimized using a 2 pointer approach
                                However I didn't dwell there since, i wanted to come up with a Hashing only solution
                                I actually did thought of a 2-pointer approach
                                Could have solved it a lot earlier, if only i had compared the index of existing quadruple candidate
                                Anyways, matter is officially closed now
[+]Space Complexity           : O(N*N)
[+]Time Complexity            : O(N*N)
[+]Level                      :  MEDIUM
[+]Tread Speed                : RELAXED
[+]LINK                      : https://www.interviewbit.com/problems/4-sum.py
[+] Supplement Sources       : N/A

"""


# ACCEPTED SOLUTION!
# CAN BE MUCH OPTIMIZED
# Solution at par with the editorial solution
# however 2 pointer approach can be used to remove the obvious fits
# I didn't dwell there, since I wanted to come up with a hasing only solution
def fourSum(lis, target):
    lis.sort()
    hashmap = {}
    length = len(lis)
    ans = set()

    for i_index in range(length):
        for j_index in range(0, i_index):
            sum = lis[i_index] + lis[j_index]
            if target - sum in hashmap:
                for subset in hashmap[target - sum]:
                    if not (subset[0] == i_index
                            or subset[1] == j_index) and not (
                                subset[0] == j_index or subset[1] == i_index):
                        ans.add(
                            tuple(
                                sorted([
                                    lis[subset[0]],
                                    lis[subset[1]],
                                    lis[i_index],
                                    lis[j_index],
                                ])))
            if sum in hashmap:
                hashmap[sum] = hashmap[sum] + [[i_index, j_index]]
            elif sum not in hashmap:
                hashmap[sum] = [[i_index, j_index]]
    return sorted(ans)


# Backtracking - solution
# Fullty Accepted Solution
# FLASHED IT!
# Devised < 10 Mins
def fourSumBacktracking(lis, target):
    lis.sort()
    ans = set()
    frontier = [(0, [])]  # index, quadruple
    while frontier:
        index, quadruple = frontier.pop()
        if len(quadruple) == 4:
            if sum(quadruple) == target:
                ans.add(tuple(quadruple))
            continue
        if index < len(lis):
            frontier.append((index + 1, quadruple + [lis[index]]))
            frontier.append((index + 1, quadruple))
    return sorted(ans)


if __name__ == "__main__":
    test_cases = [

        [[1, -1, -1, 0, 3, 1], 3],
        [[1, 0, -1, 0, -2, 2], 0],
        [[9, -8, -10, -7, 7, -8, 2, -7, 4, 7, 0, -3, -4, -5, -1, -4, 5, 8, 1, 9, -2, 5, 10, -5, -7, -1, -6, 4, 1, -
            5, 3, 8, -4, -10, -9, -3, 10, 0, 7, 9, -8, 10, -9, 7, 8, 0, 6, -6, -7, 6, -4, 2, 0, 10, 1, -2, 5, -2], 0]
    ]
    for index in range(len(test_cases)):
        test_case = test_cases[index]
        print("input: " + str(input) + "\n\tOUTPUT: :" +
              str(fourSum(test_case[0], test_case[1])))
