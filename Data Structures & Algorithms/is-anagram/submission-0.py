class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map1 = {}
        map2 = {}
        length_S = len(s)
        length_T = len(t)
        if len(s) != len(t):
            return False
        else:
            for i in range(length_S):
                #this is how I am going to solve it: 
                # I am going to check how many times each letter appears in each word
                # then if the frequency of each letter is the same between the two words
                # then I am going to return true otherwise return false
                # but now to actually implement this
                if s[i] in map1:
                    map1[s[i]] += 1
                else:
                    map1[s[i]] = 1
                if t[i] in map2:
                    map2[t[i]] += 1
                else:
                    map2[t[i]] = 1
                
        if map1==map2:
            return True
        else:
            return False
                