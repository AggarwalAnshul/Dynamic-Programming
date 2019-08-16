/*
 * Count even length binary sequences with same sum of first and second half bits
Given a number n, find count of all binary sequences of length 2n such that sum of first n bits is same as sum of last n bits.
Examples:

Input:  n = 1
Output: 2
There are 2 sequences of length 2*n, the
sequences are 00 and 11

Input:  n = 2
Output: 6
There are 6 sequences of length 2*n, the
sequences are 0101, 0110, 1010, 1001, 0000
and 1111

LINK: https://www.geeksforgeeks.org/count-even-length-binary-sequences-with-same-sum-of-first-and-second-half-bits/
 */
package go;

public class EvenLengthBinarySequence {

	public static int evenLengthBinarySequenceSolution(int length, int diff) {
		
		//BASE CASE
		if(length==2) {
			if(diff==1 || diff==-1)
				return 1;
			return (diff==0 ? 2 : 0); //return 2, if diff is 0, Otehrwise return 0
		}
		
		return 2*evenLengthBinarySequenceSolution(length-2, diff) +
				evenLengthBinarySequenceSolution(length-2, diff+1) +
				evenLengthBinarySequenceSolution(length-2, diff-1);
		
	}
	public static void main(String args[]) {
		
		int stringLength = 2;
		System.out.println( evenLengthBinarySequenceSolution( 2*stringLength, 0 ) );
	}
	
}
