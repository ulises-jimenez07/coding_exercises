
def add_paren(arr, left_rem, right_rem, string_arr, idx):
    if left_rem < 0 or right_rem < left_rem:
        return
    if left_rem == 0 and right_rem == 0:
        elem = "".join(string_arr)
        print(elem)
        arr.append(elem)
    else:
        string_arr[idx] = "("
        add_paren(arr, left_rem -1 , right_rem, string_arr, idx + 1)

        string_arr[idx] = ")"
        add_paren(arr, left_rem, right_rem - 1, string_arr, idx + 1)

def generate_parentheses_permutations(n):
    results = []
    string_arr = ["*"] * n * 2
    add_paren(results, n, n, string_arr, 0)
    return results

print(generate_parentheses_permutations(3))