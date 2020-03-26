from random import shuffle, randint


def solve(sb):
    valid_num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    coordinate = [0, 0]
    if sb.find_empty_space(coordinate):
        return True
    else:
        row = coordinate[0]
        col = coordinate[1]
        shuffle(valid_num)
        for num in valid_num:
            if validate(sb, row, col, num):
                sb.set_value(row, col, num)
                if sb.find_empty_space([0, 0]):
                    return True
                elif solve(sb):
                    return True
    sb.set_value(row, col, 0)
    return False


def validate(sb, row, col, num):
    if sb.num_in_row(row, col, num):
        return False
    elif sb.num_in_col(row, col, num):
        return False
    elif sb.num_in_square(row, col, num):
        return False
    else:
        return True


def solved_check(sb):
    for row in range(0, 9):
        for col in range(0, 9):
            if sb.grid[row][col] == 0 or not validate(sb, row, col, sb.grid[row][col]):
                return False
    sb.unsolved = False
    return True


def flip_point(x1, y1):
    return 8-x1, 8-y1


def removal(sb, difficulty):
    if difficulty == 0:
        total_remove = randint(1, 2)
    elif difficulty == 1:
        total_remove = randint(19, 20)
    else:
        total_remove = randint(21, 22)
    cds = []
    for x in range(0, 5):
        for y in range(0, 9):
            if x == 5 and y == 5:
                break
            cds.append((x, y))
    shuffle(cds)
    for i in range(0, total_remove):
        x1, y1 = cds.pop()
        x2, y2 = flip_point(x1, y1)
        sb.set_value(x1, y1, 0)
        sb.set_value(x2, y2, 0)
