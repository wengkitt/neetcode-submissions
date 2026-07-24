class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = []
        longest_substring = 0
        for c in s:
            while c in window:
                window.pop(0)

            window.append(c)
            longest_substring = max(longest_substring, len(window))
        
        return longest_substring



        