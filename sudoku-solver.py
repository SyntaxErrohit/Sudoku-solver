import pygame

pygame.init()

display_width = 452
display_height = 452
game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Sudoku solver")
font = pygame.font.SysFont(None, 50)

board = [['']*10 for i in range(10)]
test_board = [
    ['', '9', '', '2', '5', '', '6', '8', ''],
    ['', '', '5', '9', '1', '', '', '2', ''],
    ['', '4', '3', '', '8', '7', '9', '', '5'],
    ['4', '', '7', '1', '', '2', '5', '', '8'],
    ['', '8', '', '', '7', '', '', '3', '2'],
    ['9', '', '', '', '', '', '', '', '4'],
    ['3', '', '4', '8', '', '', '', '', ''],
    ['1', '5', '', '', '2', '', '3', '', ''],
    ['6', '', '', '', '', '5', '8', '', '1']
    ]

def draw_board(x=10, y=10):
    game_display.fill((30, 76, 115))
    for i in range(9):
        pygame.draw.line(game_display, (1, 36, 86), (0, i*50), (500, i*50), 3+3*(i%3==0))
        pygame.draw.line(game_display, (1, 36, 86), (i*50, 0), (i*50, 500), 3+3*(i%3==0))
    for row in range(9):
        for col in range(9):
            if row == x and col == y:
                box = pygame.Rect(col*50, row*50, 50, 50)
                pygame.draw.rect(game_display, (127, 127, 127), box)
            text = font.render(board[row][col], True, (204, 204, 204))
            text_rect = text.get_rect()
            text_rect.center = (col * 50 + 25, row * 50 + 25)
            game_display.blit(text, text_rect)

def solve_sudoku():
    row, col = find_empty_cell()

    if row is None:
        return True

    for num in map(str, range(1, 10)):
        if is_valid_move(row, col, num):
            board[row][col] = num
            if solve_sudoku():
                return True
            board[row][col] = ""

    return False

def find_empty_cell():
    for row in range(9):
        for col in range(9):
            if board[row][col] == "":
                return (row, col)
    return None, None

def is_valid_move(row, col, num):
    for i in range(9):
        if board[row][i] == num:
            return False

    for i in range(9):
        if board[i][col] == num:
            return False

    box_row = (row // 3) * 3
    box_col = (col // 3) * 3
    for i in range(box_row, box_row + 3):
        for j in range(box_col, box_col + 3):
            if board[i][j] == num:
                return False
    return True

draw_board()
running = True
while running:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False

        elif event.type == pygame.MOUSEBUTTONUP:
            # Get the position of the mouse click
            pos = pygame.mouse.get_pos()
            row = pos[1] // 50
            col = pos[0] // 50
            draw_board(row, col)
            pygame.display.flip()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                solve_sudoku()
            elif event.key == pygame.K_1:
                board[row][col] = "1"
            elif event.key == pygame.K_2:
                board[row][col] = "2"
            elif event.key == pygame.K_3:
                board[row][col] = "3"
            elif event.key == pygame.K_4:
                board[row][col] = "4"
            elif event.key == pygame.K_5:
                board[row][col] = "5"
            elif event.key == pygame.K_6:
                board[row][col] = "6"
            elif event.key == pygame.K_7:
                board[row][col] = "7"
            elif event.key == pygame.K_8:
                board[row][col] = "8"
            elif event.key == pygame.K_9:
                board[row][col] = "9"
            draw_board()
