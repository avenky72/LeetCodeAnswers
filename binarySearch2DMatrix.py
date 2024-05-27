class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            print("0")
            return False
        temp_row = []
        last_row = matrix[-1]

        if target > last_row[-1]:
            print("1")
            return False
        elif target == last_row[-1]:
            print("2")
            return True
        else:
            for row in matrix:
                temp = row
                if target == temp:
                    print("3")
                    return True
                if target <= row[-1]:
                    temp_row = row
                    break

        if temp_row:
            left = 0
            right = len(temp_row)-1
            while left <= right:
                mid = (left+right)/2
                if temp_row[mid] == target:
                    print("4")
                    return True
                elif temp_row[mid] > target:
                    right = mid - 1
                elif temp_row[mid] < target:
                    left = mid + 1
            print("5")
            return False
        
    
        print("6")

            
        
