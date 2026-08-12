class Solution:

    def encode(self, strs: List[str]) -> str:
        if (len(strs) == 0):
            return chr(258)
        returnString = chr(257).join(strs)
        print(returnString)
        return returnString

    def decode(self, s: str) -> List[str]:
        print(s)
        if s == chr(258):
            return []
        
        return s.split(chr(257))
