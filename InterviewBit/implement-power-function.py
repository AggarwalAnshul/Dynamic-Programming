"""

[+]Temporal marker           : Thu, 22:15 | Feb 06, 20
[+]Temporal marker untethered: Thu, 22:15 | Feb 06, 20
[+]Comments                  :
[+]Level                     :
[+]Tread Speed               :
[+]LINK                      : https://www.interviewbit.com/problems/implement-power-function

"""


#
#
# def powerOne(x, y):
#     if x == 1 or x == 0:
#         return x
#     if y == 1:
#         return x
#     if y == 0:
#         return 1
#     exp = y
#     ans = 1
#     while exp > 0:
#         if exp % 2 == 1:
#             ans *= x
#             exp -= 1
#         else:
#             ans = ans * ans
#             exp = exp // 2
#     return ans


def power(x, y):  # return x**y
    print('calculating for power...'+str(y))
    if x == 1 or x == 0:
        return x
    if y == 0:
        return 1
    if y == 1:
        return x
    if y%2==1:  # if y is odd
        print('this is odd...')
        return power(x, y - 1) * x
    else:
        print('this is even...')
        return power(x * x, y // 2)


data = [38008787, 36381741, 11333711]
print('calculating for an answer...')
print(power(data[0], data[1]) % data[2])
