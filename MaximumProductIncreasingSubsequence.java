/*
 Maximum product of an increasing subsequence
Given an array of numbers, find the maximum product formed by multiplying numbers of an increasing subsequence of that array.

Note: A single number is supposed to be an increasing subsequence of size 1.

Examples:

Input : arr[] = { 3, 100, 4, 5, 150, 6 }
Output : 45000
Maximum product is 45000 formed by the 
increasing subsequence 3, 100, 150. Note
that the longest increasing subsequence 
is different {3, 4, 5, 6}

Input : arr[] = { 10, 22, 9, 33, 21, 50, 41, 60 }
Output : 21780000
Maximum product is 21780000 formed by the 
increasing subsequence 10, 22, 33, 50, 60.

LINK: 
 */
package go;

public class MaximumProductIncreasingSubsequence {

	public static int maximumProductIncreasingSubsequence(int[] array) {
		int length = array.length;
		int maxLength = 0;

		// copying the main array into the aux array
		int[] aux = new int[length];
		for (int i = 0; i < length; i++) {
			aux[i] = array[i];
		}

	
		for (int i = 1; i < length; i++) {
			int localMax = 0;
			for (int j = 0; j < i; j++) {
				if (array[j] < array[i]) {
					localMax = Math.max(localMax, aux[j]);
				}
			}
			aux[i] *= localMax;
			maxLength = Math.max(maxLength, aux[i]);
			
		}
		return maxLength;
	}

	public static void main(String args[]) {

		int[] array = new int[] { 10, 22, 9, 33, 21, 50, 41, 60 };
		System.out.println(maximumProductIncreasingSubsequence(array));

	}
}