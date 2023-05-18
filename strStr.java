class Solution {
    public int strStr(String haystack, String needle) {
        int a = needle.length();
        int b = 0;
        for (int i = 0; i < haystack.length(); i++){
            if (haystack.charAt(i) == needle.charAt(b)){
                b++;
            }
            else {
                i = i - b;
                b = 0;
            }
            if (b == a){
                return i - a + 1;
            }
        }
        return -1;
    }
}
