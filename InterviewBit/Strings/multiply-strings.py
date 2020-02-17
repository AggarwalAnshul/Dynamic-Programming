"""
Given two numbers represented as strings, return multiplication of the numbers as a string.

 Note: The numbers can be arbitrarily large and are non-negative.
Note2: Your answer should not have leading zeroes. For example, 00 is not a valid answer.
For example,
given strings "12", "10", your answer should be “120”.

NOTE : DO NOT USE BIG INTEGER LIBRARIES ( WHICH ARE AVAILABLE IN JAVA / PYTHON ).
We will retroactively disqualify such submissions and the submissions will incur penalties.


[+]Temporal marker           : Mon, 18:50 | Feb 17, 20
[+]Temporal marker untethered: Mon, 19:13 | Feb 17, 20
[+]Comments                  :EASY
[+]Space Complexity          : O(N*M)
[+]Time Complexity           : O()
[+]Level                     :EASY
[+]Tread Speed               :PACED
[+]LINK                      : https://www.interviewbit.com/problems/multiply-strings
[+] Supplement Sources       : N/A
"""


def findSolution(one, two):
    if len(one) < len(two):
        return findSolution(two, one)
    length_one = len(one)
    length_two = len(two)
    ans = 0
    offset = 1
    for y in range(length_two - 1, -1, -1):
        if y < length_two-1:
            offset *= 10
        multiplier = int(two[y])
        product = ""
        carry = 0
        for z in range(length_one - 1, -1, -1):
            multiply = carry + int(one[z]) * multiplier
            multiply = str(multiply)
            carry = multiply[:-1]
            if carry == "":
                carry = 0
            else:
                carry = int(carry)
            product = multiply[-1] + product
        #print("before adding carry...product[0] :"+str(product[0])+" Carry: "+str(carry)+" pro:"+str(product))
        product = str(carry) + product
        #print("adding to the solution..."+str(product))
        ans += int(product)*offset
    return ans


if __name__ == "__main__":
    data = [["12", "5"], ["10000", '6'], ["0", '100'], ["100","25"],["99999", "99999"]]
    for x in data:
        print("input: " + str(x) + " >> " + str(findSolution(x[0], x[1])))
