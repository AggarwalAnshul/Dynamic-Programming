/*
 Maximum Sum Increasing Subsequence | DP-14 |
Given an array of n positive integers. Write a program to find the sum of maximum sum subsequence of the given array such that the integers in the subsequence are sorted in increasing order. For example, if input is {1, 101, 2, 3, 100, 4, 5}, then output should be 106 (1 + 2 + 3 + 100), if the input array is {3, 4, 5, 10}, then output should be 22 (3 + 4 + 5 + 10) and if the input array is {10, 5, 4, 3}, then output should be 10
 
LINK: https://www.geeksforgeeks.org/maximum-sum-increasing-subsequence-dp-14/
 */
package go;

public class MaximumSumIncreasingSubseqeunce {
	
	public static int maximumSumIncreasingSubsequence(int[] array) {
		int length = array.length;
		int maxLength = 0;
		
		//copying the main array into the aux array
		int[] aux = new int[length];
		for(int i=0; i<length; i++) {
			aux[i] = array[i];
		}
		
		for(int i=0; i<length; i++) {
			int localMax = 0;
			for(int j=0; j<i; j++) {
				if(array[j] < array[i]) {
					localMax = Math.max(localMax, aux[j]);
				}
			}
			aux[i] += localMax;
			maxLength = Math.max(maxLength, aux[i]);
		}
		return maxLength;
	}
	public static void main(String args[]) {
		
		int[] array = new int[]{1, 101, 2, 3, 100, 4, 5};
		System.out.println( maximumSumIncreasingSubsequence(array) );
	}
	
}
