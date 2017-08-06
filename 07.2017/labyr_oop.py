class Labyrinth:
    def __init__(self, mat, begin, end):
        self.matrix = mat
        self.action(begin, end)

    def init_walls(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] == 1:
                    self.matrix[i][j] = -1

    def check_border_down(self, index):
        if index + 1 >= len(self.matrix):
            return False
        else:
            return True

    def check_border_right(self, index, j_index):
        if j_index + 1 >= len(self.matrix[index]):
            return False
        else:
            return True

    def check_border_up_left(self, index):
        if index - 1 < 0:
            return False
        else:
            return True

    def action(self, begin, end):
        self.init_walls()
        i = begin[0]
        j = begin[1]
        if begin[0] == end[0] and begin[1] == end[1]:
            print("0")
        else:
            count = 1
            self.matrix[i][j] = -2
            if self.check_border_down(i):
                if self.matrix[i + 1][j] == 0:
                    self.matrix[i + 1][j] = count
            if self.check_border_right(i, j):
                if self.matrix[i][j + 1] == 0:
                    self.matrix[i][j + 1] = count
            if self.check_border_up_left(i):
                if self.matrix[i - 1][j] == 0:
                    self.matrix[i - 1][j] = count
            if self.check_border_up_left(j):
                if self.matrix[i][j - 1] == 0:
                    self.matrix[i][j - 1] = count
            while self.matrix[end[0]][end[1]] == 0:
                for i in range(0, len(self.matrix)):
                    for j in range(0, len(self.matrix[i])):
                        next_count = count + 1
                        if self.matrix[i][j] == count:
                            if self.check_border_down(i):
                                if self.matrix[i + 1][j] == 0:
                                    self.matrix[i + 1][j] = next_count
                            if self.check_border_right(i, j):
                                if self.matrix[i][j + 1] == 0:
                                    self.matrix[i][j + 1] = next_count
                            if self.check_border_up_left(i):
                                if self.matrix[i - 1][j] == 0:
                                    self.matrix[i - 1][j] = next_count
                            if self.check_border_up_left(j):
                                if self.matrix[i][j - 1] == 0:
                                    self.matrix[i][j - 1] = next_count
                count += 1
            self.matrix[begin[0]][begin[1]] = 0
            res = [count]
            route_reverse = ''
            i = end[0]
            j = end[1]
            while count != 0:
                prev_count = count - 1
                if self.check_border_down(i):
                    if self.matrix[i + 1][j] == prev_count:
                        route_reverse += 'N'
                        i += 1
                if self.check_border_right(i, j):
                    if self.matrix[i][j + 1] == prev_count:
                        route_reverse += 'W'
                        j += 1
                if self.check_border_up_left(i):
                    if self.matrix[i - 1][j] == prev_count:
                        route_reverse += 'S'
                        i -= 1
                if self.check_border_up_left(j):
                    if self.matrix[i][j - 1] == prev_count:
                        route_reverse += 'E'
                        j -= 1
                count -= 1
            directions = list(route_reverse)
            route = ''.join(directions[::-1])
            res.append(route)
            print(str(res))


matrix1 = Labyrinth([
    [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
], [0, 0], [11, 11])  # [62, 'ESSSSSSSSSSEENNNNNNNNNEESSSSSSSSSEENNNNNNNNNEEESSWSSESSWSSESES']

matrix2 = Labyrinth([
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
], [1, 1], [10, 10])  # [18, 'SSSSSEESEEESEEEESS']

matrix3 = Labyrinth([
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
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
], [1, 1], [12, 11])  # [21, 'EEEEEEEEESSSSSSSSSSES']
