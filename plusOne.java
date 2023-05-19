class Solution {
    public int[] plusOne(int[] digits) {
        int i = digits.length;
        int num = 0;
        if (digits[i-1] < 9){
            digits[i-1] = digits[i-1] + 1;
            return digits;
        }
        else {
            digits = new int[digits.length + 1];
            digits[i] = 0;
            digits[i-1] = digits[i-1] + 1;
        }
        return digits;

    }
}
