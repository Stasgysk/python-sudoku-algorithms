import pygame
import random
import numpy
import sys

sys.setrecursionlimit(2500)
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

# sudoku_field_9_x_9_static = [
#     [0, 0, 4, 0, 6, 0, 0, 0, 5],
#     [7, 8, 0, 4, 0, 0, 0, 2, 0],
#     [0, 0, 2, 6, 0, 1, 0, 7, 8],
#     [6, 1, 0, 0, 7, 5, 0, 0, 9],
#     [0, 0, 7, 5, 4, 0, 0, 6, 1],
#     [0, 0, 1, 7, 5, 0, 9, 3, 0],
#     [0, 7, 0, 3, 0, 0, 0, 1, 0],
#     [0, 4, 0, 2, 0, 6, 0, 0, 7],
#     [0, 2, 0, 0, 0, 7, 4, 0, 0],
# ]

sudoku_field_4_x_4 = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

font = pygame.font.SysFont("comicsans", 40)
font1 = pygame.font.SysFont("comicsans", 20)
diff = 500 / 9
field_size = 9


def clear_field(field):
    for i in range(field_size):
        for j in range(field_size):
            field[i][j] = 0
            sudoku_field_generated_positions[i][j] = 0
    return field


# def check_if_field_solved(field):
#     print("some shit")


# def if_field_solvable():
#     print("some")
def draw_box(x, y):
    pygame.draw.rect(Window, (255, 0, 0), pygame.Rect(x * diff, y * diff, diff + 3, diff + 3), 4)


def show_start_screen():
    text = font.render("Choose mode to play", 1, (255, 0, 0))
    Window.blit(text, (75, 50))
    text = font.render("(press 1 or 2)", 1, (255, 0, 0))
    Window.blit(text, (75, 100))
    text = font.render("1: 9x9", 1, (255, 0, 0))
    Window.blit(text, (75, 150))
    text = font.render("2: 4x4", 1, (255, 0, 0))
    Window.blit(text, (75, 200))
    pygame.display.update()


def show_field(field):
    for i in range(field_size):
        for j in range(field_size):
            pygame.draw.rect(Window, (255, 255, 0), (i * diff, j * diff, diff + 1, diff + 1))
            if field[i][j] != 0:
                if field_size == 9:
                    text1 = font.render(str(field[i][j]), 1, (255, 0, 0))
                    Window.blit(text1, (i * diff + 15, j * diff))
                else:
                    text1 = font.render(str(field[i][j]), 1, (255, 0, 0))
                    Window.blit(text1, (i * diff + 30, j * diff - 20))
    if field_size == 9:
        for i in range(10):
            if i % 3 == 0:
                thick = 7
            else:
                thick = 1
            pygame.draw.line(Window, (0, 0, 0), (0, i * diff), (500, i * diff), thick)
            pygame.draw.line(Window, (0, 0, 0), (i * diff, 0), (i * diff, 500), thick)
    else:
        for i in range(4):
            if i % 2 == 0:
                thick = 7
            else:
                thick = 1
            pygame.draw.line(Window, (0, 0, 0), (0, i * diff), (500, i * diff), thick)
            pygame.draw.line(Window, (0, 0, 0), (i * diff, 0), (i * diff, 500), thick)


def is_input_valid(x, y, field, val):
    if val == 0:
        return
    for i in range(field_size):
        if field[x][i] == val:
            # print('SSSS')
            return False
        if field[i][y] == val:
            # print('SSSS2')
            return False
    if field_size == 9:
        xx = x // 3
        yy = y // 3
        start_x = xx * 3
        start_y = yy * 3
        start_x_plus = start_x + 3
        start_y_plus = start_y + 3
    else:
        xx = x // 2
        yy = y // 2
        start_x = xx * 2
        start_y = yy * 2
        start_x_plus = start_x + 2
        start_y_plus = start_y + 2
        # print("XXXX: ", start_x, " ", start_x_plus, "YYYY: ", start_y, " ", start_y_plus)
        # print(start_y, " ", start_y_plus)
    for pos_x in range(start_x, start_x_plus):
        for pos_y in range(start_y, start_y_plus):
            if field[pos_x][pos_y] == val:
                # print("field: ", field[pos_x][pos_y])
                return False
    return True


