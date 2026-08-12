class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anMap = {}
        for word in strs:
            counts = [0] * 26
            for c in word:
                index = ord(c) - 97 
                counts[index] += 1
                
            strHash = ""
            for i in range(len(counts)):
                strHash += (chr(i+97) + str(counts[i]))
            
            if (strHash in anMap):
                newList = anMap[strHash]
                newList.append(word)
                anMap[strHash] = newList
            else:
                anMap[strHash] = [word]
        
        groups = []
        for key in anMap:
            groups.append(anMap[key])

        return groups
