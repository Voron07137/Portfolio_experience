def labyrinth(mat):
    for i in range(len(mat)):
        for j in range(len(mat)):
            if mat[i][j] == 1:
                mat[i][j] = -1

    count = 1
    mat[1][1] = -2
    if mat[2][1] == 0:
        mat[2][1] = count
    if mat[1][2] == 0:
        mat[1][2] = count

    while mat[10][10] == 0:
        for i in range(1, len(mat) - 1):
            for j in range(1, len(mat) - 1):
                next_count = count + 1
                if mat[i][j] == count:
                    if mat[i + 1][j] == 0:
                        mat[i + 1][j] = next_count
                    if mat[i][j + 1] == 0:
                        mat[i][j + 1] = next_count
                    if mat[i - 1][j] == 0:
                        mat[i - 1][j] = next_count
                    if mat[i][j - 1] == 0:
                        mat[i][j - 1] = next_count
        count += 1
    mat[1][1] = 0

    res = [count]
    route_reverse = ''

    i = 10
    j = 10
    while count != 0:
        prev_count = count - 1
        if mat[i + 1][j] == prev_count:
            route_reverse += 'N'
            i += 1
        if mat[i][j + 1] == prev_count:
            route_reverse += 'W'
            j += 1
        if mat[i - 1][j] == prev_count:
            route_reverse += 'S'
            i -= 1
        if mat[i][j - 1] == prev_count:
            route_reverse += 'E'
            j -= 1
        count -= 1

    directions = list(route_reverse)
    route = ''.join(directions[::-1])

    res.append(route)

    return res


matrix = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1],
    [1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]
print(labyrinth(matrix))  # [18, 'SSSSSEESEEESEEEESS']

matrix = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
print(labyrinth(matrix))  # [58, 'SSSSSSSSSEENNNNNNNNNEESSSSSSSSSEENNNNNNNNNEEESSWSSESSWSSES']

matrix = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
print(labyrinth(matrix))  # [18, 'EEEEEEEEESSSSSSSSS']
