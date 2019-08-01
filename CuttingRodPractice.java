package go;

import java.util.Arrays;
import java.util.Scanner;

public class CuttingRodPractice {
	
	
	public static int f(int num, int x, int y, int z, int index, int[] sol) {
		//System.out.println("Calling fuctino"+num);
		if(num==0)
			return index;
		if(num<0)
			return -1;
		if(sol[num]!=-2) {
			return sol[num];
		}
		int ans = Math.max( f(num-x, x, y, z, index+1, sol), 
				  Math.max(f(num-y,  x, y, z, index+1, sol), f(num-z, x, y, z, index+1, sol)));
		if(ans>=0) {
			sol[num] = ans-index;
		}
		else {
			sol[num] = -1;
		}
		return ans; 
	}
	
	
	public static void main(String args[]) {
		
		Scanner sc = new Scanner(System.in);
		/*int cases = sc.nextInt();
		for(int i=0; i<cases; i++) {
			int length = sc.nextInt();
			int x = sc.nextInt();
			int y = sc.nextInt();
			int z = sc.nextInt();
	
			int[] sol = new int[6];
			Arrays.fill(sol, -2);
			
			System.out.println(f(length, x,y,z,0,sol));
		}*/

		int[] sol = new int[4001];
		Arrays.fill(sol, -2);
		
		System.out.println(f(4, 2, 1, 1, 0, sol));
	}

}
