def print_state(towers):
    print(f"Поточний стан: {towers}")


def move_disk(towers, from_t, to_t):
    disk = towers[from_t].pop()
    towers[to_t].append(disk)
    print(f"Переміщуємо диск з {from_t} на {to_t}: {disk}")
    print_state(towers)


def hanoi(towers, n, from_t, to_t, tmp_t):
    if n == 1:
        move_disk(towers, from_t, to_t)
    else:
        hanoi(towers, n - 1, from_t, tmp_t, to_t)
        move_disk(towers, from_t, to_t)
        hanoi(towers, n - 1, tmp_t, to_t, from_t)


def solve_hanoi(n):
    towers = {'A': list(range(n, 0, -1)), 'B': [], 'C': []}
    print("Початковий стан:", towers)
    hanoi(towers, n, 'A', 'C', 'B')
    print("Кінцевий стан:", towers)


solve_hanoi(10)
