class Solution:
    def isPalindrome(self, s: str) -> bool:
        formatted_string = ''.join(char for char in s if char.isalnum()).lower()
        p_head = 0
        p_tail = len(formatted_string) - 1

        while p_tail >= p_head:
            if formatted_string[p_head] != formatted_string[p_tail]:
                return False
            
            p_head+=1
            p_tail-=1
        
        return True


        