"""

[+]Temporal marker           : Sat, 15:12 | Feb 15, 20
[+]Temporal marker untethered: Sat, 15:43 | Feb 15, 20
[+]Comments                  : Wasted time as iB has different sys.maxSize. They have the wrong value
                               Devised the approach w/o regex. It's Good
[+]Space Complexity          : O(1)
[+]Time Complexity           : O(N)
[+]Level                     : EASY
[+]Tread Speed               : Intermittent
[+]LINK                      : https://www.interviewbit.com/problems/atoi
[+] Supplement Sources       : N/A
"""


def findSolution(string):
    import sys
    flag = 0

    # Handling preceding positive/negative signs
    if string[0] == "+":
        string = string[1:]
    elif string[0] == "-":
        string = string[1:]
        flag = 1

    #Extracting the first number
    length = len(string)
    if not string[0].isdigit():
        return 0
    index = 0
    ans = ""

    while index < length and string[index].isdigit():
        ans += string[index]
        index += 1
    ans = int(ans)

    # Handling the overflow...
    if flag == 1:
        ans = ans * -1
        if ans < -(sys.maxsize)-1:
            return -(sys.maxsize)-1
    if ans > sys.maxsize:
        return sys.maxsize
    return ans


if __name__ == '__main__':
    string = "a&&*#&$*#$&(#"
    string = "   12245*^3300"
    string = "1123,34"
    string = "7 U 0 T7165 0128862 089 39 5"
    string = "V515V 5793K 627 23815945269 1 1249794L 631 8755 7"
    string = " --7"
    string = "5121478262 8070067M75 X199R 547 8C0A11 93I630 4P4071 029W433619 M3 5 14703818 776366059B9O43393"
    print("ans: >> " + str(findSolution(string)))
