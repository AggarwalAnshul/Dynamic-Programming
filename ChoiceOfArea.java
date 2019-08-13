/*
 LINK: https://www.geeksforgeeks.org/game-theory-choice-area/
 
 Choice of Area
Consider a game, in which you have two types of powers, A and B and there are 3 types of Areas X, Y and Z. Every second you have to switch between these areas, each area has specific properties by which your power A and power B increase or decrease. We need to keep choosing areas in such a way that our survival time is maximized. Survival time ends when any of the powers, A or B reaches less than 0.
Examples:

Initial value of Power A = 20        
Initial value of Power B = 8

Area X (3, 2) : If you step into Area X, 
                A increases by 3, 
                B increases by 2

Area Y (-5, -10) : If you step into Area Y, 
                   A decreases by 5, 
                   B decreases by 10

Area Z (-20, 5) : If you step into Area Z, 
                  A decreases by 20, 
                  B increases by 5

It is possible to choose any area in our first step.
We can survive at max 5 unit of time by following 
these choice of areas :
X -> Z -> X -> Y -> X

 */
package go;

public class ChoiceOfArea {
	
	static int findPower(int factor, int power) {
		return power+factor;
	}
	public static int solve(int time, int powerA, int powerB, int[] A, int[] B, int[] C, int last) {
		//System.out.println("PowerA: "+powerA+" PowerB: "+powerB);
		if(powerA < 1 || powerB < 1)
			return time;
		if(last==0) {
		int a = solve(time+1, findPower(A[0], powerA), findPower(A[1], powerB), A, B, C, 1);
		int b = solve(time+1, findPower(B[0], powerA), findPower(B[1], powerB), A, B, C, 2);
		int c = solve(time+1, findPower(C[0], powerA), findPower(C[1], powerB), A, B, C, 3);
		return Math.max(Math.max(a, b),  c);
		}
		else if(last==1) {
			int b = solve(time+1, findPower(B[0], powerA), findPower(B[1], powerB), A, B, C, 2);
		int c = solve(time+1, findPower(C[0], powerA), findPower(C[1], powerB), A, B, C, 3);
		return Math.max(b, c);	
	}
		else if(last==2) {
			int a = solve(time+1, findPower(A[0], powerA), findPower(A[1], powerB), A, B, C, 1);
			int c = solve(time+1, findPower(C[0], powerA), findPower(C[1], powerB), A, B, C, 3);
			return Math.max(a,  c);
		}
		else {
			int a = solve(time+1, findPower(A[0], powerA), findPower(A[1], powerB), A, B, C, 1);
			int b = solve(time+1, findPower(B[0], powerA), findPower(B[1], powerB), A, B, C, 2);
			return Math.max(a,  b);
		}
	}
	public static void main(String args[]) {
		
		 int[] A = new int[] {3,2};
		 int[] B = new int[] {-5, -10};
		 int[] C = new int[] {-20, 5};
		 int powerA = 20;
		 int powerB = 8;
		 System.out.println(solve(0, powerA, powerB, A, B, C, 0)-1);
	}
}