def is_solvable(field):
    for i in range(field_size):
        for j in range(field_size):
            if field[i][j] != 0:
                solvable = False
                if field_size == 9:
                    for val in range(1, 9):
                        if is_input_valid(i, j, field, val):
                            solvable = True
                            break
                else:
                    for val in range(1, 4):
                        if is_input_valid(i, j, field, val):
                            solvable = True
                            break
                if not solvable:
                    return solvable
    return True


def generate_field(field):
    for i in range(field_size):
        for j in range(field_size):
            if field_size == 9:
                available_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            else:
                available_numbers = [1, 2, 3, 4]
            flag = True
            while flag:
                if not numpy.any(available_numbers):
                    clear_field(field)
                    generate_field(field)
                    return
                if field_size == 9:
                    pos = random.randint(0, 8)
                else:
                    pos = random.randint(0, 3)
                number = available_numbers[pos]
                available_numbers[pos] = 0
                if number == 0:
                    continue
                if is_input_valid(i, j, field, number):
                    field[i][j] = number
                    flag = False

    if field_size == 9:
        count = random.randint(45, 60)
    else:
        count = 15
    for i in range(count):
        if field_size == 9:
            x = random.randint(0, 8)
            y = random.randint(0, 8)
        else:
            x = random.randint(0, 3)
            y = random.randint(0, 3)
        if field[x][y] != 0:
            field[x][y] = 0
        else:
            i -= 1
            continue
    for i in range(field_size):
        for j in range(field_size):
            if field[i][j] != 0:
                sudoku_field_generated_positions[i][j] = 1
    # clear_field(field)
    # print(field_size)
    # if field_size == 9:
    #     count = random.randint(30, 50)
    # else:
    #     count = 5
    # for i in range(count):
    #     flag = True
    #     while flag:
    #         if field_size == 9:
    #             x = random.randint(0, 8)
    #             y = random.randint(0, 8)
    #         else:
    #             x = random.randint(0, 3)
    #             y = random.randint(0, 3)
    #         if field[x][y] != 0:
    #             continue
    #         else:
    #             if field_size == 9:
    #                 val = random.randint(1, 9)
    #             else:
    #                 val = random.randint(1, 4)
    #             if is_input_valid(x, y, field, val):
    #                 if not is_solvable(field):
    #                     clear_field(field)
    #                     generate_field(field)
    #                     return
    #                 flag = False
    #                 field[x][y] = val
    #                 sudoku_field_generated_positions[x][y] = 1


def is_solved(field):
    for i in range(field_size):
        for j in range(field_size):
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
                        if field_size == 9:
                            if x != 8:
                                x += 1
                        else:
                            if x != 3:
                                x += 1
                    case pygame.K_UP:
                        if y != 0:
                            y -= 1
                    case pygame.K_DOWN:
                        if field_size == 9:
                            if y != 8:
                                y += 1
                        else:
                            if y != 3:
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
                        if sudoku_field_generated_positions[x][y] != 1:
                            field[x][y] = 0
                    case pygame.K_RETURN:
                        generate_field(field)
        if field_size != 9 and val >= 5:
            val = 0
        if is_input_valid(x, y, field, val) and sudoku_field_generated_positions[x][y] != 1:
            field[x][y] = val
        show_field(field)
        draw_box(x, y)
        pygame.display.update()
        if is_solved(field):
            break
    pygame.quit()


def main():
    show_start_screen()
    flag = True
    field_type = -1
    while flag:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_1:
                        field_type = 1
                        flag = False
                    case pygame.K_2:
                        field_type = 2
                        flag = False
    if field_type == 2:
        global diff
        diff = 500 / 4
        global field_size
        field_size = 4
        global font
        global font1
        font = pygame.font.SysFont("comicsans", 120)
        font1 = pygame.font.SysFont("comicsans", 100)
        field = sudoku_field_4_x_4
    else:
        field = sudoku_field_9_x_9
    Window.fill((255, 182, 193))
    clear_field(field)
    generate_field(field)
    play_game(field)

    input('Press Enter to exit')


if __name__ == "__main__":
    main()
