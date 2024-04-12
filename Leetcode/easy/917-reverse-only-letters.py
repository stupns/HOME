import pytest


class Solution:
    def reverse_only_letters(self, s: str) -> str:
        ls = list(s)
        left = 0
        right = len(ls) - 1

        while left < right:
            if not ls[right].isalpha():
                right -= 1
            elif not ls[left].isalpha():
                left += 1
            else:
                ls[left], ls[right] = ls[right], ls[left]
                left += 1
                right -= 1

        return "".join(ls)

@pytest.mark.parametrize("input_data, result", [
    (("ab-cd"), "dc-ba"),
    # Example 2: ((param1_value, param2_value), expected_result),
    # Add more test cases as needed
])
def test_solution(input_data, result):
    # Unpack the input data for the test case
    param1 = input_data
    # Initialize the Solution class instance
    solution = Solution()
    # Assert that the method func_name returns the expected result
    assert solution.reverse_only_letters(param1) == result
