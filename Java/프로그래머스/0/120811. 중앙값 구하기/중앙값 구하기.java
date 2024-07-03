import java.util.Arrays;
public class Solution {
    public int solution(int[] array) {
        Arrays.sort(array);
        int length = array.length;
        int midIndex = length / 2;
        return array[midIndex];
    }
}
