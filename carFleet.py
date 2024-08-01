class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = {}
        stack = []

        # Combine speed and position, and sort dict from position descending
        for i in range(len(position)):
            cars[position[i]] = speed[i]
        sorted_cars = dict(sorted(cars.items(), key=lambda item: item[0], reverse=True))
        
        # Find the time it takes for each car to get to target
        # If a car behind catches up to a car ahead, remove it from the stack as it becomes a fleet
        for i in sorted_cars.keys():
            time = (target-i)/sorted_cars[i]
            stack.append(time)
            if len(stack) >= 2:
                if stack[-1] <= stack[-2]:
                    stack.pop()  
            print(stack)      

        return len(stack)
