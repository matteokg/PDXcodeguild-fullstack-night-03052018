def rot_13(string):
    pre = "abcdefghikjlmnopqrstuvwxyz"
    post = "nopqrstuvwxyzabcdefghijklm"
    ret = ''
    for char in string:
        index = pre.find(char)
        if index < 0:
            ret += char
        else:
            ret += post[index]

    return ret

user_input = input("what you would like coded")

print(rot_13(user_input))
