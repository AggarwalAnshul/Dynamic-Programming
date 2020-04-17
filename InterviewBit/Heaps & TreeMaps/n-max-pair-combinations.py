'''

    Asked in:  
    Liv.ai

Problem Setter: dhruvi Problem Tester: ganeshk2

Given two arrays A & B of size N each.
Find the maximum N elements from the sum combinations (Ai + Bj) formed from elements in array A and B.

For example if A = [1,2], B = [3,4], then possible pair sums can be 1+3 = 4 , 1+4=5 , 2+3=5 , 2+4=6
and maximum 2 elements are 6, 5

Example:

N = 4
a[]={1,4,2,3}
b[]={2,5,1,6}

Maximum 4 elements of combinations sum are
10   (4+6), 
9    (3+6),
9    (4+5),
8    (2+6)


'''

'''

[+]Temporal marker           : 14:14 Hours | Friday 17, 2020
[+]Temporal marker untethered: 14:14 Hours | Friday 17, 2020
[+]Comments                  :
[+]Space Complexity          : O()
[+]Time Complexity           : O()
[+]Level                     :
[+]Tread Speed               :
[+]LINK                      : https://www.interviewbit.com/problems/nearest-smaller-element
[+] Supplement Sources       : N/A

'''

# MLE
# @ param lisA: list A
# @ param lisB: list B
# return len(lisA) maximum pairs among the total pairs
def operate(lisA, lisB):
    import heapq
    lengthA, lengthB = len(lisA), len(lisB)
    heap = []
    ans = []
    for itemA in lisA:
        for itemB in lisB:
            heapq.heappush(heap, (itemA+itemB, (itemA, itemB)))

    total_pairs = lengthA * lengthB
    ignore = total_pairs - lengthA
    count = 0
    for count in range(total_pairs):
        temp = heapq.heappop(heap)[1]
        if count >= ignore:
            ans = [temp] + ans
        count += 1
    return ans


if __name__ == '__main__':
    test_cases = [
        [[1, 2], [3, 4]],
        [[1,4,2,3],[2,5,1,6]],
    ]
    for index in range(len(test_cases)):
        test_case = test_cases[index]
        print("Input: " + str(test_case) +"\nOUTPUT: "+str(operate(test_case[0], test_case[1])))
