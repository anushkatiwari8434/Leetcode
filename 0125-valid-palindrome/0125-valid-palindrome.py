class Solution:
    def isPalindrome(self, s: str) -> bool:
    
        temp = ""

        for ch in s:
            if ch.isalnum():
                temp += ch.lower()

        rev = temp[::-1]

        return temp == rev
        