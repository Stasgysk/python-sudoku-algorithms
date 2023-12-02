import pygame
import random

pygame.font.init()
Window = pygame.display.set_mode((504, 504))
pygame.display.set_caption("Goose and Filip sudoku masters ;)")

sudoku_field_9_x_9 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

sudoku_field_generated_positions = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

sudoku_field_9_x_9_static = [
    [0, 0, 4, 0, 6, 0, 0, 0, 5],
    [7, 8, 0, 4, 0, 0, 0, 2, 0],
    [0, 0, 2, 6, 0, 1, 0, 7, 8],
    [6, 1, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 7, 5, 4, 0, 0, 6, 1],
    [0, 0, 1, 7, 5, 0, 9, 3, 0],
    [0, 7, 0, 3, 0, 0, 0, 1, 0],
    [0, 4, 0, 2, 0, 6, 0, 0, 7],
    [0, 2, 0, 0, 0, 7, 4, 0, 0],
]

sudoku_field_4_x_4 = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

font = pygame.font.SysFont("comicsans", 40)
font1 = pygame.font.SysFont("comicsans", 20)
diff = 500 / 9
value = 0

def clear_field(field):
    for i in range(9):
        for j in range(9):
            field[i][j] = 0
    return field

# def check_if_field_solved(field):
#     print("some shit")


# def if_field_solvable():
#     print("some")
def draw_box(x, y):
    pygame.draw.rect(Window, (255, 0, 0), pygame.Rect(x * diff, y * diff, diff + 3, diff + 3), 4)


def show_field(field):
    for i in range(9):
        for j in range(9):
            pygame.draw.rect(Window, (255, 255, 0), (i * diff, j * diff, diff + 1, diff + 1))
            if field[i][j] != 0:
                text1 = font.render(str(field[i][j]), 1, (255, 0, 0))
                Window.blit(text1, (i * diff + 15, j * diff))
    for i in range(10):
        if i % 3 == 0:
            thick = 7
        else:
            thick = 1
        pygame.draw.line(Window, (0, 0, 0), (0, i * diff), (500, i * diff), thick)
        pygame.draw.line(Window, (0, 0, 0), (i * diff, 0), (i * diff, 500), thick)


def is_input_valid(x, y, field, val):
    for i in range(9):
        if field[x][i] == val:
            return False
        if field[i][y] == val:
            return False
    xx = x // 3
    yy = y // 3
    start_x = xx * 3
    start_y = yy * 3
    for pos_x in range(start_x, start_x + 3):
        for pos_y in range(start_y, start_y + 3):
            if field[pos_x][pos_y] == val:
                return False
    return True


def is_solvable(field):
    for i in range(9):
        for j in range(9):
            if field[i][j] != 0:
                solvable = False
                for val in range(1, 8):
                    if is_input_valid(i, j, field, val):
                        solvable = True
                        break
                if not solvable:
                    return solvable
    return True


def generate_field(field):
    clear_field(field)
    count = random.randint(30, 50)
    for i in range(count):
        flag = True
        while flag:
            x = random.randint(0, 8)
            y = random.randint(0, 8)
            if field[x][y] != 0:
                continue
            else:
                val = random.randint(1, 9)
                if is_input_valid(x, y, field, val):
                    if not is_solvable(field):
                        clear_field(field)
                        generate_field(field)
                        return
                    flag = False
                    field[x][y] = val
                    sudoku_field_generated_positions[x][y] = 1


def is_solved(field):
    for i in range(9):
        for j in range(9):
            if field[i][j] == 0:
                return False
    return True


def dfs():
    print("some shit")


def play_game(field):
    x = 0
    y = 0
    val = 0
    Window.fill((255, 182, 193))
    show_field(field)

    flag = True

    while flag:
        val = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                flag = False
            if event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_LEFT:
                        if x != 0:
                            x -= 1
                    case pygame.K_RIGHT:
                        if x != 8:
                            x += 1
                    case pygame.K_UP:
                        if y != 0:
                            y -= 1
                    case pygame.K_DOWN:
                        if y != 8:
                            y += 1
                    case pygame.K_1:
                        val = 1
                    case pygame.K_2:
                        val = 2
                    case pygame.K_3:
                        val = 3
                    case pygame.K_4:
                        val = 4
                    case pygame.K_5:
                        val = 5
                    case pygame.K_6:
                        val = 6
                    case pygame.K_7:
                        val = 7
                    case pygame.K_8:
                        val = 8
                    case pygame.K_9:
                        val = 9
                    case pygame.K_BACKSPACE:
                        field[x][y] = 0
                    case pygame.K_RETURN:
                        generate_field(field)
        if is_input_valid(x, y, field, val) and sudoku_field_generated_positions[x][y] != 1:
            field[x][y] = val
        show_field(field)
        draw_box(x, y)
        pygame.display.update()
        if is_solved(field):
            break
    pygame.quit()


def main():
    field = sudoku_field_9_x_9
    Window.fill((255, 182, 193))
    generate_field(field)
    play_game(field)
    print("Starting game...")
    print("Generating sudoku field...")
    print("Trying to solve...")
    print("Some...")

    input('Press Enter to exit')


if __name__ == "__main__":
    main()
