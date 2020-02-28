"""
Find the minimum cost to cross the River
Given an integer N which is the number of villagers who need to cross a river but there is only
 one boat on which a maximum of 2 person can travel. Each person i has to pay some specific price
  Pi to travel alone in the boat. If two person i, j travel in the boat then they have to pay max(Pi, Pj).
  The task is to find the minimum amount all the villagers have to pay to cross the river.

Examples:

Input: Price[] = {30, 40, 60, 70}
Output: 220
P1 and P2 go together (which costs 40)
and P1 comes back (total cost 70 now).
Now P3 and P4 go (total cost 140) and
P2 comes back (total cost 180) and
finally P1 and P2 go together (total cost 220).


Input: Price[] = {892, 124}
Output: 892
"""


def experimental(lis):
    lis.sort()
    length = len(lis)
    if length == 1:
        return lis[0]
    cost = 0
    for index in range(length - 1, 1, -2):
        if index == 2:
            cost += lis[0] + lis[index]
        else:
            way_one = lis[0] + 2 * lis[1] + lis[index]
            way_two = lis[index] + lis[index - 1] + 2 * lis[0]
            cost += min(way_two, way_one)
    cost += lis[1]
    return cost


if __name__ == '__main__':

    data = [[300, 400, 600, 700],
            [600, 800, 150, 700],
            [500, 123, 873],
            [1321, 2450],
            [100]]

    for testCase in data:
        print("input: " + str(testCase) + " >> " + str((experimental(testCase))))
