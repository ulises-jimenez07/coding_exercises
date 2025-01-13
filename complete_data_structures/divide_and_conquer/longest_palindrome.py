def find_longest_p_s(s, start_idx, end_idx):
    if start_idx > end_idx:
        return 0
    if start_idx == end_idx:
        return 1
    if s[start_idx] == s[end_idx]:
        return 2 + find_longest_p_s(s, start_idx + 1, end_idx - 1)
    op1 = find_longest_p_s(s, start_idx, end_idx - 1)
    op2 = find_longest_p_s(s, start_idx + 1, end_idx)
    return max(op1, op2)


print(find_longest_p_s("ELRMENMET", 0, 8))
