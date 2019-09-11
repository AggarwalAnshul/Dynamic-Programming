package go;
import java.util.*;
import java.lang.*;

public class LongestPalindromicSubsequence {
	public static void findLongestPalindromicSubsequence(String words) {
		int length = words.length();
		int[][] array = new int[length+1][length+1];
		for(int i=0; i<=length; i++) {
			for(int j=0; j<=length; j++) {
				//base case initializing guard rails by ZERO
				//System.out.println("i: "+i+" J: "+j);
				if(i==0 || j==0) {
					array[i][j] = 0;
				}//filling in the matrix
				else {
					if(words.charAt(i-1)==words.charAt(length-j)) {
					
						array[i][j] = 1+array[i-1][j-1];
					}
					else {
						array[i][j] = Math.max(array[i-1][j], array[i][j-1]);
					}
				
				}
			}
		}
		//printing the answer
		String ans = "";
		int i = length,j = length;
		while(i>0 && j>0) {
			//System.out.println("i: "+i+" j: "+j);
			if(words.charAt(i-1)==words.charAt(length-j)) {
				ans+=words.charAt(i-1);
				i-=1;
				j-=1;
			}
			else {
				if(array[i-1][j]<array[i][j-1]) {
					j-=1;
				}
				else {
					i-=1;
				}
			}
		}
		System.out.println(array[length][length]);
		System.out.println(ans);
		
		//System.out.println("The answer is: "+array[length][length]);
		//printing the matrix
				/*for(int i=0; i<words.length()+1; i++) {
					System.out.println();
					for(int j=0; j<words.length()+1; j++) {
						System.out.print("\t"+array[i][j]);
					}
				}*/
	}
	public static void main(String args[])
	{
		System.out.println("Hello!");
		findLongestPalindromicSubsequence("abacdgfdcaba");
	}
}
