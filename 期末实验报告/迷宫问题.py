import time
from copy import deepcopy


class Labyrinth:
    def __init__(self, matrix, begin, end):
        """
        定义迷宫类
        :param matrix: 迷宫的矩阵
        """
        self.end = end
        self.begin = begin
        self.matrix = matrix
        self.direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        self.result_stack = []
        self.result_queue = []
        self.result_recursion = []

    def run_stack(self):
        """
        栈
        :return:
        """
        matrix = deepcopy(self.matrix)
        res = [self.begin]

        while res[-1] != self.end:
            next_step_list = []
            for i in self.direction:
                next_step = [i + j for i, j in zip(res[-1], i)]
                if matrix[next_step[0]][next_step[1]] == 0:
                    next_step_list.append(next_step)
            if next_step_list is None:
                matrix[res[-1][0]][res[-1][1]] = -1
                res.pop()
            else:
                res.append(next_step_list[0])
            if res is None:
                break

        self.result_stack = res

    def run_queue(self):
        """
        队列
        :return:
        """
        matrix = deepcopy(self.matrix)
        res = [[self.begin]]
        flg = True

        while flg:
            for re in res:
                next_step_list = []
                re_i = re.copy()
                re_j = re.copy()
                for i in self.direction:
                    next_step = [i + j for i, j in zip(re[-1], i)]
                    if matrix[next_step[0]][next_step[1]] == 0:
                        matrix[next_step[0]][next_step[1]] = -1
                        next_step_list.append(next_step)
                for j in next_step_list:
                    re_i.append(j)
                    res.append(re_i)
                    re_i = re_j
                if len(res) > 1:
                    res.remove(re)
                if re[-1] == self.end:
                    flg = False
        self.result_queue = res

    def run_recursion(self):
        """
        递归
        :return:
        """
        self.result_recursion = []
        def main(x, y, path, final_xy, mg):
            path = path.copy()
            if is_final(x, y, final_xy):
                self.result_recursion.append(path.copy())
            else:
                xy_next_list = find_next_path(x, y, mg, path)
                if xy_next_list:
                    path.append([x, y])
                    c = 0
                    for xi, yi in xy_next_list:
                        c += 1
                        main(xi, yi, path, final_xy, mg)
                else:
                    pass

        def find_next_path(x, y, mg, path):
            xyi_list = []
            for i, j in zip([-1, 0, 1, 0], [0, 1, 0, -1]):
                xi = x - i
                yi = y - j
                if mg[xi][yi] == 0 and [xi, yi] not in path:
                    xyi_list.append([xi, yi])
            return xyi_list

        def is_final(x, y, final_xy):
            if x == final_xy[0] and y == final_xy[1]:
                return True
            return False

        main(self.begin[0], self.begin[1], [], self.end, deepcopy(self.matrix))

    def show_res(self):
        self.run_recursion()
        self.run_queue()
        self.run_stack()

        print(f"使用栈算出的迷宫路径为:{self.result_stack}")
        print(f"使用队列算出的迷宫路径为:{self.result_queue}")
        print(f"使用递归算出的迷宫路径为:{self.result_recursion}")


if __name__ == '__main__':
    maze = [[1, 1, 1, 1, 1],
            [1, 0, 1, 1, 1],
            [1, 1, 0, 0, 1],
            [1, 1, 1, 0, 1],
            [1, 1, 1, 1, 1]]

    L = Labyrinth(maze, [1, 1], [3, 3])
    t = time.time()
    for i in range(1000000):
        L.run_recursion()
    t = time.time() - t
    print(t)


