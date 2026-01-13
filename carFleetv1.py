class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        """
        calculate when cars arrive to the end
        if a car behind has a shorter or same time to finish compared to a car ahead then they would be a fleet
        """

        cars = sorted(zip(position, speed), reverse=True)

        fleets = []

        for p, s in cars:
            time = (target - p) / s

            # check if there are other times in the fleet, if yeah check if quicker or not
            if not fleets or time > fleets[-1]:
                fleets.append(time)
            
            # if else, that means it catches the car ahead and doesn't need to be added to stack

        return len(fleets)

            
