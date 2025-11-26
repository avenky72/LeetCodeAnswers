class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        
        """
        given an array of integers, find the minimum absolute difference of two elements and return all pairs with that difference
        """

        # sort the array because adjacent numbers would have the lowest differences
        arr.sort()

        output = []
        lowest = float('inf')

        # keep track of the lowest so far and add pairs with that difference to the output

        for i in range(len(arr)-1):
            difference = arr[i+1] - arr[i]
            
            if difference == lowest:
                output.append([arr[i], arr[i+1]])
            elif difference < lowest:
                lowest = difference
                output = [[arr[i], arr[i+1]]]
            else:
                pass
        
        return output
