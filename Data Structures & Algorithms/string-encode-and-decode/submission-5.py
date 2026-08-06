class Solution:

    def encode(self, strs: List[str]) -> str:
        # Encoding in format of: num#ActualString
        # For Example: 5#hello would be "hello", because it 5 chracters and the word is hello
        # Another example: 1#, would be "," because it has 1 chracter and the char is ,

        encoded_str = ""
        for i, s in enumerate(strs):
            encoded_str += str(len(s)) + "#" + s 
            # if i != len(strs) -1:
            #     encoded_str += ","

        return encoded_str
            
    def decode(self, s: str) -> List[str]:

        decoded_strings = []

        i = 0

        while i < len(s):

            j = i

            # Find the "#" that ends the length

            while s[j] != "#":

                j += 1

            # Everything between i and j is the word's length

            word_length = int(s[i:j])

            # The word begins after "#"

            word_start = j + 1

            word_end = word_start + word_length

            decoded_strings.append(s[word_start:word_end])

            # Move to the beginning of the next encoded word

            i = word_end

        return decoded_strings