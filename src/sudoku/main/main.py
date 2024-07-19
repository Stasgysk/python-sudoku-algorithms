import pygame
import random
import numpy
import sys
import time
import copy
from multiprocessing import Pool

sys.setrecursionlimit(2500)
pygame.font.init()
Window = pygame.display.set_mode((504, 504))
pygame.display.set_caption("Python Sudoku")

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

steps_dfs = 0
steps_bt = 0
steps_fc = 0


def clear_field(field):
    for i in range(field_size):
        for j in range(field_size):
            field[i][j] = 0
            sudoku_field_generated_positions[i][j] = 0
    return field


def draw_box(x, y):
    pygame.draw.rect(Window, (255, 0, 0), pygame.Rect(x * diff, y * diff, diff + 3, diff + 3), 4)


def show_start_screen():
    font2 = pygame.font.SysFont("comicsans", 40)
    text = font2.render("Choose mode to play", 1, (255, 0, 0))
    Window.blit(text, (75, 50))
    text = font2.render("(press 1 or 2)", 1, (255, 0, 0))
    Window.blit(text, (75, 100))
    text = font2.render("1: 9x9", 1, (255, 0, 0))
    Window.blit(text, (75, 150))
    text = font2.render("2: 4x4", 1, (255, 0, 0))
    Window.blit(text, (75, 200))
    pygame.display.update()


def show_game_solving_method():
    font2 = pygame.font.SysFont("comicsans", 40)
    Window.fill((0, 0, 0))
    text = font2.render("Choose mode to play", 1, (255, 0, 0))
    Window.blit(text, (75, 50))
    text = font2.render("(press 1-4)", 1, (255, 0, 0))
    Window.blit(text, (75, 100))
    text = font2.render("1: You are playing", 1, (255, 0, 0))
    Window.blit(text, (75, 150))
    text = font2.render("2: DFS", 1, (255, 0, 0))
    Window.blit(text, (75, 200))
    text = font2.render("3: Backtracking", 1, (255, 0, 0))
    Window.blit(text, (75, 250))
    text = font2.render("4: Forward Checking", 1, (255, 0, 0))
    Window.blit(text, (75, 300))
    text = font2.render("5: Compare all 3", 1, (255, 0, 0))
    Window.blit(text, (75, 350))
    pygame.display.update()


def show_time_elapsed(dfs, bt, fc):
    font2 = pygame.font.SysFont("comicsans", 40)
    dfs_time = "DFS: " + str(dfs)
    text = font2.render(dfs_time, 1, (255, 0, 0))
    Window.blit(text, (4, 50))
    bt_time = "BT: " + str(bt)
    text = font2.render(bt_time, 1, (255, 0, 0))
    Window.blit(text, (4, 100))
    fc_time = "FC: " + str(fc)
    text = font2.render(fc_time, 1, (255, 0, 0))
    Window.blit(text, (4, 150))
    pygame.display.update()


def show_field(field):
    Window.fill((0, 0, 0))
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
            return False
        if field[i][y] == val:
            return False
    div = 3
    if field_size != 9:
        div = 2
    xx = x // div
    yy = y // div
    start_x = xx * div
    start_y = yy * div
    start_x_plus = start_x + div
    start_y_plus = start_y + div
    for pos_x in range(start_x, start_x_plus):
        for pos_y in range(start_y, start_y_plus):
            if field[pos_x][pos_y] == val:
                return False
    return True


def is_solvable(field):
    for i in range(field_size):
        for j in range(field_size):
            if field[i][j] != 0:
                solvable = False
                max_value = 10
                if field_size != 9:
                    max_value = 5
                for val in range(1, max_value):
                    if is_input_valid(i, j, field, val):
                        solvable = True
                        break
                if not solvable:
                    return solvable
    return True


def generate_field(field):
    max_value = 8
    if field_size != 9:
        max_value = 3
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
                pos = random.randint(0, max_value)
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
        x = random.randint(0, max_value)
        y = random.randint(0, max_value)
        if field[x][y] != 0:
            field[x][y] = 0
        else:
            i -= 1
            continue
    for i in range(field_size):
        for j in range(field_size):
            if field[i][j] != 0:
                sudoku_field_generated_positions[i][j] = 1


def is_field_empty(field):
    for i in range(field_size):
        for j in range(field_size):
            if field[i][j] == 0:
                return True
    return False


def is_solved(field):
    for i in range(field_size-1, -1, -1):
        for j in range(field_size-1, -1, -1):
            if sudoku_field_generated_positions[i][j] != 1:
                number = field[i][j]
                field[i][j] = 0
                if not is_input_valid(i, j, field, number):
                    field[i][j] = number
                    return False
                else:
                    field[i][j] = number
    return True


def find_empty_cell(field):
    for i in range(field_size):
        for j in range(field_size):
            if field[i][j] == 0:
                return i, j
    return None, None


