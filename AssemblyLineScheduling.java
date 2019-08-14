/*
 Assembly Line Scheduling | DP-34
A car factory has two assembly lines, each with n stations. A station is denoted by Si,j where i is either 1 or 2 and indicates the assembly line the station is on, and j indicates the number of the station. The time taken per station is denoted by ai,j. Each station is dedicated to some sort of work like engine fitting, body fitting, painting and so on. So, a car chassis must pass through each of the n stations in order before exiting the factory. The parallel stations of the two assembly lines perform the same task. After it passes through station Si,j, it will continue to station Si,j+1 unless it decides to transfer to the other line. Continuing on the same line incurs no extra cost, but transferring from line i at station j – 1 to station j on the other line takes time ti,j. Each assembly line takes an entry time ei and exit time xi which may be different for the two lines. Give an algorithm for computing the minimum time it will take to build a car chassis.

The below figure presents the problem in a clear picture:

The following information can be extracted from the problem statement to make it simpler:

Two assembly lines, 1 and 2, each with stations from 1 to n.
A car chassis must pass through all stations from 1 to n in order(in any of the two assembly lines). i.e. it cannot jump from station i to station j if they are not at one move distance.
The car chassis can move one station forward in the same line, or one station diagonally in the other line. It incurs an extra cost ti, j to move to station j from line i. No cost is incurred for movement in same line.
The time taken in station j on line i is ai, j.
Si, j represents a station j on line i.

 */
package go;

public class AssemblyLineScheduling {

	public static int  assemblyLineSchedulingSolution(int time, int index, int assemblyLine, String str) {
		str+="\t";
		try {
		System.out.println(str+"Function called for station: "+workTime[assemblyLine][index]+" for index: "+index+" at line: "+assemblyLine+" with time: "+time);
		str+="\t";
		}
		catch(Exception exception) {
	
			//System.out.println(exception);
		}
		//CASE: When there are no more stations in the line
		if(index==station) { 
			System.out.println(str+"Reached the final station returning with: "+time);
			return time;
		}
		
		//LINE Alternating logic
		int altAssemblyLine = (assemblyLine == 0? 1 : 0);
		//System.out.println(str+"Assembly line switched to: "+altAssemblyLine);
		
		//continue the current path
		System.out.println(str+"finding branch 1 at index: "+index+ " stationed at: "+workTime[assemblyLine][index]+"  with cost: "+time+ " at line: "+assemblyLine);
		int branch1 = assemblyLineSchedulingSolution(time+workTime[assemblyLine][index], index+1, assemblyLine, str);
		//switch to the different assembly line
		int branch2;
		System.out.println(str+"finding branch 2 at index: "+index+ " stationed at: "+workTime[altAssemblyLine][index]+"  with cost: "+time+ " at line: "+altAssemblyLine);
		if(index==station-1) {
			System.out.println(str+"return value: "+Integer.MAX_VALUE);
			branch2 = Integer.MAX_VALUE;
		}
		else {
			System.out.println(str+"Branch is calculatin with shift time: "+ shiftTime[assemblyLine][index+1]);
			branch2  = assemblyLineSchedulingSolution(time+workTime[altAssemblyLine][index]+shiftTime[assemblyLine][index+1], index+1, altAssemblyLine, str);
		
		}
		return Math.min(branch1, branch2);
	}
	
	public static int assemblyLineScheduling(int[][] workTime, int[][] shiftTime, int[] enterTime, int[]exitTime, int time, int index, int assemblyLine,String str) {
		System.out.println("Fucntion invoked for index: "+index);
		if(index==workTime.length)
		{	System.out.println(str+"Line: " + assemblyLine + " at index: "+index+" cost:" + time);
		
			return time;
		}
			if(index == 0) {

			int branch1 = assemblyLineScheduling(workTime, shiftTime, enterTime, exitTime, workTime[0][0], 1, 0,str+"\t");
			int branch2 = assemblyLineScheduling(workTime, shiftTime, enterTime, exitTime, workTime[1][0], 1, 1,str+"\t");
			return Math.min(branch1, branch2);
		}
		
		
		int i = index;
		int altAssemblyLine = (assemblyLine==0 ? 1 : 0);
		
		//continue the stream
		int sameLine = time + workTime[assemblyLine][i];
		int switchLine = time + workTime[altAssemblyLine][i] + shiftTime[assemblyLine][i+1];
		
		str+="\t";
		int branch1 = assemblyLineScheduling(workTime, shiftTime, enterTime, exitTime, sameLine, index+1, assemblyLine,str);
		int branch2 = assemblyLineScheduling(workTime, shiftTime, enterTime, exitTime, switchLine, index+1, altAssemblyLine,str);
/*	
		if(branch1 < branch2) {
			System.out.println(str+"Maintaining the line: " + assemblyLine + " at index: "+index+" cost:" + sameLine);
			return branch1;
		}else {
			System.out.println(str+"Switching to line: " + altAssemblyLine + " at index: "+index+" cost:" + switchLine);
			return branch1;
		}
	*/
		return Math.min(branch1, branch2);

		
	}
	
	static int workTime[][] = { { 4, 5, 3, 2 }, { 2, 10, 1, 4 } };
	static int shiftTime[][] = { { 0, 7, 4, 5 }, { 0, 9, 2, 8 } };
	static int enterTime[] = { 10, 12 }, exitTime[] = { 18, 7 };
	static int station = workTime[0].length;
	public static void main(String args[]) {

		
		//saves from the trouble of adding entry and exit timings
		
		System.out.println("station: "+station);

		workTime[0][0] += enterTime[0];
		workTime[1][0] += enterTime[1];
		workTime[0][station-1] += exitTime[0];
		workTime[1][station-1] += exitTime[1];
		
		for(int[] a : workTime) {
			for(int b : a) {
				System.out.print("\t"+b);
			}
			System.out.println();
		}
		
		for(int[] a : shiftTime) {
			for(int b : a) { 
				System.out.print("\t"+b);
			}
			System.out.println();
		}
		
		System.out.println(assemblyLineSchedulingSolution(0, 0, 0, ""));
		System.out.println(assemblyLineScheduling(workTime, shiftTime, enterTime, exitTime, 0, 0, 0,""));
	 }
}
