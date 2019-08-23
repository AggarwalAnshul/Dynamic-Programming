"""
Maximize the sum of selected numbers from an array to make it empty
Given an array of N numbers, we need to maximize the sum of selected numbers. At each step you need to select a number Ai, delete one occurrence of Ai-1 (if exists), Ai+1 (if exists) and Ai each from the array. Repeat these steps until the array gets empty. The problem is to maximize the sum of selected numbers.

Note: We have to delete Ai+1 and Ai-1 elements if they are present in the array and not Ai+1 and Ai-1.

Examples:

Input : a[] = {1, 2, 3} 
Output : 4
Explanation: At first step we select 1, so 1 and 
2 are deleted from the sequence leaving us with 3. 
Then we select 3 from the sequence and delete it.
So the sum of selected numbers is 1+3 = 4. 


Input : a[] =  {1, 2, 2, 2, 3, 4}
Output : 10 
Explanation : Select one of the 2's from the array, so 
2, 2-1, 2+1 will be deleted and we are left with {2, 2, 4}, 
since 1 and 3 are deleted. Select 2 in next two steps, 
and then select 4 in the last step.
We get a sum of 2+2+2+4=10 which is the maximum possible.

Temporal marker: 10:38:44 Hours | Aug23, Friday
LINK: geeksforgeeks.org/maximum-path-sum-position-jumps-divisibility-condition/
"""

def findMaximumPathSumPositionJumpsDivisibilityCondition(lis, index, sumCount):
    if(len(lis)==0):
        return sumCount
    if(index>=len(lis)):
        return sumCount
    sumCountBranchLeft = sumCount
    #Branch Left | Including the element at index
    element = lis[index]
    if(lis[0:index].index(element-1):
        sumCountBranchLeft = sumCount + element -1
    if(lis[index+1]==element+1):
        sumCountBranchLeft = sumCount + element + 1
        index += 1
    return max(MaximumPathSumPositionJumpsDivisibilityCondition(lis[:lis.index(element)]+lis[lis.index(element)+1:], index+1, sumCountBranchLeft),
               MaximumPathSumPositionJumpsDivisibilityCondition(lis, index+1, sumCount)
        
    
    
