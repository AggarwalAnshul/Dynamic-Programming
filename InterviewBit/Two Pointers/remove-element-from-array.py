"""
Remove Element from Array
Asked in:
Amazon
Remove Element

Given an array and a value, remove all the instances of that value in the array.
Also return the number of elements left in the array after the operation.
It does not matter what is left beyond the expected length.

 Example:
If array A is [4, 1, 1, 2, 1, 3]
and value elem is 1,
then new length is 3, and A is now [4, 2, 3]
Try to do it in less than linear additional space complexity.


[+]Temporal marker           : Fri, 17:3 | Feb 28, 20
[+]Temporal marker untethered: Fri, 17:08 | Feb 28, 20
[+]Comments                  : Cleared in first attempt
[+]Space Complexity          : O(1)
[+]Time Complexity           : O(N)
[+]Level                     :EASY
[+]Tread Speed               :PACED
[+]LINK                      : https://www.interviewbit.com/problems/remove-element-from-array
[+] Supplement Sources       : N/A
"""

def findSolution(lis, target):
    print("target is : "+str(target))
    length = len(lis)
    nextIndex = 0
    count = 0
    for index in range(length):
        if lis[index] != target:
            lis[nextIndex] = lis[index]
            nextIndex += 1
            count += 1
    return str(count) + " >> " +str(lis)


if __name__ == "__main__":
    data = [[[4, 1, 1, 2, 1, 3], 1]]
    for x in data:
        print("input: " + str(x) + " >> " + str(findSolution(x[0], x[1])))