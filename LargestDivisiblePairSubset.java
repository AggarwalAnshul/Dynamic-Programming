/*
 Largest divisible pairs subset
Given an array of n distinct elements, find length of the largest subset such that every pair in the subset is such that the larger element of the pair is divisible by smaller element.

Examples:

Input : arr[] = {10, 5, 3, 15, 20} 
Output : 3 
Explanation: The largest subset is 10, 5, 20.
10 is divisible by 5, and 20 is divisible by 10.

Input : arr[] = {18, 1, 3, 6, 13, 17} 
Output : 4
Explanation: The largest subset is 18, 1, 3, 6,
In the subsequence, 3 is divisible by 1, 
6 by 3 and 18 by 6.

LINK: https://www.geeksforgeeks.org/largest-divisible-pairs-subset/
 */

package go;

import java.util.Arrays;
import java.util.Scanner;

public class LargestDivisiblePairSubset {
	
	public static int largestDivisiblePairSubset(int set[]) {
	
		int len = set.length;
		int[] dp = new int[len];
		int gmax = 0;
		Arrays.sort(set);
		
		for(int i=len-1; i>=0; i--) {
			int lmax = 0;
			for(int j=len-1; j>i; j--) {
				if(set[j]%set[i]==0) {
					lmax = Math.max(lmax,  dp[j]);
				}
			}
			dp[i] = lmax+1;
			gmax = Math.max(gmax, dp[i]);
		}
		return gmax;
	}
	public static void main(String args[]) {
		
		Scanner sc = new Scanner(System.in);
		int cases = sc.nextInt();
		for(int i=0; i<cases; i++) {
			int len = sc.nextInt();
			int[] set = new int[len];
			for(int j=0; j<len; j++) {
				set[j] = sc.nextInt();
			}
			System.out.println(largestDivisiblePairSubset(set));
		} 
		/*
		//int[] set = new int[] {1,4,6,12,5,10};
		//int[] set = new int[]{10,5,3,15,20};
		//int[] set = new int[] {18, 1, 3, 6, 13, 17};
		System.out.println(largestDivisiblePairSubset(set));
		*/
	}
}
