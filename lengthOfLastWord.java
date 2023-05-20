class Solution {
    public int lengthOfLastWord(String s) {
        String a = " ";
        String n=a.concat(s); 
        String m = n.stripTrailing();
        if (m.length() == 1){
            return 1;
        }
        int i = m.length();
        int count = 0;
        for (int j = i-1; j > 0; j--){
            if (m.charAt(j) != ' '){
                count++;
            }
            else if (m.charAt(j) == ' '){
                return count;
            }
        }
        return count;
    }
}

/*
ALSO ANOTHER VIABLE SOLUTION, BUT LESS FUN
class Solution {
    public int lengthOfLastWord(String s) {
         String [] str = s.split(" ");
        return str[str.length-1].length() ;
    }
}
*/
