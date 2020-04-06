"""
Programming Hashing Equal
Equal
Asked in:  
Facebook
Given an array A of integers, find the index of values that satisfy A + B = C + D, where A,B,C & D are integers values in the array

Note:

1) Return the indices `A1 B1 C1 D1`, so that 
  A[A1] + A[B1] = A[C1] + A[D1]
  A1 < B1, C1 < D1
  A1 < C1, B1 != D1, B1 != C1 

2) If there are more than one solutions, 
   then return the tuple of values which are lexicographical smallest. 

Assume we have two solutions
S1 : A1 B1 C1 D1 ( these are values of indices int the array )  
S2 : A2 B2 C2 D2

S1 is lexicographically smaller than S2 iff
  A1 < A2 OR
  A1 = A2 AND B1 < B2 OR
  A1 = A2 AND B1 = B2 AND C1 < C2 OR 
  A1 = A2 AND B1 = B2 AND C1 = C2 AND D1 < D2
Example:

Input: [3, 4, 7, 1, 2, 9, 8]
Output: [0, 2, 3, 5] (O index)
If no solution is possible, return an empty list.
"""
"""
[+]Temporal marker            :0949 Hours | Monday 06, 2020
[+]Temporal marker Untethered :1008 Hours | Monday 06, 2020
[+]Comments                   : EASy
[+]Space Complexity           : O(N*N)
[+]Time Complexity            : O(N*N)
[+]Level                      : EASY
[+]Tread Speed                : PACED
[+]LINK                      : https://www.interviewbit.com/problems/equal.py
[+] Supplement Sources       : N/A

"""

# ACCEPTED
# OBSOLETE, FULLY ACCEPTED
"""
def equal_obsolete(lis):
    length, hashmap = len(lis), {}

    for i_index in range(length):
        for j_index in range(i_index+1, length):
            current_sum = lis[i_index] + lis[j_index]
            if current_sum not in hashmap:
                hashmap[current_sum] = [[i_index, j_index]]
            else:
                hashmap[current_sum] += [[i_index, j_index]]


    for i_index in range(length):
        for j_index in range(i_index + 1, length):
            current_sum = lis[i_index] + lis[j_index]
            if current_sum in hashmap:
                for quadruple in hashmap[current_sum]:
                    if not(quadruple[0] == i_index or quadruple[1] == j_index) and not (quadruple[0] == j_index or quadruple[1] == i_index):
                        return [i_index, j_index, quadruple[0], quadruple[1]]
"""
# Accepted, I'm using this as the supreme solution
#OBSOLETE_2, FULLY ACCEPTED
"""
def equal(lis):
    length, hashmap = len(lis), {}
    ans = []

    for i_index in range(length):
        for j_index in range(i_index + 1, length):
            current_sum = lis[i_index] + lis[j_index]
            if current_sum in hashmap:
                for quadruple in hashmap[current_sum]:
                    if not ((quadruple[0] == i_index or quadruple[1] == j_index) and
                            not (quadruple[0] == j_index or quadruple[1] == i_index)):
                        if quadruple[0] < i_index:
                            new_answer = [quadruple[0],quadruple[1], i_index, j_index]
                        else:
                            new_answer = [i_index, j_index,quadruple[0], quadruple[1]]
                        if not ans or ans > new_answer:
                            ans = new_answer
            else:
                hashmap[current_sum] = [[i_index, j_index]]
    return ans
"""

# ACCEPTED, Current Supreme
def equal(lis):
    length, hashmap = len(lis), {}
    ans = []

    for i_index in range(length):
        for j_index in range(i_index + 1, length):
            current_sum = lis[i_index] + lis[j_index]
            if current_sum in hashmap:
                    if not hashmap[current_sum][0] in [i_index,j_index] and not hashmap[current_sum][1] in [i_index, j_index]:
                        if hashmap[current_sum][0] < i_index:
                            new_answer = hashmap[current_sum]+[i_index, j_index]
                        else:
                            new_answer = [i_index, j_index] + hashmap[current_sum]
                        if not ans or ans > new_answer:
                            ans = new_answer
            else:
                hashmap[current_sum] = [i_index, j_index]
    return ans





if __name__ == "__main__":
    test_cases = [
        [3, 4, 7, 1, 2, 9, 8],
    ]
    for index in range(len(test_cases)):
        test_case = test_cases[index]
        print("input: "+str(test_case)+"\n\tOUTPUT: :"+str(equal(test_case)))
