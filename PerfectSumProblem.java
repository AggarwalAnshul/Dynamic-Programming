/*
 Perfect Sum Problem (Print all subsets with given sum)
Given an array of integers and a sum, the task is to print all subsets of given array with sum equal to given sum.

Examples:

Input : arr[] = {2, 3, 5, 6, 8, 10}
        sum = 10
Output : 5 2 3
         2 8
         10

Input : arr[] = {1, 2, 3, 4, 5}
        sum = 10
Output : 4 3 2 1 
         5 3 2 
         5 4 1 
Asked in Tesco

LINK: https://www.geeksforgeeks.org/perfect-sum-problem-print-subsets-given-sum/
 */
package go;

import java.util.ArrayList;
import java.util.*;

public class PerfectSumProblem {

	public static Stack<Integer> stack = new Stack<Integer>();
	
	//a utility function that prints the stack
	static void printStack(Stack<Integer> stack) {
		for(int e : stack)
			System.out.print(e+ " ");
		System.out.println();
	}
	
	public static void perfectSumProblem(int sum, int index, int[] set) {
		
		if(index<=set.length) {
			if(sum==0) {
				printStack(stack);
			}
			else if(sum>0 && index<set.length) {
				if(set[index]<=sum) {
					stack.push(set[index]);
					perfectSumProblem(sum-set[index], index+1, set);
					stack.pop();
					perfectSumProblem(sum, index+1, set);
				}
			}
		}
	}
	
	
	/* DEBUG VERSION */
	
	public static void perfectSumProblemDEBUG(int sum, int index, int[] set) {

		if(index<=set.length) {
		//System.out.println("In func index: "+index+" ele: "+set[index]+" sum: "+(10-sum)+"|"+sum);
		/*for(int e : store)
			System.out.print(e+" ");
		System.out.println();
*/
		
		if(sum==0) {
			System.out.print("");
			for(int e : stack)
				System.out.print(e+" ");
			System.out.println();
			//System.out.println("Popping: "+store.peek());
			//store.pop();
		}
		else if(sum>0 && index<set.length) {
			if(set[index]<=sum) {
				stack.push(set[index]);
				perfectSumProblemDEBUG(sum-set[index], index+1, set);
			//	System.out.println("Popping: "+store.peek());
				stack.pop();
				//System.out.println("Calling the right branch");
				perfectSumProblemDEBUG(sum, index+1, set);
			}
		}
		
		//System.out.println("Exiting function with index: "+index+" ele: "+set[index]+ " sum: "+sum);
		}
	}
	
	public static void main(String args[]) {
	/*
		Scanner sc = new Scanner(System.in);
		int cases = sc.nextInt();
		for(int i=0; i<cases; i++) {
			int len = sc.nextInt();
			int[] set = new int[len];
			for(int j=0; j<len; j++) {
				set[j] = sc.nextInt();
			}
	*/
		
	int sum = 10;
	int[] set = new int[] {2, 3, 5, 6, 8, 10};
	perfectSumProblem(sum, 0, set);
	
		} 
	}

