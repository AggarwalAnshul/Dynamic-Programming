#M.75

"""
Bitmasking and Dynamic Programming | Set 1 (Count ways to assign unique cap to every person)
Consider the below problems statement.

There are 100 different types of caps each having a unique id from 1 to 100. Also, there are ‘n’
persons each having a collection of a variable number of caps. One day all of these persons decide
to go in a party wearing a cap but to look unique they decided that none of them will wear the same
type of cap. So, count the total number of arrangements or ways such that none of them is wearing
the same type of cap.

Constraints: 1 <= n <= 10 Example:

The first line contains the value of n, next n lines contain collections
of all the n persons.
Input:
3
5 100 1     // Collection of the first person.
2           // Collection of the second person.
5 100       // Collection of the third person.

Output:
4
Explanation: All valid possible ways are (5, 2, 100),  (100, 2, 5),
            (1, 2, 5) and  (1, 2, 100)
Since, number of ways could be large, so output modulo 1000000007



[+]Temporal marker            :  Sun, 14:24 | Dec 29, 20
[+]Temporal marker untethered :  Sun, 14:24 | Dec 29, 20
[+]Comments                   : *Pretty complex
                                *Had to learn a completely new paradigm, Bitmasking with DP
                                *Still in the development phase
                                *Questions solved within 3 attemps spanned over 3 days, after learning
                                    bitmasking or reading to be more precise.
[+]Level                      : HARD
[+]Tread speed                : Relaxed,paced
[+]LINK                       : https://www.geeksforgeeks.org/bitmasking-and-dynamic-programming-set-1-count-ways-to-assign-unique-cap-to-every-person
"""

def findSolution(cap, mask, persons, dp):
    allmask = (1<<(len(persons)))-1
    #Check if the terminal case has arrived, when all three are wearing some cap
    if(mask==allmask):
        return 1
    if(cap>100):
        return 0

    #if this subproblem is already not solved
    if(dp[cap][mask]==-1):
        when_this_cap_is_included = 0
        #Try for each person who can wear this cap
        for x in range(len(persons)):
            person = persons[x]
            #if this persons has this cap and is not already wearing it
            if( (person&(1<<cap)) and not(mask & (1<<x))):
                when_this_cap_is_included += findSolution(cap+1, mask|(1<<x), persons, dp)

        when_this_cap_is_excluded = findSolution(cap+1, mask, persons, dp)
        dp[cap][mask] = when_this_cap_is_included + when_this_cap_is_excluded
    return dp[cap][mask]

if __name__ == "__main__":
    lis = [[5, 100, 1], [2], [5, 100]]
    rows = 100
    cols = (2**len(lis)) - 1

    #Creating a 2D array for storing results
    dp = [[-1 for x in range(cols+1) ]for y in range(rows+1)]
    print("rows: "+str(len(dp)))
    print("cols: "+str(len(dp[0])))

    #Creating a map, to tell quickly if a person has a said cap or not?
    persons = []
    for sublis in lis:
        person = 0
        for ele in sublis:
            person = person | (1<<ele)
        persons.append(person)
    #print(persons)
    print(findSolution(0, 0, persons, dp))