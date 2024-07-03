import java.util.ArrayList;
import java.util.List;

public class Solution {
    public int[] solution(int n) {
        List<Integer> oddNumbers = new ArrayList<>();
        for (int i = 1; i <= n; i += 2) {
            oddNumbers.add(i);
        }
        int[] result = new int[oddNumbers.size()];
        for (int i = 0; i < oddNumbers.size(); i++) {
            result[i] = oddNumbers.get(i);
        }
        
        return result;
    }
}
