# 169. Majority Element
# Difficulty: Easy
# https://leetcode.com/problems/majority-element/
# Runtime: 31 ms | Memory: 21.6 MB

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        dictionary = {}
        max = 0

        for num in nums:
            dictionary[num] = 0

        for num in nums:
            if num in dictionary:
                dictionary[num] += 1

        for key, value in dictionary.items():
            if value > max:
                max = value
                winner = key

        return winner
