class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_parts = []
        for string in strs:
            encoded_parts.append(str(len(string)) + "#" + string)
        return "".join(encoded_parts)
    def decode(self, s: str) -> List[str]:
        result = []
        i=0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            string_start = j + 1
            string_end = string_start + length
            result.append(s[string_start:string_end])
            i = string_end
        return result


# store length of string + "#" + string
# 5#Hello5#World