def get_path_memoized(maze):
    if not maze:
        return None
    path= []
    failed_points= set()
    if is_path_memoized(maze, len(maze)-1, len(maze[0])-1, path,failed_points):
        return path
    return None

def is_path_memoized(maze,row, col, path, failed_points):
    if col <0 or row<0 or not maze[row][col]:
        return False
    point = (row, col)
    if point in failed_points:
        return False
    
    is_at_origin = (row==0) and (col==0)

    if (is_at_origin
        or is_path_memoized(maze, row, col-1, path, failed_points)
        or is_path_memoized(maze, row-1, col, path, failed_points)):
        path.append(point)
        return True

    failed_points.add(point)
    return False


print(get_path_memoized([[True, True], [False, True]]))