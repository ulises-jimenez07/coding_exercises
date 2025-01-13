def reverse(str):
    length = len(str)
    backward=""
    for i in range(length-1,-1,-1) :
        backward+=str[i]
    return backward

print(reverse("hola"))