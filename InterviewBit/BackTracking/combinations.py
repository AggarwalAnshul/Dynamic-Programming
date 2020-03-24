'''
Combinations
Asked in:
Amazon
Adobe
Given two integers n and k, return all possible combinations of k numbers out of 1 2 3 ... n.

Make sure the combinations are sorted.

To elaborate,

Within every entry, elements should be sorted. [1, 4] is a valid entry while [4, 1] is not.
Entries should be sorted within themselves.
Example :
If n = 4 and k = 2, a solution is:

[
  [1,2],
  [1,3],
  [1,4],
  [2,3],
  [2,4],
  [3,4],
]
 Warning : DO NOT USE LIBRARY FUNCTION FOR GENERATING COMBINATIONS.
Example : itertools.combinations in python.
If you do, we will disqualify your submission retroactively and give you penalty points.


[+]Temporal marker           : 20:34 21 37Hours | Sunday 22, 2020
[+]Temporal marker untethered: 19:54(Elegant & Efficient) | Monday 23, 2020 ||
                                23:50 Hours(Accepted) | Sunday 22, 2020
[+]Comments                  : Took a lot of time then expected to get the first accepted solution
                                >> I've been trying to devise a solution like the editorial one
                                >> though i just saw the LOC and for loops not the specifics
                                >> Finally devised the same solution
                                >> PS: I've been working constantly on office stuff since morning
                                >> Implemented the solution in about 20 minutes now
                                >> Spent around half hour in the morning to further tweak the last nights solution
                                >> This question has an interesting approach towards recursion and combinatorics
                                >> Matter is closed now.
[+]Space Complexity          : O(2^N)
[+]Time Complexity           : O(2^N)
[+]Level                     : MEDIUM
[+]Tread Speed               : Relaxed
[+]LINK                      : https://www.interviewbit.com/problems/nearest-smaller-element
[+] Supplement Sources       : N/A

'''

#Accepted but unelegant if that's even some word
def driver_obsolete(value, position):
    if position == 1:
        return [[x] for x in range(1, value+1)]
    def combine(value, index, value_limit, index_limit):
        # print("index: "+str(index)+" value: "+str(value))
        if index == index_limit and value <= value_limit:
            return [[value]]
        if index > index_limit or value > value_limit:
            return None
        solution = []
        for i in range(value, value_limit + 1):
            for j in range(i + 1, value_limit + 1):
                # print("Checking for index: " + str(index+1) + " value: " + str(j) + " for value: "+ str(i))
                temp = combine(j, index + 1, value_limit, index_limit)
                if temp:
                    for item in temp:
                        # print("\tadded to solution: " + str([i] + item))
                        if not solution or solution[-1] != [i] + item:
                            solution.append([i] + item)
        return solution
    return combine(1, 1, value, position)

#ACCEPTED BUT CAN BE OPTIMIZED
def combine_obsolete(value, position):
    solution, ans = [],  []
    for v in range(1, value+1):
        temp = []
        for item in solution:
            intermediate = item + [v]
            if len(intermediate) == position:
                ans.append(intermediate)
            else:
                temp.append(intermediate)
            temp.append(item)
        temp.append([v])
        solution = temp
    return sorted(ans)

# Fails some test cases
def drive(value, length):
    if length == 1:
        return [[x] for x in range(1, value+1)]
    def combine(value, index, max, length):
        if index == length:
            return [[value]]
        if index > length or value > max:
            return []
        result = []
        for new_value in range(value, max+1):
            for new_value_combine in range(new_value+1, max+1):
                for item in combine(new_value_combine, index+1, max, length):
                    if not result or [new_value]+item != result[-1]:
                        result.append([new_value]+item)
        return result
    return combine(1, 1, value, length)

#Most elegant and efficient solution
def drive(value, length):
    def combine(value, index, max, length):
        if index == length+1:
            return [[]]
        if index > length+1 or value > max:
            return []
        result = []
        for new_value in range(value, max+1):
            for item in combine(new_value+1,index+1, max, length):
                result.append([new_value]+item)
        return result

    return combine(1, 1, value, length)

if __name__ == '__main__':
    test_cases = [
        [4,2],
        [5,2],
        [4, 3],
        [5,1]
    ]
    for test_case in test_cases:
        print("Input: "+str(test_case)
              + "\n\t Naive: " + str(driver_obsolete(test_case[0], test_case[1]))
              + "\n\t NEW  : " + str(drive(test_case[0], test_case[1])))

    a = list(map(int, input("\nEnter the numbers : ").strip().split()))[:n]
