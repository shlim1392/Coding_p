public class Solution {
    public int solution(int n, int k) {
        int pricePerLambSkewer = 12000;
        int pricePerDrink = 2000;
        int freeDrinks = n / 10;
        int paidDrinks = k - freeDrinks;
        int totalCost = (n * pricePerLambSkewer) + (paidDrinks * pricePerDrink);
        return totalCost;
    }
}