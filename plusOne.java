class Solution {
    public int[] plusOne(int[] digits) {
        int j = digits.length;
        for (int i = j - 1; i >= 0; i--)
            {if (digits[i] < 9){
                digits[i] = digits[i] + 1;
                return digits;
            }
            else {
                digits[i] = 0;}
        }
        digits = new int [digits.length + 1];
        digits[0] = 1;
        return digits;

    }
}

/* 
FAILED ATTEMPTS

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
*/
