class Solution {
    public boolean isPalindrome(int x) {
        int n = String.valueOf(x).length();
        String num = String.valueOf(x);
        String rev = "";
        for (int i = n-1; i >= 0; i--){
            rev += num.charAt(i);
        }
        if (rev.equals(num)){
            return true;
        }
        else{
            System.out.print(rev);
            return false;
        }
    }       
  }
