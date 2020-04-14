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
[+]Temporal marker Untethered :1520 Hours | Tuesday 14, 2020
[+]Comments                   :
                                Laying off @ 1439 Hours very light
                                Finally this is solved
                                I did figure the approach on day one
                                couldn't implement properly
                                finally today, saw partial implementation from GFG 40%
                                Implemented in about an hour
                                this matter is officially closed now

[+]Space Complexity           : O(N)
[+]Time Complexity            : O(N)
[+]Level                      :  MEDIUM | UPPER
[+]Tread Speed                : SUPER RELAXED & LAID OFF
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
        propect_ans = string[start:end + 1]
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

                # remove from the checklist
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
            # remove the first
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


# ACCEPTED!
def windowString(string, pattern):
    window_start, window_length, min_window = 0, 0, ""
    string_length, pattern_length = len(string), len(pattern)
    pattern_hash, string_hash = {}, {}

    # hashing the pattern
    for char in pattern:
        pattern_hash[char] = pattern_hash.get(char, 0) + 1

    # finding the minimum window
    for index, char in enumerate(string):
        if char in pattern_hash:
            string_hash[char] = string_hash.get(char, 0) + 1
            if string_hash.get(char) <= pattern_hash.get(char):
                window_length += 1

        # Prospective window found
        if window_length == pattern_length:
            # Stripping the window from the start
            while (not pattern_hash.get(string[window_start], None) or
                   string_hash[string[window_start]] > pattern_hash[string[window_start]]):
                string_hash[string[window_start]] = string_hash.get(string[window_start], 1) - 1
                window_start += 1
            # Assigning the new window
            if not min_window or len(min_window) > len(string[window_start:index + 1]):
                min_window = string[window_start:index + 1]
            # Discarding the first window character
            string_hash[string[window_start]] = string_hash.get(string[window_start],
                                                                1) - 1  # 1 so that hashvalue not gets in negative for single instance
            window_length, window_start = window_length - 1, window_start + 1
    return min_window


if __name__ == "__main__":
    test_cases = [
        ["ADOBECODEBANC", "ABC"],
        ["AAAAAA", "AA"],
        ["ABCEDFG", "ED"],
    ]
    for index in range(len(test_cases)):
        test_case = test_cases[index]
        print("input: " + str(test_case) + "\n\tOUTPUT: :" +
              str(windowString(test_case[0], test_case[1])))
