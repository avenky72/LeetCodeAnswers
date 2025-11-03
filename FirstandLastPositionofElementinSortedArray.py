class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        found = [-1, -1]


        # Binary Search Helper Function
        def b_search(target):
            left, right = 0, len(nums)-1

            while left <= right:
                med = (left + right) // 2

                if nums[med] == target:
                    print("found: ", med)
                    return med

                elif nums[med] < target:
                    left = med + 1

                elif nums[med] > target:
                    right = med - 1
            return None


        
        place = b_search(target)

        i, j = place, place
        
        if place is not None:
            while (i > 0 and j < len(nums)-1):
                if (nums[i-1] != target and nums[j+1] != target):
                    break
                if nums[i-1] == target:
                    i -= 1
                if nums[j+1] == target:
                    j += 1
            found = [i, j]
            return found
        
        else:
            return found

        


   


        
        
