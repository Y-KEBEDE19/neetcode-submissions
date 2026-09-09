class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sMap = {} # hashmap for s
        tMap = {} # hashmap for t
        if len(s) != len(t):
            return False
        else:
            for i in range(len(s)):
                charS = s[i]
                charT = t[i]

                if charS in sMap:
                    sMap[charS] += 1
                else:
                    sMap[charS] = 1
                
                if charT in tMap:
                    tMap[charT] += 1
                else:
                    tMap[charT] = 1

        return sMap == tMap



