class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        dict = {}
        left = 0
        best = 0

        for right in range(len(fruits)):
            if fruits[right] not in dict:
                dict[fruits[right]] = 0
            dict[fruits[right]] += 1

            while len(dict) > 2:
                dict[fruits[left]] -= 1
                if dict[fruits[left]] == 0:
                    del dict[fruits[left]]
                left += 1

            best = max(best, right - left + 1)

        return best