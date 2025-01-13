def bit_insertion(n,m,i,j):
    ones_left= -1 <<(j+1) #move ones to the left of j
    ones_right= (1<<i) -1 #place ones at the right of i
    mask = ones_left | ones_right # create mask with 0's where m will be inserted
    cleared = n & mask #clear the number for the insertion
    moved = m<<i #moved m i spaces
    return cleared | moved



bin_num=bit_insertion(int("10000000000", 2), int("10011", 2), 2, 6)
print(bin(bin_num))