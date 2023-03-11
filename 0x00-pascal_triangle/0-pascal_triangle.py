#!/usr/bin/python3
"""
Module that defines an algorithm for pascal's triangle
"""

def pascal_triangle(n):
    List = []
    if n <= 0:
        return (List)

    for row in range(n):
        List.append([])
        List[row].append(1)
        for index in range(1, row):
            List[row].append(List[row-1][index-1] + List[row-1][index])
        if(n != 0):
            List[row].append(1)
    return (List)
        
        
