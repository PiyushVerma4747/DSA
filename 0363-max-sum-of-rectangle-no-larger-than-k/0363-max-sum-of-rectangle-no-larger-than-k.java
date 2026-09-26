// import java.util.*;// for inmporting tree set in java 
// class Solution {
//     public int maxSumSubmatrix(int[][] matrix, int k) {
//         int rows = matrix.length;
//         int cols = matrix[0].length;
//         int answer = Integer.MIN_VALUE;

//         for (int left = 0; left < cols; left++) {
//             int[] rowSum = new int[rows];
//             for (int right = left; right < cols; right++) {
//                 // Add the current column to rowSum
//                 for (int r = 0; r < rows; r++) {
//                     rowSum[r] += matrix[r][right];
//                 }
//                 // Find maximum subarray sum <= k
//                 int currentSum = 0;
//                 TreeSet<Integer> prefixSums = new TreeSet<>();
//                 prefixSums.add(0);
//                 for (int value : rowSum) {
//                     currentSum += value;
//                     // Find smallest prefix >= currentSum - k
//                     Integer previous = prefixSums.ceiling(currentSum - k);
//                     if (previous != null) {
//                         answer = Math.max(
//                             answer,
//                             currentSum - previous
//                         );
//                     }
//                     prefixSums.add(currentSum);
//                     // k is the maximum possible answer
//                     if (answer == k) {
//                         return k;
//                     }
//                 }
//             }
//         }
//         return answer;
//     }
// }

// ABOVE MY SOLUTION IS NOT OPTIMISESD

import java.util.*;

class Solution {
    public int maxSumSubmatrix(int[][] matrix, int k) {

        int rows = matrix.length;
        int cols = matrix[0].length;

        // Make cols the smaller dimension
        if (rows < cols) {
            int[][] temp = new int[cols][rows];

            for (int i = 0; i < rows; i++) {
                for (int j = 0; j < cols; j++) {
                    temp[j][i] = matrix[i][j];
                }
            }

            matrix = temp;
            rows = matrix.length;
            cols = matrix[0].length;
        }

        int answer = Integer.MIN_VALUE;

        // Fix the top row
        for (int top = 0; top < rows; top++) {

            int[] colSum = new int[cols];

            // Fix the bottom row
            for (int bottom = top; bottom < rows; bottom++) {

                // Compress rows into a 1D array
                for (int c = 0; c < cols; c++) {
                    colSum[c] += matrix[bottom][c];
                }

                // Maximum subarray sum <= k
                TreeSet<Integer> prefix = new TreeSet<>();
                prefix.add(0);

                int currentSum = 0;

                for (int value : colSum) {

                    currentSum += value;

                    Integer previous =
                            prefix.ceiling(currentSum - k);

                    if (previous != null) {
                        answer = Math.max(
                                answer,
                                currentSum - previous
                        );
                    }

                    prefix.add(currentSum);

                    if (answer == k) {
                        return k;
                    }
                }
            }
        }
        return answer;
    }
}

