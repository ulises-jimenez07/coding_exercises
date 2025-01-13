from typing import List


def flood_fill(screen: List[List[int]], r: int, 
        c: int, old_color, new_color: int):
    if(
        r < 0
        or r >= len(screen)
        or c < 0
        or c >= len(screen[0])
        or screen[r][c] != old_color
    ):
       return
    
    screen[r][c] = new_color
    flood_fill(screen, r + 1, c, old_color, new_color)
    flood_fill(screen, r - 1, c, old_color, new_color)
    flood_fill(screen, r, c + 1, old_color, new_color)
    flood_fill(screen, r, c - 1, old_color, new_color)



def paint_fill(
        screen: List[List[int]], r: int, 
        c: int, new_color: int
) -> List[List[int]]:
    if not screen:
        return None
    

    old_color = screen[r][c]
    flood_fill(screen, r, c, old_color, new_color)
    return screen

if __name__ == "__main__":
   print( paint_fill([[1, 2, 5], [2, 2, 4], [2, 8, 6]],
            1,
            1,
            3)
   )