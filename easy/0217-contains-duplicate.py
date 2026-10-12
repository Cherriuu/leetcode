# 217. Contains Duplicate
# Difficulty: Easy
# https://leetcode.com/problems/contains-duplicate/
# Runtime: 20 ms | Memory: 37.3 MB

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        dictionary = {}

        for num in nums:
            if num in dictionary:
                return True
            else:
                dictionary[num] = 1

        return False
