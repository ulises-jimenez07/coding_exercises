def get_perms(str_word):
    result = []
    get_perms_inner("", str_word, result)
    return result


def get_perms_inner(prefix, remainder, result):
    if len(remainder) == 0:
        result.append(prefix)
    length = len(remainder)
    for i in range(length):
        before = remainder[:i]
        after = remainder[i + 1 :]
        c = remainder[i]
        get_perms_inner(prefix + c, before + after, result)


if __name__ == "__main__":
    print(get_perms("str"))
