"""
Given an array of words and a length L, format the text such that each line has exactly L characters and is fully (left and right) justified.
You should pack your words in a greedy approach; that is, pack as many words as you can in each line.

Pad extra spaces ‘ ‘ when necessary so that each line has exactly L characters.
Extra spaces between words should be distributed as evenly as possible.
If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.
For the last line of text, it should be left justified and no extra space is inserted between words.

Your program should return a list of strings, where each string represents a single line.

Example:

words: ["This", "is", "an", "example", "of", "text", "justification."]

L: 16.

Return the formatted lines as:

[
   "This    is    an",
   "example  of text",
   "justification.  "
]
 Note: Each word is guaranteed not to exceed L in length.


[+]Temporal marker           : Wed, 12:32 | Feb 19, 20
[+]Temporal marker untethered: Wed, 13:35 | Feb 19, 20
[+]Comments                  :MEDIUM
[+]Space Complexity          : O(N)
[+]Time Complexity           : O(N)
[+]Level                     :MEDIUM
[+]Tread Speed               :Intermittent
[+]LINK                      : https://www.interviewbit.com/problems/justified-text
[+] Supplement Sources       : N/A
"""


def fullJustify(words, limit):
    values = []
    answer = []
    length = len(words)

    if length == 0:
        return answer

    for word in words:
        values.append(len(word))

    index = 0
    while index < length:
        tempIndex = index
        sum = values[index]
        spaces = 0
        while sum <= limit:
            if index + 1 >= len(words) or sum + values[index + 1] + 1 > limit:
                break
            else:
                index += 1
                sum += values[index] + 1
                spaces += 1
        diff = limit - sum + spaces
        if index == length - 1:
            mean = 1
            offset = 0
        elif spaces == 0:
            mean = 0
            offset = 0
        else:
            mean = diff // spaces
            offset = diff % spaces
        string = ""
        tempSum = 0
        while tempIndex <= index:
            string += words[tempIndex]
            tempSum += values[tempIndex]
            tempIndex += 1
            for x in range(0, mean):
                if tempSum + 1 <= limit:
                    string += " "
                    tempSum += 1
            if offset > 0:
                offset -= 1
                tempSum += 1
                string += " "
        while tempSum < limit:
            tempSum += 1
            string += " "
        print(">" + string + "<")
        answer.append(string)
        index += 1
    return answer


if __name__ == "__main__":
    data = [
        [["glu", "muskzjyen", "ahxkp", "t", "djmgzzyh", "jzudvh", "raji", "vmipiz", "sg", "rv", "mekoexzfmq",
         "fsrihvdnt", "yvnppem", "gidia", "fxjlzekp", "uvdaj", "ua", "pzagn", "bjffryz", "nkdd", "osrownxj", "fvluvpdj",
         "kkrpr", "khp", "eef", "aogrl", "gqfwfnaen", "qhujt", "vabjsmj", "ji", "f", "opihimudj", "awi", "jyjlyfavbg",
         "tqxupaaknt", "dvqxay", "ny", "ezxsvmqk", "ncsckq", "nzlce", "cxzdirg", "dnmaxql", "bhrgyuyc", "qtqt", "yka",
         "wkjriv", "xyfoxfcqzb", "fttsfs", "m"], 144],
        [["What", "must", "be", "shall", "be."], 12],
        [["This", "is", "an", "example", "of", "text", "justification."], 16],
        [["aaa", "bb", "cc", "ddddd"], 6]
        ]

    for x in data:
        print("input: " + str(x) + " >> " + str(fullJustify(x[0], x[1])))
