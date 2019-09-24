"""
#M.1
Lobb Number
In combinatorial mathematics, the Lobb number Lm, n counts the number of ways that n + m open parentheses can be arranged to form the start of a valid sequence of balanced parentheses.
The Lobb number are parameterized by two non-negative integers m and n with n >= m >= 0. It can be obtained by:
 L_{m,n} = \frac{2\times m + 1}{m + n + 1}\binom{2\times n}{m + n} 

Lobb Number is also used to count the number of ways in which n + m copies of the value +1 and n – m copies of the value -1 may be arranged into a sequence such that all of the partial sums of the sequence are non- negative.

Examples :

Input : n = 3, m = 2
Output : 5

Input : n =5, m =3
Output :35
[+]Temporal marker            : 11:25 Hours | Thursday, Sept05, 19
[+]Temporal marker untethered : 11:28 Hours | Thursday, Sept05, 19
[+]Comments                   : Problem Poorly/Vaguely describled
                                Laying off the prob. until further light on the matter
[+]Tread speed                : N/A 
[+]Level                      : N/A
[+]LINK                       : https://www.geeksforgeeks.org/lobb-number/
"""
def findSolution(m, n)

if __name__ == "__main__":
    m = 2
    n = 3
    print(findSolution(2,3))
