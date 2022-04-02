def grid_paths(rows, cols, memo = {}):
    if rows == 0 and cols == 0:
        return 1

    if rows < 0 or cols < 0:
        return 0

    if (rows, cols) in memo:
        return memo[(rows, cols)]

    memo[(rows, cols)] = grid_paths(rows-1, cols, memo) + grid_paths(rows, cols-1, memo)
    #sum_paths = grid_paths(rows-1, cols, memo) + grid_paths(rows, cols-1, memo)
    return memo[(rows, cols)]


print(grid_paths(20,20))

