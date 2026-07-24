class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []

        for i in range(len(position)):
            cars.append((position[i], speed[i]))

        cars.sort(reverse=True)

        fleet = []

        for car_position, car_speed in cars:
            time = (target - car_position) / car_speed

            if not fleet or time > fleet[-1]:
                fleet.append(time)

        return len(fleet)
                