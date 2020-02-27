"""

[+]Temporal marker           : Wed, 19:49 | Feb 26, 20
[+]Temporal marker untethered: Wed, 10:28 | Feb 27, 20
[+]Comments                  :
[+]Space Complexity          : O(1)
[+]Time Complexity           : O(N)
[+]Level                     : MEDIUM
[+]Tread Speed               : Relaxed
[+]LINK                      : https://www.interviewbit.com/problems/array-3-pointers
[+] Supplement Sources       : N/A
"""


# def binary(lis, left, right, one, two):
#     leftTemp = left
#     rightTemp = right
#     ans = -1
#     while leftTemp <= rightTemp:
#         mid = (leftTemp + rightTemp)//2
#         if lis[mid] == one:
#             ans = mid
#             break
#         elif lis[mid] > one:
#             rightTemp = mid - 1
#         else:
#             leftTemp = mid + 1
#     if ans == -1:
#         return ans
#     leftTemp = left
#     rightTemp = right
#     while leftTemp <= rightTemp:
#         mid = (leftTemp + rightTemp)//2
#         if lis[mid] == two:
#             ans = mid
#             break
#         elif lis[mid] > two:
#             rightTemp = mid -1
#         else:
#             leftTemp = mid + 1
#     if ans == -1:
#         return ans
#     minimum = min(one, two)
#     for x in range(right+1):
#         if lis[x] < one:
#             return x
#     return -1
#
#
# # def experimental(lis):
# #     pointer = [len(lis[0]) - 1, len(lis[1]) - 1, len(lis[2]) - 1]
# #     import sys
# #     ans = sys.maxsize
# #     flag = 0
# #     while flag == 0:
# #         for index in range(3):
# #             secondIndex = (index + 1) % 3
# #             thirdIndex = (index + 2) % 3
# #             pointer[index] = binary(lis[index], 0, pointer[index],
# #                                     lis[secondIndex][pointer[secondIndex]],
# #                                     lis[thirdIndex][pointer[thirdIndex]])
# #             if pointer[index] == -1:
# #                 flag = 1
# #             ans = min(ans, max(abs(lis[0][pointer[0]] - lis[1][pointer[1]]),
# #                                abs(lis[1][pointer[1]] - lis[2][pointer[2]]),
# #                                abs(lis[0][pointer[0]] - lis[2][pointer[2]])
# #                                ))
# #     ans = min(ans, max(abs(lis[0][pointer[0]] - lis[1][pointer[1]]),
# #                        abs(lis[1][pointer[1]] - lis[2][pointer[2]]),
# #                        abs(lis[0][pointer[0]] - lis[2][pointer[2]])
# #                        ))
# #     return ans
# def experimental(lis):
#     pointer = [0, 0, 0]
#     import sys
#     ans = sys.maxsize
#     flag = 0
#     while flag == 0:
#         minimum = min(lis[0][pointer[0]], lis[1][pointer[1]], lis[2][pointer[2]])
#         for index in range(3):
#             if lis[index][pointer[index]] == minimum:
#                 if pointer[index] < len(lis[index])-1:
#                     pointer[index] += 1
#                 else:
#                     flag = 1
#                     ans = min(ans, max(abs(lis[0][pointer[0]] - lis[1][pointer[1]]),
#                                        abs(lis[1][pointer[1]] - lis[2][pointer[2]]),
#                                        abs(lis[0][pointer[0]] - lis[2][pointer[2]])
#                                        ))
#                     return ans
#                     break
#             ans = min(ans, max(abs(lis[0][pointer[0]] - lis[1][pointer[1]]),
#                                abs(lis[1][pointer[1]] - lis[2][pointer[2]]),
#                                abs(lis[0][pointer[0]] - lis[2][pointer[2]])
#                                ))
#     ans = min(ans, max(abs(lis[0][pointer[0]] - lis[1][pointer[1]]),
#                        abs(lis[1][pointer[1]] - lis[2][pointer[2]]),
#                        abs(lis[0][pointer[0]] - lis[2][pointer[2]])
#                        ))
#     return ans
#
# def findSolution(lis):
#     pointer = [len(lis[0])-1, len(lis[1])-1, len(lis[2])-1]
#     import sys
#     ans = sys.maxsize
#     flag = 0
#     while flag == 0:
#         for index in range(3):
#             next_index = (index + 1) % 3
#             if lis[index][pointer[index]] > lis[next_index][pointer[next_index]]:
#                 if pointer[index] > 0:
#                     pointer[index] -= 1
#                 else:
#                     flag = 1
#             else:
#                 if pointer[next_index] > 0:
#                     pointer[next_index] -= 1
#                 else:
#                     flag = 1
#             ans = min(ans, max(abs(lis[0][pointer[0]] - lis[1][pointer[1]]),
#                                abs(lis[1][pointer[1]] - lis[2][pointer[2]]),
#                                abs(lis[0][pointer[0]] - lis[2][pointer[2]])
#                                ))
#     ans = min(ans, max(abs(lis[0][pointer[0]] - lis[1][pointer[1]]),
#                        abs(lis[1][pointer[1]] - lis[2][pointer[2]]),
#                        abs(lis[0][pointer[0]] - lis[2][pointer[2]])
#                        ))
#     return ans

# EDITORIAL IS SIMILAR TO THIS
def findSolution(lis):
    def returnAnswer(pointer, lis):
        maximum = 0
        minimum = 0
        for index in range(len(pointer)):
            if lis[index][pointer[index]] > lis[maximum][pointer[maximum]]:
                maximum = index
            if lis[index][pointer[index]] < lis[minimum][pointer[minimum]]:
                minimum = index
        return lis[maximum][pointer[maximum]] - lis[minimum][pointer[minimum]]

    pointer = [0, 0, 0]
    ans = lis[0][-1]
    while True:
        minimum = 0
        for index in range(3):
            if lis[index][pointer[index]] < lis[minimum][pointer[minimum]]:
                minimum = index
        if pointer[minimum] < len(lis[minimum]) - 1:
            pointer[minimum] += 1
        else:
            return min(ans, returnAnswer(pointer, lis))
        ans = min(ans, returnAnswer(pointer, lis))
    return ans


if __name__ == "__main__":
    data = [
        [[1, 4, 10], [2, 15, 20], [10, 12]]
    ]
    for x in data:
        print("input: " + str(x) + " >> " + str(findSolution(x)))
