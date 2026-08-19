class Solution:
    def romanToInt(self, s: str) -> int:
        symbol = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        p1 = 0
        num = 0

        while p1 < len(s):
            if p1 + 1 != len(s):
                if s[p1] == "I" and s[p1+1] == "V":
                    num = num + 4
                    p1 = p1 + 2
                elif s[p1] == "I" and s[p1+1] == "X":
                    num = num + 9
                    p1 = p1 + 2
                elif s[p1] == "X" and s[p1+1] == "L":
                    num = num + 40
                    p1 = p1 + 2
                elif s[p1] == "X" and s[p1+1] == "C":
                    num = num + 90
                    p1 = p1 + 2
                elif s[p1] == "C" and s[p1+1] == "D":
                    num = num + 400
                    p1 = p1 + 2
                elif s[p1] == "C" and s[p1+1] == "M":
                    num = num + 900
                    p1 = p1 + 2
                else:
                    num = num + symbol[s[p1]]
                    p1 = p1 + 1
            else:
                    num = num + symbol[s[p1]]
                    p1 = p1 + 1
        
        return num