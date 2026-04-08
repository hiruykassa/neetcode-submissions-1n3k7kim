class Solution:
    def isPalindrome(self, s: str) -> bool:
        #iterate
        cleaned = ""
        for i in s:
            if i in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890":
                cleaned += i.lower()
        #reverse it
        reverse = "".join(reversed(cleaned))
            
        #compare the reverse to the original 
        
        return reverse == cleaned
