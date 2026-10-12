# 169. Majority Element
# Difficulty: Easy
# https://leetcode.com/problems/majority-element/
# Runtime: 26 ms | Memory: 21.5 MB

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        dictionary = {}

        for num in nums:
            dictionary[num] = 0

        for num in nums:
            if num in dictionary:
                dictionary[num] += 1

        max_key = max(dictionary, key=dictionary.get)
        return max_key
