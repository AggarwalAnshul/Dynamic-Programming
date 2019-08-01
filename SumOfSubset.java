package go;

import java.util.Arrays;

public class SumOfSubset {

	/*Streamlined DP*/
	public static Boolean solveDP(int sum, int[] set) {
		
		Boolean[][] matrix = new Boolean[sum+1][set.length+1];
		for(int j=0; j<set.length+1; j++) {
			matrix[0][j] = Boolean.TRUE; 
		}
		for(int i=1; i<sum+1; i++) {
			matrix[i][0] = Boolean.FALSE;
		}
		//filling in the matrix
		for(int sumIndex=1; sumIndex<=sum; sumIndex++) {
			for(int j=1; j<=set.length; j++) {
				//System.out.println("Accessing sum: "+sum+" i: "+sumIndex+" j: "+j);
				if(sumIndex < set[j-1]) {
					matrix[sumIndex][j] = matrix[sumIndex][j-1];
				}
				else {
					matrix[sumIndex][j] = ( matrix[ sumIndex-set[j-1] ][j-1] || matrix[sumIndex][j-1]);
				}
			}
		}
		
		//Printing the matrix
		System.out.print("\t0\t");
		for(int e : set)
			System.out.print(e+" \t");
		for(int i=0; i<sum+1; i++) {
			System.out.println();
			System.out.print(i+"\t");
			for(int j=0; j<set.length+1; j++) {
				System.out.print(matrix[i][j]+"\t");
			}
		}
		return matrix[sum][set.length];
	}
	
	/*Naive Approach*/
	public static Boolean solve(int sum, int[] set) {
		System.out.println("seraching for sum: "+sum+ " in array: ");
		for(int e : set)
			System.out.print("\t"+e);
		System.out.println();
		if(sum==0)
			return Boolean.TRUE;
		if(sum<0 || set.length==0)
			return Boolean.FALSE;
		int[] sub = Arrays.copyOfRange(set, 0, (set.length-1));
	//	System.out.println("Accessing element with sub length: "+sub.length);
		return (solve((sum-set[set.length-1]), sub) || solve(sum, sub));
	}
	public static void main(String args[]) {
		 int[] set = new int[] {3, 34, 12, 5, 2};
		 int sum = 9;
		 System.out.println("\nAnswer >>"+solveDP(sum, set));
	}
}
