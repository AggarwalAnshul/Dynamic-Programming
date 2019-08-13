package go;

import java.util.Arrays;

public class TilingProblem {
	/*Revisiting*/
	public static int tilingProblem(int area) {
		if(area==0)
			return 1;
		if(area<0)
			return 0;
		return (tilingProblem(area-2)+tilingProblem(area-4));
	}
	public static int solve(int tile, int[] sol) {
		if(tile==0)
			return 1;
		if(tile<0)
			return 0;
		if(sol[tile]!=-2)
			return sol[tile];
		
		sol[tile] =  solve(tile-2, sol)+solve(tile-4, sol);
		return sol[tile];
	}
	public static void main(String args[]) {
		/*int tile = 4;
		int sol[] = new int[tile+1];
		Arrays.fill(sol, -2);
		System.out.println(solve(tile, sol));
		*/
		int n = 4;
		System.out.println(tilingProblem(2*n));
	}
}
