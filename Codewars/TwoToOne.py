"""
a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
longest(a, b) -> "abcdefklmopqwxy"

a = "abcdefghijklmnopqrstuvwxyz"
longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"
"""

def longest(a1, a2):
    return ''.join(sorted(set(a1 + a2)))

a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"

print(longest(a, b))