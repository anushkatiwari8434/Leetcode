class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        a=word.lower()
        b=word.upper()
        c=word.capitalize()
        if (word==a)or (word==b)or (word==c):
            return True
        else:
            return False    
        