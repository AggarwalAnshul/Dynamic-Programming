"""

Programming Hashing Window String
Window String
Asked in:  
Google
Directi
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in linear time complexity.
Note that when the count of a character C in T is N, then the count of C in minimum window in S should be at least N.

Example :

S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC"

 Note:
If there is no such window in S that covers all characters in T, return the empty string ''.
If there are multiple such windows, return the first occurring minimum window ( with minimum start index ).

"""
"""
[+]Temporal marker            :1246 Hours | Tuesday 07, 2020
[+]Temporal marker Untethered :1246 Hours | Tuesday 07, 2020
[+]Comments                   : Laying off @ 1439 Hours very lighyt
[+]Space Complexity           : O()
[+]Time Complexity            : O()
[+]Level                      : 
[+]Tread Speed                :
[+]LINK                      : https://www.interviewbit.com/problems/window-string.py
[+] Supplement Sources       : N/A

"""

# OBSOLETE, Giving partial results
def windowString_partial(string, target):
    global_set = set(char for char in target)
    working_set = list(target)
    stack = []
    length = len(string)
    ans = ""
    start, end = 0, 0
    while start < length and end < length:
        if not working_set:
            propect_ans = string[start:end]
            if len(propect_ans) == len(target):
                return propect_ans
            if not ans or len(ans) > len(propect_ans):
                ans = propect_ans
            removed = stack.pop(0)
            working_set = [removed]
            while string[start] != stack[0]:
                start += 1
            if removed in stack:
                working_set = []
                continue

        current_char = string[end]
        if current_char in global_set:
            stack.append(current_char)
            if current_char in working_set:
                working_set.remove(current_char)
        end += 1
    if not working_set:
        propect_ans = string[start:end+1]
        if len(ans) > len(propect_ans):
            ans = propect_ans
    return ans


def windowString_abandoned(string, target):
    global_set = set(target)
    checklist, worklist = {}, {}
    start, end = 0, 0
    final_window, length = "", len(string)
    ans = ""

    # Initialize the data
    for char in target:
        if char in checklist:
            checklist[char] += 1
        else:
            checklist[char] = 1

    while start < length and end < length:
        if checklist:
            current_char = string[end]
            if current_char in global_set:
                # add in working set
                if current_char not in worklist:
                    worklist[current_char] = 1
                else:
                    worklist[current_char] += 1
                
                #remove from the checklist
                if current_char in checklist:
                    if checklist[current_char] == 1:
                        checklist.pop(current_char)
                    else:
                        checklist[current_char] -= 1
            end += 1
        else:
            # check if it's the answer
            if end - start == len(target):
                return string[start:end]
            if not ans or len(ans) > end - start:
                ans = string[start:end]
            #remove the first
            removed_char = string[start]
            checklist[removed_char] = 1
            if removed_char in worklist:
                if worklist[removed_char] == 1:
                    worklist.pop(removed_char)
                else:
                    worklist[removed_char] -= 1
            if string[start] in worklist:
                checklist = {}
            start += 1
            while start < length and string[start] not in global_set:
                start += 1

    if not ans or len(ans) > end - start:
        ans = string[start:end]
    return ans


def windowString(string, target):
    characters_seen, checklist = {}, {}
    global_set = set(target)
    start, end = 0, 0
  
    # preparing the data
    for char in target:
        if char in checklist:
            checklist[char] += 1
        else:
            checklist[char] = 1
    
    while start < length and end < length:
        

        

    

if __name__ == "__main__":
    test_cases = [
        ["ADOBECODEBANC", "ABC"],
        ["AAAAAA", "AA"],
        ["ABCEDFG", "ED"],
    ]
    for index in range(len(test_cases)):
        test_case = test_cases[index]
        print("input: "+str(test_case)+"\n\tOUTPUT: :" +
              str(windowString(test_case[0], test_case[1])))
