import java.util.ArrayList;
import java.util.List;

public class Solution {
    public static List<Integer> solution(int n, int[] numlist) {
        List<Integer> result = new ArrayList<>();
        
        for (int num : numlist) {
            if (num % n == 0) {
                result.add(num);
            }
        }
        
        return result;
    }
}