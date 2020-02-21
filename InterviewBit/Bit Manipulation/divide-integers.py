"""
Divide two integers without using multiplication, division and mod operator.

Return the floor of the result of the division.

Example:

5 / 2 = 2
Also, consider if there can be overflow cases. For overflow case, return INT_MAX.

Note: INT_MAX = 2^31 - 1


[+]Temporal marker           : Fri, 13:24 | Feb 21, 20
[+]Temporal marker untethered: Fri, 13:24 | Feb 21, 20
[+]Comments                  :
[+]Space Complexity          : O()
[+]Time Complexity           : O()
[+]Level                     :
[+]Tread Speed               :
[+]LINK                      : https://www.interviewbit.com/problems/divide-integers
[+] Supplement Sources       : N/A
"""

def findSolution(a, b):
    power = math.log(b) / math.log(2)



if __name__ == "__main__":
    data = []
    for x in data:
        print("input: " + str(x) + " >> " + str(findSolution(x)))