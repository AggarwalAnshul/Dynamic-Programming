package go;

/*
 Given a set of non-negative integers, and a value sum, determine if there is a subset of the given set with sum equal to given sum.
Example:

Input:  set[] = {3, 34, 4, 12, 5, 2}, sum = 9
Output:  True  //There is a subset (4, 5) with sum 9.
 
 LINK:https://www.geeksforgeeks.org/subset-sum-problem-dp-25/
 */
public class SubsetSum {
	
	public static Boolean solveS(int[] set, int sum) {
		
		int len = set.length;
		Boolean[][] dp = new Boolean[sum+1][len+1];
		
		//initializing the matrix
		for(int i=1; i<=sum; i++) {
			dp[i][0] = Boolean.FALSE;
		}
		for(int j=0; j<=len; j++) {
			dp[0][j] = Boolean.TRUE;
		}
		
		//solving the matrix
		for(int i=1; i<=sum; i++) {
			for(int j=1; j<=len; j++) {
				
				dp[i][j] = dp[i][j-1];
				if(i>=set[j-1]) {
					dp[i][j] = dp[ i - set[j-1] ][j-1] || dp[i][j];
				}
			}
		}
		return dp[sum][len];
	}
	
	public static Boolean solve(int[] set, int sum, int index) {
		if(sum==0)
			return Boolean.TRUE;
		if(set.length!=0 & index<set.length && sum>0) {
			return solve(set, sum-set[index], index+1)||solve(set, sum, index+1);
		}
		return Boolean.FALSE;
	}
	public static void main(String args[]) {
		int[] set = new int[] {3,34,4,12,5,2};
		int sum = 9;
		int[][] dp = new int[sum+1][set.length+1];
		System.out.println(solveS(set, sum));
		//System.out.println( (solve(set, sum, 0)==Boolean.TRUE ? "True" : "False"));
	}
}
