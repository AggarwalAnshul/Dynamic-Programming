package go;

public class MaximumLengthSnakeSequence {

	public static int maximumLengthSnakeSequenceSolution(int[][] matrix) {

		int maxSnakeLength = 0;
		int rows = matrix.length;
		int cols = matrix[0].length;
		int pivot = cols - 1; // 0 index ready

		int[][] dp = new int[rows][cols];
		dp[rows - 1][cols - 1] = 1;

		for (int pi = pivot - 1; pi >= 0; pi--) {
			int piElement = dp[pi][pi];
			for (int j = rows - 1; j > pi; j--) {

				int element = matrix[j][pivot];
				int elementRight = matrix[j][pi + 1];
				int elementBottom = (j != rows - 1 ? matrix[j + 1][pi] : 0);

				if (Math.abs(element - elementRight) == 1
						|| (j != rows - 1 && Math.abs(element - elementBottom) == 1)) {
					dp[j][pi] = Math.max(dp[j][pi + 1], (j != rows - 1 ? dp[j + 1][pi] : 0))+1;
					maxSnakeLength = Math.max(maxSnakeLength, dp[j][pi]);
				}

			}
			for (int i = cols - 1; i >= pivot; i--) {

				int element = matrix[pi][i];
				int elementRight = (i != cols - 1 ? matrix[pi][i + 1] : 0);
				int elementBottom = matrix[pi + 1][i];

				if (Math.abs(elementBottom - element) == 1
						|| (i != cols - 1 && Math.abs(elementRight - element) == 1)) {

					dp[pi][i] = Math.max(dp[pi + 1][i], (i != cols - 1 ? dp[pi][i + 1] : 0))+1;
					maxSnakeLength = Math.max(maxSnakeLength, dp[pi][i]);
				}
			}

		}

		return maxSnakeLength;

	}

	public static void main(String args[]) {

		int[][] matrix = new int[][] { { 9, 6, 5, 2 }, { 8, 7, 6, 5 }, { 7, 3, 1, 6 }, { 1, 1, 1, 7 }, };
		System.out.println(maximumLengthSnakeSequenceSolution(matrix));

	}
}
