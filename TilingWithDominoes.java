/*
  Tiling with Dominoes
Given a 3 x n board, find the number of ways to fill it with 2 x 1 dominoes.

Example 1
Following are all the 3 possible ways to fill up a 3 x 2 board.


Example 2
Here is one possible way of filling a 3 x 8 board. You have to find all the possible ways to do so.

Examples :

Input : 2
Output : 3

Input : 8
Output : 153

Input : 12
Output : 2131

LINK: https://www.geeksforgeeks.org/tiling-with-dominoes
 */
package go;

public class TilingWithDominoes {
	public static int b(int area) {
		if(area<=0)
			return 0;
		if(area==1)
			return 1;
		return a(area-1) + b(area-2);
	}
	public static int a(int area) {
		if(area==0)
			return 1;
		if(area==1)
			return 0;
		return a(area-2) + 2*b(area-1);
	}
	public static int tilingWithDominoes(int area) {
		
		return a(area);
	}
	public static void main(String args[]) {
		int n = 8;
		System.out.println(tilingWithDominoes(n));;
	}
}
