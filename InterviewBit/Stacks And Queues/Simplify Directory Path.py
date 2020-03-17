"""
Simplify Directory Path
Asked in:
Microsoft
Given a string A representing an absolute path for a file (Unix-style).

Return the string A after simplifying the absolute path.

Note:

Absolute path always begin with ’/’ ( root directory ).

Path will not have whitespace characters.



Input Format

The only argument given is string A.
Output Format

Return a string denoting the simplified absolue path for a file (Unix-style).
For Example

Input 1:
    A = "/home/"
Output 1:
    "/home"

Input 2:
    A = "/a/./b/../../c/"
Output 2:
    "/c"


[+]Temporal marker           : Tue, 18:41 | Mar 17, 20
[+]Temporal marker untethered: Tue, 17:01 | Mar 17, 20
[+]Comments                  : Took some time to understand the structure of unix file system and semantics
                                >Ate my supper
                                >coded in about 15 mins
                                >Oh Man!! Editorial is sooo efffing coooooool
                                >when I'll be able to think natively like THIS!
[+]Space Complexity          : O(N)
[+]Time Complexity           : O(N)
[+]Level                     : EASY
[+]Tread Speed               : Relaxed
[+]LINK                      : https://www.interviewbit.com/problems/Simplify Directory Path
[+] Supplement Sources       : N/A
"""
def simplifyPath(absolute_path):

    def stack_is_empty(stack):
        return len(stack) == 0

    i, length = 0, len(absolute_path)
    directory, flag = "", 0
    stack = []

    while i < length:
        if absolute_path[i] == "/":
            # start searching for directory
            if i+2 < length and absolute_path[i+1] == "." and absolute_path[i+2] == ".":
                # go back
                i += 3
                if not stack_is_empty(stack):
                    stack.pop()
            elif i+1 < length and absolute_path[i+1] == ".":
                # do nothing
                i += 2
            else:
                # start looking for directory
                i += 1
                while i < length and absolute_path[i] != "/":
                    directory += absolute_path[i]
                    i += 1
                    flag = 1
                if flag == 1:
                    stack.append(directory)
                    flag = 0
                    directory = ""
    absolute_path = ""
    if stack_is_empty(stack):
        return "/"
    for item in stack:
        absolute_path += "/"+item
    #print(stack)
    return absolute_path

def simplifyPath_editorial(absolute_path):
    simplified_path = []
    directories = absolute_path.split('/')
    for directory in directories:
        if directory == "" or directory == ".":
            continue
        elif directory == "..":
            if len(simplified_path) > 0:
                simplified_path.pop()
        else:
            simplified_path.append(directory)
    return '/'+'/'.join(simplified_path)

if __name__ == '__main__':
    test_cases = [
        "/home/",
        "/a/./b/../../c/",
        "/../",
        "/home//foo/"
    ]
    for test_case in test_cases:
        print("INPUT >> " + str(test_case)
              + "\n\t\t | OUTPUT >> " + str(simplifyPath(test_case))
              + " | EDITORIAL >> "+str(simplifyPath_editorial(test_case)))
