# https://leetcode.com/problems/string-to-integer-atoi/

class Solution:
    def myAtoi(self, s: str) -> int:
        num = ""
        s = s.lstrip()

        if s == "":
            return 0

        if s[0] in "-+":
            num += s[0]
            s = s[1:]

        for char in s:
            if char.isnumeric():
                num += char
            else:
                break

        try:
            num = int(num)
        except ValueError:
            return 0

        return max(min(num, 2**31-1), -2**31)
