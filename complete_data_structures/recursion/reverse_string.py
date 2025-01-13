def reverse(strn):
    if len(strn) == 0:
        return ""
    return reverse(strn[1:]) + strn[0]


print(reverse("hola"))
