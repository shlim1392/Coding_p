class Solution {
    public int solution(int n) {
        int sum = 0;
        for (int x = 0; x <= n; x++) { 
            if (x % 2 == 0) {
                sum += x;
            }
        }
        return sum;
    }
}
