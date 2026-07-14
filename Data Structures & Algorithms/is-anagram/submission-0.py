class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        char_counter = dict()

        for c in s:
            if c in char_counter:
                char_counter[c]+=1
            else:
                char_counter[c] = 1
        
        for c in t:
            if c not in char_counter:
                return False
            else:
                char_counter[c]-=1
                if char_counter[c]<0:
                    return False
        
        for v in char_counter.values():
            if v != 0:
                return False

        return True

        