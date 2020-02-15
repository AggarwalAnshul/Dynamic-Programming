"""
Validate if a given string is numeric.

Examples:

"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
Return 0 / 1 ( 0 for false, 1 for true ) for this problem

Clarify the question using “See Expected Output”

Is 1u ( which may be a representation for unsigned integers valid?
For this problem, no.
Is 0.1e10 valid?
Yes
-01.1e-10?
Yes
Hexadecimal numbers like 0xFF?
Not for the purpose of this problem
3. (. not followed by a digit)?
No
Can exponent have decimal numbers? 3e0.1?
Not for this problem.
Is 1f ( floating point number with f as prefix ) valid?
Not for this problem.
How about 1000LL or 1000L ( C++ representation for long and long long numbers )?
Not for this problem.
How about integers preceded by 00 or 0? like 008?
Yes for this problem


[+]Temporal marker           : Sat, 16:21 | Feb 15, 20
[+]Temporal marker untethered: Sat, 16:38 | Feb 15, 20
[+]Comments                  : The problem per se was not difficult
                                *Accounting for all the validations and corner cases was the main task
                                *Matter is closed now
                                *A much more efficient solution can certainly be devised.
[+]Space Complexity          : O(1)
[+]Time Complexity           : O(N)
[+]Level                     : MEDIUM
[+]Tread Speed               : Paced
[+]LINK                      : https://www.interviewbit.com/problems/alid-number
[+] Supplement Sources       : N/A
"""


# Check whether there is a sign preceding number of not
# serves to ignore the sign
def checkSign(string):
    if len(string) > 0:
        if string[0] == "-" or string[0] == "+":
            return string[1:]
    return string


# Find the number of numerals in the string provided
# Returns the index which is not numeral in this substring
def findNumber(string):
    length = len(string)
    index = 0
    num = ""
    while index < length and string[index].isdigit():
        num += string[index]
        index += 1
    return index


# Validation after encountering exp operator
# Returns whether the substring after exp is a number or not
def afterExponent(string):
    length = len(string)
    if length > 0:
        string = checkSign(string)
        if len(string) == 0 and not string[0].isdigit():
            return 0
        index = findNumber(string)
        if index < len(string):
            return 0
        return 1
    return 0


# Validations after encountering Decimal operator
# Returns whether the substring after decimal is num or not
def afterDecimal(string):
    # print("i receieved..."+string)
    if len(string) > 0:
        rightIndex = findNumber(string)
        # print('right index is...'+str(rightIndex))
        if rightIndex == 0:
            return 0
        elif rightIndex >= len(string):
            return 1
        elif rightIndex < len(string):
            if string[rightIndex] == "e":
                return afterExponent(string[rightIndex + 1:])
            else:
                return 0
    return 0


# THE DRIVER CODE
def findSolution(string):
    # print("received: " + string)
    string = string.lstrip()
    string = string.rstrip()
    # print("stripped string is: " + string)
    if len(string) > 0:
        string = checkSign(string)
        # print("after checking sign string is: " + string)
        if len(string) == 0:
            return 0
        # print('finding number...')
        index = findNumber(string)
        # print('break found at...'+str(index))
        length = len(string)
        if index < length:
            # print('we have a break...')
            string = string[index:]
            if string[0] == ".":
                # print('\twe have a decimal!')
                return afterDecimal(string[1:])
            elif string[0] == "e":
                # print('\tWe have an exponent..')
                return afterExponent(string[1:])
            else:
                return 0
        # print('letting it go..')
        return 1
    return 0


if __name__ == '__main__':
    test_cases = ["0", " 0.1 ", "abc", "1 a", "2e10",
                  "32467826570812365702673647926314796457921365792637946579269236594265794625762375621765476592146926410592659021465904652.687236478235187653874637824647856428756387264578245676579032657906097542609  ",
                  "+      ", " +", "      "]
    for test_case in test_cases:
        print("checking for : " + test_case, end=" \n\t")
        print("Answer >> " + str(findSolution(test_case)))