def if_show(field, show):
    if show is True:
        time.sleep(0.01)
        show_field(field)
        pygame.display.update()


def dfs(field, show):
    if_show(field, show)
    global steps_dfs
    steps_dfs += 1
    x, y = find_empty_cell(field)

    if x is None and y is None:
        return False

    highest = 10

    if field_size != 9:
        highest = 5

    # for number in range(1, highest):
    #     field[x][y] = number
    #     if not dfs(field, show):
    #         field[x][y] = 0
    #         if is_input_valid(x, y, field, number):
    #             field[x][y] = number
    #             return True
    #     else:
    #         if not dfs(field, show):
    #             field[x][y] = 0
    #             if is_input_valid(x, y, field, number):
    #                 field[x][y] = number
    #                 return True
    #             else:
    #                 return False
    #
    # if_show(field, show)
    # return True

    for number in range(1, highest):
        if_show(field, show)
        field[x][y] = number
        if is_field_empty(field):
            dfs(field, show)
        else:
            field[x][y] = 0
            if is_input_valid(x, y, field, number):
                field[x][y] = number
        if is_solved(field):
            return True
    if is_solved(field):
        return True
    else:
        field[x][y] = 0
    return False


def back_tracking(field, show):
    if_show(field, show)
    global steps_bt
    steps_bt += 1
    x, y = find_empty_cell(field)

    if x is None or y is None:
        return True

    highest = 10

    if field_size != 9:
        highest = 5

    for number in range(1, highest):
        if is_input_valid(x, y, field, number):
            field[x][y] = number

            if back_tracking(field, show):
                return True
            field[x][y] = 0
    return False


def is_input_valid_for_other_positions(x, y, field, max_value):
    for i in range(field_size):
        if field[x][i] != 0:
            continue
        flag = False
        for j in range(1, max_value):
            if is_input_valid(x, i, field, j):
                flag = True
                break
        if not flag:
            return False
    for i in range(field_size):
        if field[i][y] != 0:
            continue
        flag = False
        for j in range(1, max_value):
            if is_input_valid(i, y, field, j):
                flag = True
                break
        if not flag:
            return False
    return True


def forward_checking(field, show):
    if_show(field, show)
    global steps_fc
    steps_fc += 1
    x, y = find_empty_cell(field)

    if x is None and y is None:
        return True

    highest = 10

    if field_size != 9:
        highest = 5

    for number in range(1, highest):
        if is_input_valid(x, y, field, number):
            field[x][y] = number
            if is_input_valid_for_other_positions(x, y, field, highest):
                if forward_checking(field, show):
                    return True
            field[x][y] = 0
    return False


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
        if not is_field_empty(field):
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
            if event.type == pygame.QUIT:
                flag = False
                return

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

    flag = True

    show_game_solving_method()
    while flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                flag = False
                return
            if event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_1:
                        play_game(field)
                        flag = False
                    case pygame.K_2:
                        dfs(field, True)
                        flag = False
                    case pygame.K_3:
                        back_tracking(field, True)
                        flag = False
                    case pygame.K_4:
                        forward_checking(field, True)
                        flag = False
                    case pygame.K_5:
                        field1 = copy.deepcopy(field)
                        field2 = copy.deepcopy(field)
                        field3 = copy.deepcopy(field)

                        start_time1 = time.perf_counter()
                        dfs(field1, False)
                        end_time1 = time.perf_counter()
                        elapsed_time1 = end_time1 - start_time1
                        elapsed_time1 = "{:.10f}".format(elapsed_time1)
                        print("DFS:", elapsed_time1)

                        start_time2 = time.perf_counter()
                        back_tracking(field2, False)
                        end_time2 = time.perf_counter()
                        elapsed_time2 = end_time2 - start_time2
                        elapsed_time2 = "{:.10f}".format(elapsed_time2)
                        print("BT: ", elapsed_time2)

                        start_time3 = time.perf_counter()
                        forward_checking(field3, False)
                        end_time3 = time.perf_counter()
                        elapsed_time3 = end_time3 - start_time3
                        elapsed_time3 = "{:.10f}".format(elapsed_time3)
                        print("FC: ", elapsed_time3)

                        #Window.fill((0, 0, 0))
                        #show_time_elapsed(elapsed_time1, elapsed_time2, elapsed_time3)
                        flag = False

                        print(steps_dfs)
                        print(steps_bt)
                        print(steps_fc)

                        # for i in range(field_size):
                        #     print(field[i])
                        # print()
                        # for i in range(field_size):
                        #     print(field1[i])
                        print(is_solved(field1))
                        print(is_solved(field2))
                        print(is_solved(field3))
    flag = True
    while flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                flag = False
                return


if __name__ == "__main__":
    main()
