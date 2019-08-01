package go;

public class CuttingRod {
	
	public static int f(int num, int length,  int[] sol, int[] array) {
		System.out.println("Solving the function for "+num);
		if(num==0) {
			System.out.println("Exitting fucntion f(0) returned 0");
			
			return 0;
			}
		int ans = 0;
		if(sol[num]!=-1)
		{
			System.out.println("sol["+num+"] is: "+sol[num]);
			return sol[num];

		}
		else {
		for(int i=0; i<num; i++) {
			System.out.println("\tChecking function perm for: ["+(i+1)+"] + f("+(num-1-i)+")");
			ans = Math.max(ans,  (array[i]+f(num-1-i, length, sol, array)));
			
			}
		}
		sol[num] = ans;
		System.out.println("Exitting function: "+num+ " returning the max value: "+ans);
		return ans;
	}
	
	public static void main(String args[]) {
		
		int length = 8;
		int[] array = new int[] {3,5,8,9,10,17,17,20};
		int[] sol = new int[length+1];
		
		//initializing the array
		for(int i=0; i<sol.length; i++) {
			sol[i] = -1;
		}
		
		//solving the problem
		System.out.println( f(8, 8, sol, array) );
		
		
	}
}
