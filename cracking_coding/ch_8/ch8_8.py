def print_perms(string):
    result = []
    letter_count_map = build_freq_tables(string)
    print_perms_inner(letter_count_map, "", len(string), result)
    return result


def build_freq_tables(string):
    letter_count_map = {}
    for letter in string:
        if letter in letter_count_map:
            letter_count_map[letter] += 1
        else:
            letter_count_map[letter] = 1
    return letter_count_map


def print_perms_inner(letter_count_map, prefix, remaining, result):
    if remaining == 0:
        result.append(prefix)
        return

    for character in letter_count_map:
        count = letter_count_map[character]
        if count > 0:
            letter_count_map[character] -= 1
            print_perms_inner(letter_count_map, prefix + character, remaining - 1, result)
            letter_count_map[character] = count


if __name__ == "__main__":
    print(print_perms("aaf"))
