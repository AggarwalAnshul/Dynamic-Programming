"""
Given a string A representating json object. Return an array of string denoting json object with proper indentaion.

Rules for proper indentaion:

Every inner brace should increase one indentation to the following lines.
Every close brace should decrease one indentation to the same line and the following lines.
The indents can be increased with an additional ‘\t’
Note:

[] and {} are only acceptable braces in this case.

Assume for this problem that space characters can be done away with.




[+]Temporal marker           : Wed, 17:28 | Feb 19, 20
[+]Temporal marker untethered: Wed, 17:53 | Feb 19, 20
[+]Comments                  : Looks like judge isn't working
                               output looks correct though
                               Laying off this  problem for the time being
[+]Space Complexity          : O(N)
[+]Time Complexity           : O(N)
[+]Level                     :
[+]Tread Speed               :
[+]LINK                      : https://www.interviewbit.com/problems/pretty-json
[+] Supplement Sources       : N/A
"""


def prettyJSON(string):
    print(string)
    length = len(string)
    index = 0
    indent = ""
    json = ""
    import re
    while index < length:
        char = string[index]
        if char == "{" or char == "[":
            json += "\n" + indent + char
            indent += "\t"
        elif char == "}" or char == "]":
            indent = indent[:-1]
            json += "\n" + indent + char
        elif char == ',':
            json += ","
        else:
            # this is a character
            if index > 0:
                #print('index: '+str(index))
                previous = string[index-1]
                if previous == "{" or char == "[":
                    json += "\n" + indent + char
                elif previous == "}" or char == "]":
                    json += "\n" + indent + char
                elif previous == ",":
                    json += "\n" + indent + char
                else:
                    json += char
            else:
                json += char
        index += 1
        #print(json)
    return json

    #
    # while index < length:
    #     if re.match("{|}|[|]|,", string[index]):
    #         json += "\n"
    #     if string[index] == '{' or string[index] == '[':
    #         json += indent + string[index]
    #         indent += "\t"
    #         json += "\n" + indent
    #     elif string[index] == '}' or string[index] == ']':
    #         indent = indent[:-1]
    #         json += "\n" + indent + string[index]
    #         json += "\n" + indent
    #     elif string[index] == ",":
    #         json += ","
    #         json += "\n" + indent
    #     else:
    #         json += string[index]
    #     index += 1
    # return json


if __name__ == "__main__":
    data = ["{A:\"B\",C:{D:\"E\",F:{G:\"H\",I:\"J\"}}}",
            "[\"foo\", {\"bar\":[\"baz\",null,1.0,2]}]",
            "{\"id\":100,\"firstName\":\"Jack\",\"lastName\":\"Jones\",\"age\":12}"]
    for x in data:
        print("input: " + str(x) + " >> " + str(prettyJSON(x)))
