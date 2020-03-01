"""
Kth Smallest Element in the Array
Find the kth smallest element in an unsorted array of non-negative integers.

Definition of kth smallest element

 kth smallest element is the minimum possible n such that there are at least k elements in the array <= n.
In other words, if the array A was sorted, then A[k - 1] ( k is 1 based, while the arrays are 0 based )
NOTE
You are not allowed to modify the array ( The array is read only ).
Try to do it using constant extra space.

Example:

A : [2 1 4 3 2]
k : 3

answer : 2

[+]Temporal marker           : Fri, 22:28 | Feb 28, 20
[+]Temporal marker untethered: Fri, 22:28 | Feb 28, 20
[+]Comments                  :
[+]Space Complexity          : O()
[+]Time Complexity           : O()
[+]Level                     :
[+]Tread Speed               :
[+]LINK                      : https://www.interviewbit.com/problems/kth-smallest-element-in-the-array
[+] Supplement Sources       : N/A
"""

def findSolution(lis, k):
    mask = 0
    aux = [0 for x in range(32)]
    for element in lis:
        mask ^= 1 << element
    check = 0
    count = 0
    while 1 > 0:
        print("checking for: "+str(check))
        if mask & 1 << check:
            count += 1
            print("\tths is "+str(count)+" th element")
        if count == k:
            return check
        check += 1


if __name__ == "__main__":
    data = [[[2,1,4,3,2],3]]
    for x in data:
        print("input: " + str(x) + " >> " + str(findSolution(x[0], x[1])))