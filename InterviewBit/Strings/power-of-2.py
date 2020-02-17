"""

[+]Temporal marker           : Mon, 13:33 | Feb 17, 20
[+]Temporal marker untethered: Mon, 13:33 | Feb 17, 20
[+]Comments                  :
[+]Space Complexity          : O()
[+]Time Complexity           : O()
[+]Level                     :
[+]Tread Speed               :
[+]LINK                      : https://www.interviewbit.com/problems/power-of-2
[+] Supplement Sources       : N/A
"""


def findSolution(number):
    #print("checking for Num: "+str(number))
    length = len(number)
    remainder = ""
    while int(number) > 2:
        #print("\t"+str(number))
        index = 0
        length = len(number)
        divisor = ""
        while index < length:
            char = int(remainder + number[index])
            if char == 1:
                char = int(remainder + number[index:index + 2])
                index += 2
                divisor += "0"
                remainder = str(char % 2)
                divisor += str(char // 2)
            else:
                remainder = str(char % 2)
                divisor += str(char // 2)
                index += 1
        if not int(remainder) == 0 or not int(divisor[-1]) % 2 == 0:
            return 0
        number = divisor
    if int(number) == 2:
        return 1
    return 0


# def findSolution(number):
#     if int(number) == 2:
#         return 1
#     # print("checking for: "+str(number))
#     length = len(number)
#     index = 0
#     remainder = ""
#     divisor = ""
#     while index < length:
#         # print("index: "+str(index))
#         char = int(remainder + number[index])
#         if char == 1:
#             char = int(remainder + number[index:index + 2])
#             index += 2
#             divisor += "0"
#             remainder = str(char % 2)
#             divisor += str(char // 2)
#         else:
#             remainder = str(char % 2)
#             divisor += str(char // 2)
#             # print("\tworking with: " + str(char))
#             index += 1
#
#         # print("\t\tRemainder: "+str(remainder))
#     # print(">><< Remainder: " + str(remainder))
#     # print(">>DIVISOR: " + str(divisor))
#     if remainder != "0" or (int(divisor[-1]) % 2 != 0):
#         return 0
#     return findSolution(divisor)


if __name__ == "__main__":
    data = ["153", "128", "37778931862957161709568", "20", "1024", "1028", "514"]
    for x in data:
        print("input: " + str(x) + " >> " + str(findSolution(x)))
