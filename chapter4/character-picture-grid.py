# character-picture-grid
# Author: Daniel Shin
# Source: Automate the Boring Stuff with Python Ch.4 Practice Project2 (p103)

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']] # from source

for iy in range(len(grid[0])):
    for ix in range(len(grid)):
        print(grid[ix][iy],end='')
    print('')
    
