package go;
import java.util.Scanner;

public class IncreasingSubsetSum {
	
	//obsolete my creation
	public static int solve(int[] set) {
		
		int len = set.length;
		int[][] matrix = new int[len+1][len+1];
		
		//matrix initialization
		for(int i=len-1; i>0; i--) {
			if(set[i-1]>set[len-1]) {
				matrix[i][len] = set[i-1];
			}else {
				matrix[i][len] = set[i-1]+set[len-1];
			}
		}
		
		//matrix filling
		for(int i=len-2; i>0; i--) {
			for(int j=len-1; j>i; j--) {
				matrix[i][j] = Math.max(matrix[i][j+1], Math.max(matrix[j][j+1], (set[i-1]<set[j-1] ? set[i-1]+matrix[j][j+1] : matrix[j][j+1])));
			}
		}
		//filling in the final row
		for(int j=len-1; j>0; j--) {
			matrix[0][j] = Math.max(matrix[0 ][j+1], matrix[j][j+1]);
		}
		return matrix[0][1];
	}
	
	//streamlined FTJ
	public static int solveS(int[] set) {
		
		int len = set.length;
		int[] dp = new int[len];
		for(int i=0; i<len; i++) {
			dp[i] = set[i];
		}
		
		int max = set[0];
		for(int i=1; i<len; i++) {
			for(int j=0; j<i; j++) {
				if(set[i] > set[j] && dp[i]<dp[j]+set[i]) {
					dp[i] = dp[j]+set[i];
					max = Math.max(max, dp[i]);
					System.out.print("i: "+i+" j: "+j+" \t");
					for(int e : dp) {
						System.out.print(e+"\t");}
						System.out.print(" max: "+max+"\n");
					
				}
			}
		}
		return max;
		
	}
	public static void main(String args[]) {
		int[] set = new int[] {1,101,2,3,100,4,5};
		//int[] set = new int[] {10, 5, 4, 3};
	
		
		//input the set
		/*
		Scanner sc = new Scanner(System.in);
		int cases = sc.nextInt();
		
		
		for(int i=0; i<cases; i++) {
			int len = sc.nextInt();
			int[] set = new int[len];
			for(int j=0; j<len; i++) {
				set[j] = sc.nextInt();
			}
			System.out.println(solveS(set));
		}*/
		System.out.println(solveS(set));
	}
		
}
