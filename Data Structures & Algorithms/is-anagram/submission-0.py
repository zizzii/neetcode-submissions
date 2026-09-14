class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictS = {}
        for l in s:
            if l not in dictS:
                dictS[l] = 1
            else:
                dictS[l] += 1
        dictT = {}
        for l in t:
            if l not in dictT:
                dictT[l]= 1
            else:
                dictT[l] +=1
        return dictS == dictT