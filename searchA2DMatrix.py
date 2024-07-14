class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t_row = []
        if not matrix or not matrix[0]:
            return False

        for row in matrix:
            if target >= row[0] and target <= row[len(row)-1]:
                t_row = row
                break
        print(t_row)

        if t_row:
            left = 0
            right = len(t_row)-1
            while left <= right:
                mid = (left + right) // 2
                if t_row[mid] == target:
                    return True
                elif t_row[mid] > target:
                    right = mid - 1
                elif t_row[mid] < target:
                    left = mid + 1
            return False

            
        
        
