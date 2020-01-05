#M.75

"""
Count Possible Decodings of a given Digit Sequence
Let 1 represent ‘A’, 2 represents ‘B’, etc. Given a digit sequence, count the
number of possible decodings of the given digit sequence.
Examples:

Input:  digits[] = "121"
Output: 3
// The possible decodings are "ABA", "AU", "LA"

Input: digits[] = "1234"
Output: 3
// The possible decodings are "ABCD", "LCD", "AWD"
An empty digit sequence is considered to have one decoding. It may be assumed that
the input contains valid digits from 0 to 9 and there are no leading 0’s, no extra
 trailing 0’s and no two or more consecutive 0’s.


[+]Temporal marker            :  Wed, 19:28 | Sep 25, 19
[+]Temporal marker untethered :  Wed, 19:28 | Sep 25, 19
[+]Comments                   : *
                                *
                                *
[+]Level                      :
[+]Tread speed                :
[+]LINK                       : https://www.geeksforgeeks.org/count-possible-decodings-given-digit-sequence
"""
def findSolution(string):
    length = len(string)
    dp = [0]*length
    dp[0] = 1

    for i in range(1, length):
        #print("Checking for: "+string[i])
        if(dp[i-1]!=0):
            if(string[i]!='0'):
                dp[i] = dp[i-1]
                if( int(string[i-1:i+1]) < 27 and string[i-1]!='0'):
                    dp[i] += 1
            else:
                if( int(string[i-1:i+1]) < 27):
                    dp[i] = dp[i-2]

    #print(dp)
    return dp[length-1]


if __name__ == "__main__":
    string = "121"
    string = "1234"
    string = "6592012"
    string = "1123"
    print(findSolution(string))
