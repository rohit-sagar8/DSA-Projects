from PIL import Image, ImageDraw, ImageFont

def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True

def find_empty_cell(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return row, col
    return None, None

def solve_sudoku(board):
    row, col = find_empty_cell(board)
    if row is None and col is None:
        return True

    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num

            if solve_sudoku(board):
                return True

            board[row][col] = 0

    return False

def export_sudoku_image(board, output_filename):
    cell_size = 50
    image_size = cell_size * 9
    image = Image.new("RGB", (image_size, image_size), "white")
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()

    for row in range(9):
        for col in range(9):
            value = str(board[row][col]) if board[row][col] != 0 else ""
            x = col * cell_size + cell_size // 2
            y = row * cell_size + cell_size // 2
            draw.text((x, y), value, fill="black", font=font, anchor="mm")

    image.save(output_filename)

def read_sudoku_from_file(filename):
    sudoku = []
    with open(filename, "r") as file:
        for line in file:
            row = [int(num) for num in line.strip().split()]
            sudoku.append(row)
    return sudoku

if __name__ == "__main__":
    input_filename = "input_sudoku.txt"
    output_image_filename = "sudoku_solution.png"

    sudoku_board = read_sudoku_from_file(input_filename)
    if solve_sudoku(sudoku_board):
        export_sudoku_image(sudoku_board, output_image_filename)
        print("Sudoku solved and image exported.")
    else:
        print("No solution exists.")
