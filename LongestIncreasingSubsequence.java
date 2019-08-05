package go;

import java.util.Scanner;

public class LongestIncreasingSubsequence {
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
		
		/*
		int[] set = new int[] {0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15};
		System.out.println(longestIncreasingSubsequence(set));
		*/
		Scanner sc = new Scanner(System.in);
		int cases = sc.nextInt();
		for(int i=0; i<cases; i++) {
			int len = sc.nextInt();
			int[] set = new int[len];
			for(int j=0; j<len; j++) {
				set[j] = sc.nextInt();
			}
			System.out.println(longestIncreasingSubsequence(set));
		}
	}
}
