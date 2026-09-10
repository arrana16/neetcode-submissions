class Solution:
    def isAlpha(self, c: str):
        if (ord(c) >= 48 and ord(c) <= 57) or (ord(c) >= 65 and ord(c) <= 122):
            return True
        return False
    
    def isPalindrome(self, s: str) -> bool:
        print(ord("0"))
        #49->122
        left = 0
        right = len(s)-1

        while (left < right and left < len(s) and right >= 0):
            l = s[left]
            r = s[right]
            print(l, r)

            if not self.isAlpha(l):
                print("1")
                left += 1
                continue
            elif not self.isAlpha(r):
                print("2")
                right -= 1
                continue
            else:
                print("3")
                if l.lower() != r.lower():
                    return False
                left += 1
                right -= 1
            

        
        return True


        