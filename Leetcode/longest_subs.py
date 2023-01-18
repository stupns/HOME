import pytest


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len_resulted_set = 0
        for sum_counter in range(len(s)):
            resulted_set = set()
            for symbol in s[sum_counter:]:
                prev_len_resulted_set = len(resulted_set)
                resulted_set.add(symbol)
                len_resulted_set = len(resulted_set)
                if max_len_resulted_set < len_resulted_set:
                    max_len_resulted_set = len_resulted_set
                elif len_resulted_set == prev_len_resulted_set:
                    break
        return max_len_resulted_set


s = Solution()


@pytest.mark.parametrize("string, answer", [
    ("a", 1),
    ("a", 1),
    ("abcabcbb", 3),
    ("pwwkew", 3),
])
def test_solution(string, answer):
    assert s.lengthOfLongestSubstring(string) == answer
