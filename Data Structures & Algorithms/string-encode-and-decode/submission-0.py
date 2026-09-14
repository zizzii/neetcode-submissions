class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for i in range(len(strs)):
            shifted_word = ""
            for j in range(len(strs[i])):
                shifted_word += chr(((ord(strs[i][j]) + 1) % 256))
            encoded += str(len(shifted_word)) + "#" + shifted_word
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while(i < len(s)):
            j = i
            while s[j] != '#':
                j+=1
            length = int(s[i:j])

            start = j + 1
            end = j + length + 1
            encoded_word = s[start:end]

            decoded_word = ""
            for char in encoded_word:
                decoded_word += chr((ord(char)-1)%256)

            decoded.append(decoded_word)
            i = end
        return decoded
