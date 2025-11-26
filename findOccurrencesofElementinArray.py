class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        
        """
        Given an array of integers and a input integer, find the index of that input integer in the array based on the query values from the query array
        """

        # Save each index of the occurrence of X in nums
        occurrences = []
        answer = []

        for i in range(len(nums)):
            if nums[i] == x:
                occurrences.append(i)

        # Loops through the queries and make sure the q is within the bounds of occurrences
        for q in queries:
            if q >= 1 and q <= len(occurrences):
                answer.append(occurrences[q-1])
            else:
                answer.append(-1)
        return answer
            
        


        
