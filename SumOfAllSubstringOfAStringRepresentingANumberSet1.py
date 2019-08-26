"""
Sum of all substrings of a string representing a number | Set 1
Given a integer represented as a string, we need to get the sum
of all possible substrings of this string.

>>>>>>>>>>>>>>>>> SET1 <<<<<<<<<<<<<<<<<<<<<<

Examples:

Input  : num = “1234”
Output : 1670
Sum = 1 + 2 + 3 + 4 + 12 + 23 +
       34 + 123 + 234 + 1234 
    = 1670

Input  : num = “421”
Output : 491
Sum = 4 + 2 + 1 + 42 + 21 + 421 = 491

[+]Temporal Marker            : 11:51 Hours | Aug26, Monday
[+]Temporal marker Untethered : 12:28 Hours | Aug26, Monday
[+]Tread speed                : Relaxed
[+]Comments                   : Brute force approach derived in record time(1A)
                                Brainstorming requried for Optimized approach
                                S Version approach derived in less than 18mins
                                implementation of S Version in acceptable time
[+]LINK                       : geeksforgeeks.org/sum-of-all-substrings-of-a-string-representing-a-number/
"""

#Streamlined algorithm running on T:O(N) & S:O(1)
def findSumOfAllSubstringsS(num):
    length = len(num)
    last = 0
    sumCount = 0
    
    for x in range(length, 0, -1):
        last += pow(10,length-x)
        sumCount += last*int(num[x-1])*x
        #print("ele: "+str(ele)+"last: "+str(last)+" x: "+str(x))

    return(sumCount)

#Brute force algorithm running on T:O(N*N) and S:O(1)
def findSumOfAllSubstrings(num):
    length = len(num)
    sumCount = 0
    for x in range(0, length):
        last = 0
        for y in range(x, length):
            last = last*10 + (int(num[y]))
            sumCount += last
    return sumCount

num = "16"
#num = "6759"
#num = "421"
#num = "1234"

print(findSumOfAllSubstringsS(num))
print(findSumOfAllSubstrings(num))


