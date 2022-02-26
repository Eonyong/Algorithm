class Solution:
    def reverse(self, x: int) -> int:
        is_plus = '-' if x < 0 else ''
        x = int(is_plus + ''.join(reversed(str(abs(x)))))
        return x if -2**31 <= x <= 2**31 - 1 else 0