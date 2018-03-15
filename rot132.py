def rot13(x):
    code = ""

    for v in x:
        c = ord(v)
        if c >= ord('a') and c <= ord('z'):
            if c > ord('m'):
                c -= 13
            else:
                c += 13
        elif c >= ord('A') and c <= ord('Z'):
            if c > ord('M'):
                c -= 13
            else:
                c += 13

        code += chr(c)

    return code


user_input=input("Enter the phrase you would like coded")

print(rot13(user_input))
