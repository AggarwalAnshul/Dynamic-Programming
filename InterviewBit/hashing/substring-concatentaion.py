'''
    Substring Concatenation

Substring Concatenation

    Asked in:
    Facebook

You are given a string, S, and a list of words, L, that are all of the same length.

Find all starting indices of substring(s) in S that is a concatenation of each word in L exactly once and without any intervening characters.

Example :

S: "barfoothefoobarman"
L: ["foo", "bar"]

You should return the indices: [0,9].
(order does not matter).

'''
'''

[+]Temporal marker           :N/A
[+]Temporal marker untethered: N/A
[+]Comments                  : NO COMMENTS FOUND FOR THIS ONE
                                FILE DELETED ACCIDENTALLY FORM VS CODE GIT
                                IMPORTED FORM IB SOLUTION
                                ------- PARTIAL COMMENTS ---------
                                LAID IT OFF ON THE INITIAL DAY
                                SAW PARTIAL IMPLEMENTATION FROM GFG, 40%
                                IMPLEMENTED IN ABOUT AN HOUR
                                MATTER IS OFFICIALLY CLOSED NOW

[+]Space Complexity          : O(N)
[+]Time Complexity           : O(N)
[+]Level                     : MEDIUM | uPPPER
[+]Tread Speed               : RELAXED
[+]LINK                      : https://www.interviewbit.com/problems/nearest-smaller-element
[+] Supplement Sources       : N/A

'''


def findSubstring(string, list_of_words):
    hashset = {}
    for word in list_of_words:
        hashset[word] = hashset.get(word, 0) + 1

    ans = []
    word_size = len(list_of_words[0])
    substring_size = len(list_of_words) * word_size

    for i in range(len(string) - substring_size + 1):
        flag = 0
        tempset = hashset.copy()
        for j in range(i, i + substring_size, word_size):
            word = string[j:j + word_size]
            if word not in tempset:
                flag = 1
            else:
                if tempset[word] == 1:
                    tempset.pop(word)
                else:
                    tempset[word] -= 1
        if flag == 0 and not tempset:
            ans.append(i)
    return ans

if __name__ == '__main__':
    test_cases = [
        ["barfoothefoobarman", ["foo", "bar"] ],
    ]
    for index in range(len(test_cases)):
        test_case = test_cases[index]
        print("Input: "+str(test_case)+"\nOUTPUT: "+str(findSubstring(test_case[0], test_case[1])))