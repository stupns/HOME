import pytest
import re


class Solution:
    def myAtoi(self, string: str) -> int:
        res = re.search("^ *[+-]?\d+", string)
        if res is None:
            return 0
        pre_res = int(res[0])
        if pre_res < -2147483648:
            return -2147483648
        if pre_res > 2147483647:
            return 2147483647
        return pre_res


s = Solution()


@pytest.mark.parametrize("string, answer", [
    ("42", 42),
    ("     -42", -42),
    ("    11111211231231231", 2147483647),
    ("4193 with words", 4193),
    ("words and 987", 0),
    ("0032", 32),
    ("-91283472332", -2147483648),
    ("21474836460", 2147483647)
])
def test_solution(string, answer):
    assert s.myAtoi(string) == answer
