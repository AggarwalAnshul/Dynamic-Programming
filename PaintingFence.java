/*
 * 
 Painting Fence Algorithm
Given a fence with n posts and k colors, find out the number of ways of painting the fence such that at most 2 adjacent posts have the same color. Since answer can be large return it modulo 10^9 + 7.

Examples:

Input : n = 2 k = 4
Output : 16
We have 4 colors and 2 posts.
Ways when both posts have same color : 4 
Ways when both posts have diff color :
4*(choices for 1st post) * 3(choices for 
2nd post) = 12

Input : n = 3 k = 2
Output : 6

LINK: https://www.geeksforgeeks.org/Painting-Fence-Algorithm

 */
package go;

public class PaintingFence {

	public static int paintingFenceSolution(int colors, int posts) {
		
		int same = 0;
		int diff = colors;
		int total = same + diff; 
		
		for(int i=1; i<posts; i++) {
			same = diff;
			diff = total*(colors-1);
			total = same + diff;
		}
		return total;
	}
	public static void main(String args[]) {
		int colors; 
		int posts;
		System.out.println(paintingFenceSolution(2, 3));
	}
}
