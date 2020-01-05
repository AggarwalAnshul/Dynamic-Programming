#M.76

"""
 Given two integers n and k, count the number of binary strings of length n
  with k as number of times adjacent 1’s appear.

Examples:

Input  : n = 5, k = 2
Output : 6
Explanation:
Binary strings of length 5 in which k number of times
two adjacent set bits appear.
00111
01110
11100
11011
10111
11101

Input  : n = 4, k = 1
Output : 3
Explanation:
Binary strings of length 3 in which k number of times
two adjacent set bits appear.
0011
1100
0110

[+]Temporal marker            :  Sun, 11:56 | Jan 05, 20
[+]Temporal marker untethered :  Sun, 11:56 | Jan 05, 20
[+]Comments                   : *
                                *
                                *
[+]Level                      :
[+]Tread speed                :
[+]LINK                       : https://www.geeksforgeeks.org/count-binary-strings-k-times-appearing-adjacent-two-set-bits
"""

def findSolution(previous, count, k, ans, length, str):
    if(length==0):
        return ans
    if(previous==0):
        return (findSolution(0, count, k, ans, length-1, str+"0") +
               findSolution(1, count,k,  ans, length-1, str+"1"))
    if(previous==1):
        a = 0
        b = 0
        a = findSolution(0, count, k, ans, length-1, str+"0")
        if(count+1<=k):
            if(count+1==k):
                ans+=1
                print(str+"1")
            b = findSolution(1, count+1, k, ans, length-1,str+"1")
        return a+b

if __name__ == "__main__":
    print(findSolution(0, 0, 2, 0, 5, "0"))