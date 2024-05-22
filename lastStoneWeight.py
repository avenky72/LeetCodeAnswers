class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        if len(stones) == 0:
            return 0
        stone = sorted(stones)
        
        while len(stone) > 1:
            y = stone.pop(len(stone)-1)
            x = stone.pop(len(stone)-1)
            if x == y:
                pass
            elif x != y:
                stone.append(y-x)
                stone = sorted(stone)
        if len(stone) == 0:
            return 0
        else:
            return stone[0]       
