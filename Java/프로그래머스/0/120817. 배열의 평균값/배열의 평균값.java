class Solution {
    public double solution(int[] numbers) {
        double answer = sum(numbers) / (double) numbers.length;
        return answer;
    }

    private int sum(int[] numbers) {
        int sum = 0;
        for (int number : numbers) {
            sum += number;
        }
        return sum;
    }
}