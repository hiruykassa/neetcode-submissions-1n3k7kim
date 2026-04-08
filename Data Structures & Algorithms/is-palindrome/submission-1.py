class Solution:
    def isPalindrome(self, s: str) -> bool:
        combined = "".join(char.lower() for char in s if char.isalnum())
        reverse = "".join(char.lower() for char in reversed(s) if char.isalnum())

        return combined == reverse
            