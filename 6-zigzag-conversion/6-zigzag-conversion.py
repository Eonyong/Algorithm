from collections import defaultdict

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        word_dict = defaultdict(str)
        answer = ''
        l, depth, cnt = 0, 0, 1
        while l < len(s):
            if not depth:
                cnt = 1
            elif depth == numRows - 1:
                cnt = -1
            
            word_dict[depth] += s[l]
            
            depth += cnt
            l += 1
        else:
            for k, v in word_dict.items():
                answer += v
            else:
                return answer