### https://leetcode.com/problems/decode-string/description/

def decode_string(s: str) -> str:
    stack = []
    
    key = 0
    value = ""
    flip = False
    for char in s:
        if not char.isdigit():
            if key == 0:
                stack.append(char)
                continue

            if char == '[':
                flip = True


            if flip:
                value += char

        else:
            key = key*10+int(char)


    print(stack)

    return s

def main():
    inp = "2[abc]3[cd]e"
    op = decode_string(inp)
    print(op)

if __name__=="__main__":
    main()