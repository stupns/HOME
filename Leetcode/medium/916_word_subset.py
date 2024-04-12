"""
You are given two string arrays words1 and words2.

A string b is a subset of string a if every letter in b occurs in a including multiplicity.

For example, "wrr" is a subset of "warrior" but is not a subset of "world".
A string a from words1 is universal if for every string b in words2, b is a subset of a.

Return an array of all the universal strings in words1. You may return the answer in any order.



Example 1:

Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["e","o"]
Output: ["facebook","google","leetcode"]
Example 2:

Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["l","e"]
Output: ["apple","google","leetcode"]


Constraints:

1 <= words1.length, words2.length <= 104
1 <= words1[i].length, words2[i].length <= 10
words1[i] and words2[i] consist only of lowercase English letters.
All the strings of words1 are unique.
"""
from collections import Counter
import pytest


class Solution:
    def word_subsets(self, words1: list[str], words2: list[str]) -> list[str]:
        letter = {}
        for word in words2:
            for char in word:
                count = word.count(char)
                if char not in letter or count > letter[char]:
                    letter[char] = count


        res = set(words1)
        for word in words1:
            for k, v in letter.items():
                if v > word.count(k):
                    res.remove(word)
                    break
        return list(res)

    def word_subsets2(self, words1: list[str], words2: list[str]) -> list[str]:
        result = []
        tempDict = Counter()
        for w in words2:
            tempDict |= Counter(w)

        for w in words1:
            if not tempDict - Counter(w):
                result.append(w)
        return result


@pytest.mark.parametrize("input_data, answer", [
    ((["amazon", "apple", "facebook", "google", "leetcode"], ["e", "o"]), ["facebook", "google", "leetcode"]),
    ((["amazon", "apple", "facebook", "google", "leetcode"], ["l", "e"]), ["apple", "google", "leetcode"]),
])
def test_solution(input_data, answer):
    words1, words2 = input_data
    actual = Solution().word_subsets(words1, words2)
    assert sorted(actual) == sorted(answer)


@pytest.mark.parametrize("input_data, answer", [
    ((["amazon", "apple", "facebook", "google", "leetcode"], ["e", "o"]), ["facebook", "google", "leetcode"]),
    ((["amazon", "apple", "facebook", "google", "leetcode"], ["l", "e"]), ["apple", "google", "leetcode"]),
])
def test_solution2(input_data, answer):
    words1, words2 = input_data
    assert Solution().word_subsets2(words1, words2) == answer
