"""
#M.16

Word Break Problem | DP-32
Given an input string and a dictionary of words, find out if the input string can be segmented into a space-separated sequence of dictionary words. See following examples for more details.
This is a famous Google interview question, also being asked by many other companies now a days.

Consider the following dictionary 
{ i, like, sam, sung, samsung, mobile, ice, 
  cream, icecream, man, go, mango}

Input:  ilike
Output: Yes 
The string can be segmented as "i like".

Input:  ilikesamsung
Output: Yes
The string can be segmented as "i like samsung" 
or "i like sam sung".

[+]Temporal marker            : 19:05 Hours,                  | Sunday, Sept08, 19
[+]Temporal marker untethered : 19:25 Hours, 20:32(Final D*)  | Sunday, Sept08, 19
[+]Comments                   : Already had the apporach in my mind
                                Implementation took 15 mins max
                                All test cases passed
                                Don't feel a dynamic solution is requried
                                GFG Shows a DP Solution, However my solution has the same
                                complexity as theirs, so i'm not moving into unchartered territory unnecessarily
                                Consider the matter closed
                                Now realized branch solution is needed
                                DP Added now 
[+]Tread speed                : Relaxed
[+]Level                      : Easy
[+]LINK                       : https://www.geeksforgeeks.org/word-break-problem-dp-32/
"""

#A function that returns a new list by adding a new word to an existing list
def copy(one, word):
    new = []
    for x in one:
        new.append(x)
    new.append(word)
    return new



#T-Complexity: O(word*dic) | S-Complexity: O(n)
#Obsolete, later found out, only gives partial results
"""def findSolution(word, start, end, dic):
    if(start==end and start==len(word)):
        return True  
    if(end > (len(word)-1)):
        return False 
    substring = word[start : end+1] 
    for sub in dic:             if(substring==sub):
            print(sub)
            return findSolution(word, end+1, end+1, dic)
                                
    return findSolution(word, start, end+1, dic)""" 


def findSolutionUDP(word, start, end, dic, seq, dp):
    if(start==end and start==len(word)):
        print(seq)
        return 1  #The case of success
    if(end > (len(word)-1)):
        return 0 #The case of failure
    substring = word[start : end+1] #The substring to work on
    if(dp[start][end] == -1):
        for sub in dic:     #looking if this substring is in dic?
            if(substring==sub):
                branchOne = findSolutionUDP(word, start, end+1, dic, seq, dp)
                branchTwo = findSolutionUDP(word, end+1, end+1, dic, copy(seq, sub), dp)
                dp[start][end] = (branchOne or branchTwo)
                return dp[start][end]
        dp[start][end] = findSolutionUDP(word, start, end+1, dic, seq, dp)
        return dp[start][end]
    else:
        return dp[start][end]
    
def findSolutionDP(word, dic):
    length = len(word)
    dp = [[0]*length for x in range(length)]

    #dp[i][j] word contain if this is a part of sequence or not in dic

def findSolutionU(word, start, end, dic, seq):
    if(start==end and start==len(word)):
        print(seq)
        return True  #The case of success
    if(end > (len(word)-1)):
        return False #The case of failure
    substring = word[start : end+1] #The substring to work on
    for sub in dic:     #looking if this substring is in dic?
        if(substring==sub):
            branchOne = findSolutionU(word, start, end+1, dic, seq)
            branchTwo = findSolutionU(word, end+1, end+1, dic, copy(seq, sub))
            return (branchOne or branchTwo)
                
    return findSolutionU(word, start, end+1, dic, seq) #adding more char to substring

if __name__ == "__main__":
    #lis = [sum, dices, faces]
    dic = ["mobile","samsung","sam","sung", "man","mango","icecream","and", 
        	"go","i","like","ice","cream"]
    word = "ilike"
    word = "ilikesamsung"
    word = "ilikeposamsung"
    word = "iiiiiiii"
    word = ""
    word = "ilikelikeimangoiii"
    word = "samsungandmango"
    word = "samsungandmangok"
    word = "ilikesamsungmobile"
    word = "ilikeicecreamandmango"
    length = len(word)
    print(findSolutionU(word, 0, 0, dic,[]))
    dp = [[-1]*length for x in range(length)]
    print("UDP")
    print(findSolutionUDP(word, 0, 0, dic, [], dp))
    #print(findSolution(word, 0, 0, dic))
