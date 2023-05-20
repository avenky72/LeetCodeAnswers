class Solution {
    public int singleNumber(int[] nums) {
        int count = 0;
        for (int i = 0; i < nums.length; i++) {
            count = 0;
            for (int j = 0; j < nums.length; j++) {
                if (nums[i] == nums[j]) {
                    count++;
                }
            }
            if (count == 1) {
                return nums[i];
            }
        }
        return -1;
    }
}

/* 

FAILED SUBMISSIONS:

class Solution {
    public int singleNumber(int[] nums) {
        int i = 0;
        int j = 0;
        int n;
        boolean de = true;

        for(i = 0; i < nums.length-1; i++)
        {
            n = nums[i];

            for(j = i+1; j < nums.length; j++)
            {
                if(n == nums[j])
                {
                    de = false;;
                }
                if(j == nums.length-1) 
                {
                    return n;
                }
            }
            if (de){
                return nums
            }

        }
        return nums[nums.length-1];
    }
}


class Solution {
    public int singleNumber(int[] nums) {
        boolean exist = true;
        int answer = 0;
        if (nums.length == 1){
            return nums[0];
        }
        for (int i = 0; i < nums.length; i++){
            for (int j = i + 1; j < nums.length; j++){
                if (nums[i] == nums[j]){
                    exist = false;
                }
                if (nums[i] != nums[j]){
                    exist = true;
                }
            }
            if (exist){
                answer = nums[i];
                System.out.println(answer);
            }
            if (exist == false){
                answer = nums[nums.length-1];
            }

        }
        System.out.println(answer);
        return answer; 
    }
}


class Solution {
    public int singleNumber(int[] nums) {
        int count = 0;
        for (int i = 0; i < nums.length; i++) {
            count = 0;
            for (int j = j; j < nums.length; j++) {
                if (nums[i] == nums[j]) {
                    count++;
                }
            }
            if (count == 0) {
                return nums[i];
            }
        }
    }
}

*/
