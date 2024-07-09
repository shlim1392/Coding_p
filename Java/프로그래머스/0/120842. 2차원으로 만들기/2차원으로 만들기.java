import java.util.Arrays;

public class Solution {
    public int[][] solution(int[] num_list, int n) {
        int length = num_list.length;
        int rowCount = length / n;
        int[][] result = new int[rowCount][n];
        
        for (int i = 0; i < rowCount; i++) {
            for (int j = 0; j < n; j++) {
                result[i][j] = num_list[i * n + j];
            }
        }
        
        return result;
    }
}