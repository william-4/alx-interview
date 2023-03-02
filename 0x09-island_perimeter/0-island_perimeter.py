def island_perimeter(grid: list[list]):
    perimeter = 0
    for row in range(len(grid)):
        for item in range(len(grid[row])):
            if grid[row][item] == 1:
                try:
                    if grid[row-1][item] == 0:
                        perimeter += 1
                except IndexError:
                    perimeter += 1
                try:
                    if grid[row+1][item] == 0:
                        perimeter += 1
                except IndexError:
                    perimeter += 1
                try:
                    if grid[row][item-1] == 0:
                        perimeter += 1
                except IndexError:
                    perimeter += 1
                try:
                    if grid[row][item+1] == 0:
                        perimeter += 1
                except IndexError:
                    perimeter += 1
    return (perimeter)
