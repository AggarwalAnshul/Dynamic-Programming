'''

[+]Temporal marker           : 14:18 Hours | Tuesday 31, 2020
[+]Temporal marker untethered: 14:48 Hours | Tuesday 31, 2020
[+]Comments                  :  Not happy with the original accepted solution
                                Can do better
                                Editorial solution was eye-opener
                                matter is closed now

[+]Space Complexity          : O(N)
[+]Time Complexity           : O(N)
[+]Level                     : MEDIUM
[+]Tread Speed               :
[+]LINK                      : https://www.interviewbit.com/problems/nearest-smaller-element
[+] Supplement Sources       : N/A

'''

#Accepted
def twoSum_obsolete(lis, target):
    ans, hashmap, length = [], {}, len(lis)

    for index in range(length):
        currentValue = lis[index]
        if currentValue not in hashmap:
            hashmap[lis[index]] = [index]
        else:
            hashmap[lis[index]].append(index)

    for index in range(length):
        currentValue, remainingValue = lis[index], target - lis[index]
        if remainingValue in hashmap:
            index1, index2 = index+1, hashmap[remainingValue][0]+1
            if index2 > index1:
                if ans:
                    if index2 < ans[1]:
                        ans = [index1, index2]
                    elif index2 == ans[1] and index1 < ans[0]:
                        ans = [index1, index2]
                else:
                    ans = [index1, index2]
            elif currentValue == remainingValue:
                indexLis = hashmap[remainingValue]
                if len(indexLis) > 1:
                    if not ans or index2 < ans[1] or index2==ans[1] and index1 < ans[0]:
                        index2 = indexLis[1]+1
                        ans = [index1, index2]
    return ans

# Editorial Inspired
def twoSum(lis, target):
    hashmap = {}
    for index, value in enumerate(lis):
        remainingValue = target - value
        if remainingValue in hashmap:
            return [hashmap[remainingValue]+1, index+1]
        elif value not in  hashmap:
            hashmap[value] = index
    return []

if __name__ == '__main__':
    test_cases = [
        [[2, 7, 11, 15], 9],
        [[1,2,3,2,4], 4],
        [[ 4, 7, -4, 2, 2, 2, 3, -5, -3, 9, -4, 9, -7, 7, -1, 9, 9, 4, 1, -4, -2, 3, -3, -5, 4, -7, 7, 9, -4, 4, -8 ], -3],
        [[1, 1, 1],2],
       [ [1,2,1,2,1],3],
        [[ 2, 5, 0, -6, 7, -4, 0, 4, 3, 0, -2, 0, 9, -3, -9, -3, 9, 3, 2, -10, -8, -3, -10, -5, 2, -8, 4, 5, 6, 7, -10, 4, -3, -10, 5, 4, 1, 5, 5, -3, -1, -8, -3, -6, -7, -8, -8, -7, 0, -2, 7, 7, 10, -7, -7, 10, -4, 0, 0, -6, -5, -5, 0, 8, 4, 1, 4, -1, -10, -4, -6, 10, -2, 9, -6, -3, -4, -1, 10, -9, -5, 10, -5, 8, 3], 0],
        [[10, -3, 5, -7, -4, 5, 6, -7, 8, -5, 8, 0, 8, -5, -10, -1, 1, -6, 4, -1, -2, -2, 10, -2, -4, -7, 5, 1, 7, -10, 0, 5, 8, 6, -8, 8, -8, -8, 3, -9, -10, -5, -5, -10, 10, -4, 8, 0, -6, -2, 3, 7, -5, 5, 1, -7, 0, -5, 1, -3, 10, -4, -3, 3, 3, 5, 1, -2, -6, 3, -4, 10, -10, -3, -8, 2, -2, -3, 0, 10, -6, -8, -10, 6, 7, 0, 3, 9, -10, -7, 8, -7, -7],-2]
    ]
    for test_case in range(len(test_cases)):
        test_case = test_cases[test_case]
        print("input: "+str(test_case)+"\n\tOUTPUT: "+str(twoSum(test_case[0], test_case[1])))
