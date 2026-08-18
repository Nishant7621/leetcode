class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        frequency = Counter(nums)

        if k == n:
            return max(nums)

        if k == 1:
            answer = -1

            for number, count in frequency.items():
                if count == 1:
                    answer = max(answer, number)

            return answer

        answer = -1

        if frequency[nums[0]] == 1:
            answer = max(answer, nums[0])

        if frequency[nums[-1]] == 1:
            answer = max(answer, nums[-1])

        return answer