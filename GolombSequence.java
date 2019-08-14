/*
 Golomb sequence
In mathematics, the Golomb sequence is a non-decreasing integer sequence where n-th term is equal to number of times n appears in the sequence.

The first few values are
1, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5, ……

Explanation of few terms:
Third term is 2, note that three appears 2 times.
Second term is 2, note that two appears 2 times.
Fourth term is 3, note that four appears 3 times.

Given a positive integer n. The task is to find the first n terms of Golomb sequence.

Examples :

Input : n = 4
Output : 1 2 2 3

Input : n = 6
Output : 1 2 2 3 3 4

LINK: https://www.geeksforgeeks.org/golomb-sequence
 */
package go;

public class GolombSequence {

	public static int[] golombSequence(int terminal) {

		int[] array = new int[terminal];
		array[0] = 1;
		int last = 1;
		int count = 1;
		for (int i = 1; i < terminal; i++) {

			if (count == 1) {

				last += 1;
				array[i] = last;
				count = array[last-1];
			} else {
				array[i] = last;
				count -= 1;
			}
	}
		return array;
	}

	public static void main(String args[]) {

		int terminal = 50;
		int[] dp = golombSequence(terminal);
		for (int a : dp) {
			System.out.print(a+" ");
		}
	}
}
