class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        else:
            trip = [x - y for x, y in zip(gas, cost)]
            start = 0
            tank = 0
            for i in range(len(trip)):
                tank += trip[i]
                if tank < 0:
                    # The idea is that if you can make it up to i and then i can make it to the end, i can make it all the way
                    start = i + 1
                    tank = 0
            return start
