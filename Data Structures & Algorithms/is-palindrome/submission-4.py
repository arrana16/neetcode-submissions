class Solution:
    def isAlpha(self, c: str):
        if (ord(c) >= 48 and ord(c) <= 57) or (ord(c) >= 65 and ord(c) <= 122):
            return True
        return False
    
    def isPalindrome(self, s: str) -> bool:
        #49->122
        left = 0
        right = len(s)-1

        while (left < right and left < len(s) and right >= 0):
            l = s[left]
            r = s[right]

            if not self.isAlpha(l):
                left += 1
                continue
            elif not self.isAlpha(r):
                right -= 1
                continue
            else:
                if l.lower() != r.lower():
                    return False
                left += 1
                right -= 1
            

        
        return True


        