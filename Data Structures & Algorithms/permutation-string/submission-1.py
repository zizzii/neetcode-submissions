class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        matches = 0

        charS1 = [0] * 26
        charS2 = [0] * 26

        if len(s1) > len(s2):
            return False

        for i in range(len(s1)):
            charS1[ord(s1[i]) - ord('a')] += 1 
            charS2[ord(s2[i]) - ord('a')] += 1 

        for i in range(26):
            matches += charS1[i] == charS2[i]
            
        if matches == 26:
            return True

        for i in range(len(s1), len(s2)):
            val = ord(s2[i]) - ord('a')

            if charS2[val] == charS1[val]:
                matches -= 1

            charS2[val] += 1
            

            if charS2[val] == charS1[val]:
                matches += 1
                if matches == 26:
                    return True
            
            c = s2[i-len(s1)]
            val = ord(c) - ord('a')
            if charS2[val] == charS1[val]:
                matches -= 1
            charS2[val] -= 1
            if charS2[val] == charS1[val]:
                matches += 1
                if matches == 26:
                    return True


        return False
