#!/usr/bin/python3
"""
Module defining a function to calcutate perimeter
"""


def island_perimeter(grid):
    """
    Returns perimeter of an island
    Args:
        grid (list): list of lists representing the island and water body
    Return:
        Perimeter of the island
    """
    if grid == []:
        return 0    
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
