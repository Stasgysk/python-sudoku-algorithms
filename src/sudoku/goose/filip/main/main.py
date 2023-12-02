import pygame

pygame.font.init()
Window = pygame.display.set_mode((500, 500))
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
x = 0
z = 0
diff = 500 / 9
value = 0


def check_if_field_solved(field):
    print("some shit")


def if_field_solvable():
    print("some")


def if_solved():
    print("some")


def generate_field():
    print("some shit")


def solve_field():
    print("some shit")


def dfs():
    print("some shit")


def play_game():
    print("some shit")


def show_field(field):
    for i in range(9):
        for j in range(9):
            pygame.draw.rect(Window, (255, 255, 0), (i * diff, j * diff, diff + 1, diff + 1))
            text1 = font.render(str(field[i][j]), 1, (255, 0, 0))
            Window.blit(text1, (i * diff + 15, j * diff))
    for i in range(10):
        if i % 3 == 0:
            thick = 7
        else:
            thick = 1
        pygame.draw.line(Window, (0, 0, 0), (0, i * diff), (500, i * diff), thick)
        pygame.draw.line(Window, (0, 0, 0), (i * diff, 0), (i * diff, 500), thick)


def main():
    Window.fill((255, 182, 193))
    pygame.event.pump()
    show_field(sudoku_field_9_x_9_static)
    pygame.display.update()
    print("Starting game...")
    print("Generating sudoku field...")
    print("Trying to solve...")
    print("Some...")

    input('Press Enter to exit')


if __name__ == "__main__":
    main()
