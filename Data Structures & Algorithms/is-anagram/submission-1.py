class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        s_letters = [0] * 26
        t_letters = [0] * 26

        for char in s:
            s_letters[ord(char)-97] += 1

        for char in t:
            t_letters[ord(char)-97] += 1

        for i in range(len(s_letters)):
            if s_letters[i] != t_letters[i]:
                return False

        return True


        # return True
        