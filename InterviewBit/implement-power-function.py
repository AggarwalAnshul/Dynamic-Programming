"""

[+]Temporal marker           : Thu, 22:15 | Feb 06, 20
[+]Temporal marker untethered: Mon, 12:45 | Feb 10, 20
[+]Comments                  :Switched focus to another problem which would explain temporal marker
                                *Couldn't have found the log(n) technique to exponentiate w/o GFG
                                *Devised the solution on my own after understanding the logic
                                *The solution was still not being accepted
                                *The catch was to take % of individual results, which would keep down the overall
                                result significantly low and hence large number multiplication overhead won't be an issue
                                for us.This also doesn't impacts the result's accuracy
                                *Also learnt about the mod of negative numbers from this problem
                                *Great problem.
                                *MATTER IS CLOSED NOW.
[+]Level                     :MEDIUM
[+]Tread Speed               :RELAXED
[+]LINK                      : https://www.interviewbit.com/problems/implement-power-function

"""


def power(x, y, m):  # return x**y
    if x == 0:
        return x
    if y == 0:
        return 1
    if y & 1:
        return (power(x, y - 1, m) * x) % m
    else:
        y = power(x, y // 2, m)
        return (y * y) % m


data = [38008787, 36381741, 11333711]
data = [-1, 1, 20]
print(power(data[0], data[1], data[2]))
