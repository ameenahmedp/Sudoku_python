def find_next_empty(puzzle):
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == 0:
                return r,c
    return None, None


def is_valid(puzzle, guess, row, col):
    #row checking
    row_vals = puzzle[row]
    if guess in row_vals:
        return False

    #column checking
    col_vals = []
    for i in range(9):
        col_vals.append(puzzle[i][col])
    if guess in col_vals:
        return False

    #3*3 grid checking
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3

    for c in range(col_start, col_start + 3):
        for r in range(row_start, row_start + 3):
            if puzzle[r][c] == guess:
                return False
    #all checking over
    return True


def solve_sudoku(puzzle):
    row, col = find_next_empty(puzzle)

    if row is None:
        return True

    for guess in range(1,10):
        if is_valid(puzzle, guess, row, col):
            #add the guess to the table
            puzzle[row][col] = guess 

            #recursively call function
            if solve_sudoku(puzzle):
                return True       

        #if guess is not valid then backtrack and try new number
        puzzle[row][col] = 0

    #if puzzzle unsovable
    return False

if __name__ == '__main__':
    example_board = [
        [3, 9, 0,  0, 5, 0,  0, 0, 0],
        [0, 0, 0,  2, 0, 0,  0, 0, 5],
        [0, 0, 0,  7, 1, 9,  0, 8, 0],
        
        [0, 5, 0,  0, 6, 8,  0, 0, 0],
        [2, 0, 6,  0, 0, 3,  0, 0, 0],
        [0, 0, 0,  0, 0, 0,  0, 0, 4],

        [5, 0, 0,  0, 0, 0,  0, 0, 0],
        [6, 7, 0,  1, 0, 5,  0, 4, 0],
        [1, 0, 9,  0, 0, 0,  2, 0, 0],
    ]
    print("Input table : ")
    for c in range(0,3):
        print(example_board[c])
    print("\n")

    for c in range(3,6):
        print(example_board[c])
    print("\n")
    
    for c in range(6,9):
        print(example_board[c])
    
    print("\n")
    print(solve_sudoku(example_board))
    print("\n")

    print("Solved Table : ")
    for c in range(0,3):
        print(example_board[c])
    print("\n")

    for c in range(3,6):
        print(example_board[c])
    print("\n")

    for c in range(6,9):
        print(example_board[c])
