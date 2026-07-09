class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ""
        for i in s:
            if i.isalnum():
                clean += i
        
        return clean.lower() == clean[::-1].lower()