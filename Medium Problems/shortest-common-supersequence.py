"""
#M.37
Shortest Common Supersequence
Given two strings str1 and str2, find the shortest string that has both str1 and str2 as subsequences.
Examples :

Input:   str1 = "geek",  str2 = "eke"
Output: "geeke"

Input:   str1 = "AGGTAB",  str2 = "GXTXAYB"
Output:  "AGXGTXAYB"

[+]Temporal marker            : 12:40  Hours, | Thursday  Sept12, 19
[+]Temporal marker untethered : 14:00  Hours  | Thursday  Sept12, 19
[+]Comments                   : *Problem similar to find no. of palindromic substrings
                                *For the ranges just split the string as per range
                                *Rest of the algo is same
                                *Also the problem requires substring of length=1 also
                                *So jsut added the length of the string in the final ans also
                                *Problem is now solved
                                *Don't let go of that transgression acquired last night[+]Tread speed                : Relaxed
[+]Level                      : Easy
[+]Tread speead               : Paced
[+]LINK                       : https://www.geeksforg eeks.org/shortest-common-supersequence/
"""

def findSolution(one, two, x, y, cost, string):
    #print(string+" cost: "+str(cost))
    #print("x: "+str(x)+ " y: "+str(y)+ " cost: "+str(cost))
    if(x>len(one)-1 and y<len(two)):
        return [cost+len(two)-y, string+two[y:]]
    if(y>=len(two)):
        return [cost, string]
    if(one[x]==two[y]):
        a = findSolution(one, two, x+1, y+1, cost, string+one[x])
        b = findSolution(one, two, x+1, y, cost+1, string+one[x])
        if(a[0]<b[0]):
            return a
        return b
    #print("compromising...>>>")
    a = findSolution(one, two, x+1, y+1, cost+1,string+one[x]+two[y])
    c = findSolution(one, two, x, y+1, cost+1,string+two[y])
    b = findSolution(one, two, x+1, y, cost, string+one[x])
    if(a[0]<b[0] and a[0]<c[0]):
        return a
    elif(c[0]<a[0] and c[0]<b[0]):
        return c
    return b

if __name__ == "__main__":
    lis = ["AGGTAB", "GXTXAYB"]
    lis = ["geek","eke"]
    
    print(findSolution(lis[0], lis[1], 0, 0, 0,""))
    """
    if(len(lis[1])>len(lis[0])):
        lis[0],lis[1] = lis[1],lis[0]
    print(findSolution(lis[0], lis[1], 0, 0, 0,""))
    """
