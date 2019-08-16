package go;

public class LongestRepeatedSubsequence {


	public static String reverse(String str) {
		String reverse = "";
		int length = str.length();
		for(int i=length-1; i>=0; i--) {
			reverse += str.charAt(i);
		}
		return reverse;
	}
	public static String longestPalindromicSubsequenceSolution(String str) {
		
	int maxLength = 0;
	int length = str.length();
	int[][] dp = new int[length+1][length+1];

	//Initializing the dp matrix
	for(int i=0; i<=length; i++) {
		dp[i][0] = 0;
		dp[0][i] = 0;
	}

	//Populating the dp matrix
	for(int i=1; i<=length; i++) {
		for(int j=1; j<=length; j++) {
			
			if( str.charAt(i-1)==str.charAt(j-1) && i!=j) {
				dp[i][j] = dp[i-1][j-1] + 1;
			}else {
				dp[i][j] = Math.max(dp[i][j-1], dp[i-1][j]);
			}
		}
	}
	
	String longestRepeatedSubseqeunce = "";
	//Reading the LongestRepeated Subsequence
	int i = length, j = length;
	while(i>0 && j>0) {
		
		if(str.charAt(i-1)==str.charAt(j-1) && i!=j){
				longestRepeatedSubseqeunce += str.charAt(i-1);
				i-=1;
				j-=1;
			}
		else {
			if(dp[i-1][j] > dp[i][j-1]){
				i-=1;
			}
			else {
				j-=1;
			}
		}
	}
	return reverse(longestRepeatedSubseqeunce);
}
	public static void main(String args[]) {
			
			String string = "ATACTCGGA";
			System.out.println( longestPalindromicSubsequenceSolution(string) );
		}

}
