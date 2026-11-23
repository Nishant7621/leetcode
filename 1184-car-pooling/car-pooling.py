
class Solution:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        arr = [0] * 1001

        for passengers, start, end in trips:
            arr[start] += passengers
            arr[end] -= passengers

        current = 0

        for i in range(1001):
            current += arr[i]

            if current > capacity:
                return False

        return True
