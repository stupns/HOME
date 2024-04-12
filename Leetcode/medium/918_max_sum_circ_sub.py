'''Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.

A circular array means the end of the array connects to the beginning of the array. Formally, the next element of nums[i] is nums[(i + 1) % n] and the previous element of nums[i] is nums[(i - 1 + n) % n].

A subarray may only include each element of the fixed buffer nums at most once. Formally, for a subarray nums[i], nums[i + 1], ..., nums[j], there does not exist i <= k1, k2 <= j with k1 % n == k2 % n.



Example 1:

Input: nums = [1,-2,3,-2]
Output: 3
Explanation: Subarray [3] has maximum sum 3.
Example 2:

Input: nums = [5,-3,5]
Output: 10
Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10.
Example 3:

Input: nums = [-3,-2,-3]
Output: -2
Explanation: Subarray [-2] has maximum sum -2.
'''
import pytest


class Solution:
    def max_subarray_sum_circular(self, nums: list[int]) -> int:
        curr_max, curr_min = 0, 0
        max_sum, min_sum = nums[0], nums[0]
        total_sum = 0

        for num in nums:
            curr_max = max(curr_max, 0) + num
            max_sum = max(curr_max, max_sum)

            curr_min = min(curr_min, 0) + num
            min_sum = min(curr_min, min_sum)

            total_sum += num

        if total_sum == min_sum:
            return max_sum

        return max(max_sum, total_sum - min_sum)


@pytest.mark.parametrize("input_data, result", [
    ([1, -2, 3, -2], 3),
    ([5, -3, 5], 10),
    ([-3, -2, -3], -2)
    # Add more test cases as needed
])
def test_solution(input_data, result):
    # Unpack the input data for the test case
    param1 = input_data
    # Initialize the Solution class instance
    solution = Solution()
    # Assert that the method func_name returns the expected result
    assert solution.max_subarray_sum_circular(param1) == result
