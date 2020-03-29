'''

[+]Temporal marker           : 10:51 Hours | Saturday 28, 2020
[+]Temporal marker untethered: 10:46 Hours | Sunday 29, 2020
[+]Comments                  : Coulnd't solve in optimal setting
                                Devised the basic approach using hint
                                Couldn't implement the correct solution
                                I was finally tired and used the editorial solution
                                matter is closed now
[+]Space Complexity          : O(N)
[+]Time Complexity           : O(N)
[+]Level                     : MEDIUM
[+]Tread Speed               : Relaxed
[+]LINK                      : https://www.interviewbit.com/problems/nearest-smaller-element
[+] Supplement Sources       : N/A

'''

# TLE
def getPermutation_obsolete(A, B):
    import itertools as iter
    lis = [x for x in range(1, A+1)]
    ans =  [x for x in iter.permutations(lis)][B-1]
    solution = ""
    for x in ans:
        solution += str(x)
    return solution

#EDITORIAL SOLUTION
def getPermutation(n, k):
    import math
    lis = [x for x in range(1, n+1)]
    permutation = ""
    k -= 1
    while n > 0:
        n -= 1
        index, k = divmod(k,math.factorial(n))
        permutation += str(lis[index])
        lis = lis[:index]+lis[index+1:]
    return permutation

if __name__ == '__main__':
    #print(permute([x for x in range(1,4)]))
    length = 4
    import math
    for index in range(1, math.factorial(length)+1):
        print(index,end=" >> :")
        print(getPermutation(length, index))
    #print(getPermutation(3,5))