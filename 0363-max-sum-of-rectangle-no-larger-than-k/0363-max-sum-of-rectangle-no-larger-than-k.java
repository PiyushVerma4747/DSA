import java.util.*;// for inmporting tree set in java 

class Solution {
    public int maxSumSubmatrix(int[][] matrix, int k) {
        int rows = matrix.length;
        int cols = matrix[0].length;
        int answer = Integer.MIN_VALUE;

        for (int left = 0; left < cols; left++) {
            int[] rowSum = new int[rows];
            for (int right = left; right < cols; right++) {
                // Add the current column to rowSum
                for (int r = 0; r < rows; r++) {
                    rowSum[r] += matrix[r][right];
                }
                // Find maximum subarray sum <= k
                int currentSum = 0;
                TreeSet<Integer> prefixSums = new TreeSet<>();
                prefixSums.add(0);
                for (int value : rowSum) {
                    currentSum += value;
                    // Find smallest prefix >= currentSum - k
                    Integer previous = prefixSums.ceiling(currentSum - k);
                    if (previous != null) {
                        answer = Math.max(
                            answer,
                            currentSum - previous
                        );
                    }
                    prefixSums.add(currentSum);
                    // k is the maximum possible answer
                    if (answer == k) {
                        return k;
                    }
                }
            }
        }
        return answer;
    }
}