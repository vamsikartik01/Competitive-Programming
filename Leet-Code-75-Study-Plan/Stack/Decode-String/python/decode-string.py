### https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        result = []
        stack = []
        read = False
        key = 0
        value = ""
        for char in s:
            if char == "[" :
                if not stack:
                    read = True
                    value = ""
                else:
                    value += char
                stack.append(char)
                
                continue
            elif char == "]" :
                stack.pop()
                if not stack:
                    read = False
                    value = self.decodeString(value)
                    result.append([key, value])
                    key = 0
                else:
                    value += char
                continue

            if not read:
                if char.isdigit():
                    key = key*10 + int(char)
                    
                else:
                    key = 0
                    result.append([1,char])

            if read:
                value += char

        op = ""
        for [i,c] in result:
            op += i*c

        return op

                