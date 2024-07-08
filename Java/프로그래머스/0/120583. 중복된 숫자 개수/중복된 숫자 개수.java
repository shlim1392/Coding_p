public class Solution {
    public static int solution(int[] array, int n) {
        int count = 0;
        
        for (int num : array) {
            if (num == n) {
                count++;
            }
        }
        
        return count;
    }
}