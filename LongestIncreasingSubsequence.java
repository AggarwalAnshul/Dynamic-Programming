/*
 The Longest Increasing Subsequence (LIS) problem is to find the length of the longest subsequence of a given sequence such that all elements of the subsequence are sorted in increasing order. For example, the length of LIS for {10, 22, 9, 33, 21, 50, 41, 60, 80} is 6 and LIS is {10, 22, 33, 50, 60, 80}.
More Examples:

Input  : arr[] = {3, 10, 2, 1, 20}
Output : Length of LIS = 3
The longest increasing subsequence is 3, 10, 20

Input  : arr[] = {3, 2}
Output : Length of LIS = 1
The longest increasing subsequences are {3} and {2}

Input : arr[] = {50, 3, 10, 7, 40, 80}
Output : Length of LIS = 4
The longest increasing subsequence is {3, 7, 40, 80}
 
 LINK: https://www.geeksforgeeks.org/longest-increasing-subsequence-dp-3/
 */

package go;
import java.util.Scanner;

public class LongestIncreasingSubsequence {
	public static int longestIncreasingSubsequenceRecursive(int[] set, int last, int index, int sum) {
		
		//System.out.println("Accessing index: "+index);
		//System.out.println("Exploring set:[ "+set[index]+" ]   index: "+index);
		//terminal case
		if(set.length<1 || index>set.length-1)
			return sum;
		
		//calculating branching path
		int branch1 = (set[index] > last ? longestIncreasingSubsequenceRecursive(set, set[index], index+1, sum+1) : sum);
		int branch2 = longestIncreasingSubsequenceRecursive(set, last, index+1, sum);
		return Math.max(branch1, branch2);
	}
	public static int longestIncreasingSubsequence(int[] set) {
		int len = set.length;
		int[] dp = new int[len];
		dp[0] = 0;
		
		int max = 0;
		for(int i=1; i<len; i++) {
			for(int j=0; j<i; j++) {
				if(set[j]<set[i]) {
					dp[i] = Math.max(dp[i], dp[j]+1);
					}
			}
			max = Math.max(max, dp[i]);
		}
		
		//Printing the array
		/*for(int e : dp) {
			System.out.print(e);
		}*/
		return max+1;
	}
	public static void main(String args[]) {
		
		
		int[] set = new int[] {0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15};
		//int[] set = new int[] {3,10,2,1,20};
		System.out.println(longestIncreasingSubsequenceRecursive(set, 0, 0, 0));
		//System.out.println(longestIncreasingSubsequence(set));
		/*Scanner sc = new Scanner(System.in);
		int cases = sc.nextInt();
		for(int i=0; i<cases; i++) {
			int len = sc.nextInt();
			int[] set = new int[len];
			for(int j=0; j<len; j++) {
				set[j] = sc.nextInt();
			}
			System.out.println(longestIncreasingSubsequenceRecursive(set, 0, 0, 0));
		}*/
	}
}
