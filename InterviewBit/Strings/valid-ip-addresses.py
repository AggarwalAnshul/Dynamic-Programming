"""

[+]Temporal marker           : Sat, 17:54 | Feb 15, 20
[+]Temporal marker untethered: Sat, 19:54 | Feb 15, 20
[+]Comments                  :
[+]Space Complexity          : O()
[+]Time Complexity           : O()
[+]Level                     :
[+]Tread Speed               :
[+]LINK                      : https://www.interviewbit.com/problems/valid-ip-addresses
[+] Supplement Sources       : N/A
"""


def findSolution(string, group, prev, offset):
    offset += " "
    print(offset + string + " length: " + str(len(string)) + " group: " + str(group) + " PREV: " + prev)
    length = len(string)
    if group == 3 and length == 0:
        print(offset + "returning: " + prev)
        return [prev]
    elif length == 0 and group < 3:
        print('returning negative...')
        return None
    elif group >= 3 and length >= 0:
        print(offset + "returning none...")
        return None

    ans = []
    for i in range(0, 3):
        if i <= len(string) - 1:
            if int(string[:i + 1]) < 256:
                if string[0] != "0" or (string[0] == "0" and len(string[:i + 1]) == 1):
                    lis = findSolution(string[i + 1:], group + 1, string[:i + 1], offset)
                    if lis is not None:
                        for x in range(len(lis)):
                            el = lis[x]
                            ans.append(prev + "." + el)
                        print(offset + 'added to answer: ' + str(lis))

    return ans


def driver(string):
    length = len(string)
    if 12 < length < 4:
        return ""
    ans = []
    for i in range(0, 3):
        if i <= len(string) - 1:
            if int(string[:i + 1]) < 256:
                if string[0] != "0" or (string[0] == "0" and len(string[:i + 1]) == 1):
                    lis = findSolution(string[i + 1:], 0, string[:i + 1], " ")
                    if lis is not None:
                        for x in range(len(lis)):
                            el = lis[x]
                            # lis[x] = string[:i + 1] + "." + el
                        ans += lis
    return ans


if __name__ == '__main__':
    string = "11234"
    string = "25525511135"
    string = "0100100"
    string = "010010"
    print(driver(string))
