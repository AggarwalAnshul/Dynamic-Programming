"""
/*DESC
Anagrams
Asked in:  
Amazon
Microsoft
Goldman Sachs
Given an array of strings, return all groups of strings that are anagrams. Represent a group by a list of integers representing the index in the original list. Look at the sample case for clarification.

 Anagram : a word, phrase, or name formed by rearranging the letters of another, such as 'spar', formed from 'rasp' 
 Note: All inputs will be in lower-case. 
Example :

Input : cat dog god tca
Output : [[1, 4], [2, 3]]
cat and tca are anagrams which correspond to index 1 and 4.
dog and god are another set of anagrams which correspond to index 2 and 3.
The indices are 1 based ( the first element has index 1 instead of index 0).

 Ordering of the result : You should not change the relative ordering of the words / phrases within the group. Within a group containing A[i] and A[j], A[i] comes before A[j] if i < j. 
Seen this question in a real interview beforeYesNo
*/

[+]Temporal marker            :0920 Hours | Monday 06, 2020
[+]Temporal marker Untethered :0937 Hours | Monday 06, 2020
[+]Comments                   : ~ 5 minutes in reading and preparing the workspace
                                ~ 1 minute in checking and submitting the solution
                                Devised solution at par with the editorial solution
                                Matter is officially closed now 
[+]Space Complexity           : O(N)
[+]Time Complexity            : O(N)
[+]Level                      : EASY
[+]Tread Speed                : PACED
[+]LINK                      : https://www.interviewbit.com/problems/anagrams.py
[+] Supplement Sources       : N/A

"""


# ACCEPTED
def anagrams(lis):
    hashmap = {}
    for index, value in enumerate(lis):
        value = ''.join(sorted(value))
        if value in hashmap:
            hashmap[value] += [index+1]
        else:
            hashmap[value] = [index + 1]
    return [hashmap[key] for key in hashmap]


if __name__ == "__main__":
    test_cases = [
        ["booyah", "god", "dog", "cat", "tca"],
        ["cat", "god", "dog", "tca"],
        ["cat", "dog", "act", "god", "tca"],

    ]
    for index in range(len(test_cases)):
        test_case = test_cases[index]
        print("input: "+str(test_case)+"\n\tOUTPUT: :" +
              str(anagrams(test_case)))
