'''

[+]Temporal marker           : 14:13 Hours | Tuesday 31, 2020
[+]Temporal marker untethered: 14:13 Hours | Tuesday 31, 2020
[+]Comments                  :  Laid off the original Day
                                Today solved in about 30 minutes
                                Devised solution worked better than the expectations
                                devised solution at par with the editorial
                                This matter is officially closed now
[+]Space Complexity          : O(N)
[+]Time Complexity           : O(N)
[+]Level                     : MEDIUM
[+]Tread Speed               : Relaxed
[+]LINK                      : https://www.interviewbit.com/problems/nearest-smaller-element
[+] Supplement Sources       : N/A

'''

# ACCEPTED 
# Time Complexity: O(N) | Space-Complexity: O(N)
# Very Happy with the solution
def lszero(lis):
    hashmap = {}
    length, ans, sum = len(lis), [], 0

    for index in range(length):
        sum += lis[index]
        if sum not in hashmap:
            hashmap[sum] = index
        if sum == 0 or sum in hashmap:
            start_index, end_index = 0 if sum == 0 else hashmap[sum]+1, index+1
            if not ans or ans and ans[1]-ans[0] < end_index - start_index:
                ans = [start_index, end_index]

    return lis[ans[0] : ans[1]] if ans else []

if __name__ == "__main__":
    test_cases = [
        [1,2,-2,4,-4],
        [1,2,-2,4,-4,1,3,-3],
        [1,2,3,4],
        [1,2,-2,3,4,-4,7,5,-5],
        [5, 1, 2, -3, 5],
        [1,2,-3,4,5]
    ]
    for index in range(len(test_cases)):
        test_case = test_cases[index]
        print("input: "+str(test_case)+ "\n\toutput: "+str(lszero(test_case)))