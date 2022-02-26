class Solution:
    def reverse(self, x: int) -> int:
        answer = 0
        is_plus = -1 if x < 0 else 1
        x = abs(x)
        while True:
            d, m = divmod(x, 10)
            answer = answer * 10 + m
            if not d:
                return answer * is_plus if -2**31 <= answer <= 2**31 - 1 else 0
            else:
                x = d
