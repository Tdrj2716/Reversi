from random import random
import subprocess
from time import time
from random import randint, random
from tqdm import trange
from math import exp, log, sqrt

start_temp = 20
end_temp = 0.01

def tempera(strt, now, tl):
    x = (now - strt) / tl
    return pow(start_temp, 1 - x) * pow(end_temp, x)
    #return start_temp + (end_tmp - start_temp) * (now - strt) / tl

def prob(p_score, n_score, strt, now, tl):
    dis = n_score - p_score
    if dis >= 0.0:
        return 1.0
    return exp(dis / tempera(strt, now, tl))

pattern_num = 5
index_num = 38
param_num = 92

base_param = []
with open('param_base.txt', 'r') as f:
    for _ in range(param_num):
        base_param.append(float(f.readline()))

'''
translate_raw = [
    [0, 1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14, 15], [16, 17, 18, 19, 20, 21, 22, 23], [24, 25, 26, 27, 28, 29, 30, 31], [32, 33, 34, 35, 36, 37, 38, 39], [40, 41, 42, 43, 44, 45, 46, 47], [48, 49, 50, 51, 52, 53, 54, 55], [56, 57, 58, 59, 60, 61, 62, 63], 
    [0, 8, 16, 24, 32, 40, 48, 56], [1, 9, 17, 25, 33, 41, 49, 57], [2, 10, 18, 26, 34, 42, 50, 58], [3, 11, 19, 27, 35, 43, 51, 59], [4, 12, 20, 28, 36, 44, 52, 60], [5, 13, 21, 29, 37, 45, 53, 61], [6, 14, 22, 30, 38, 46, 54, 62], [7, 15, 23, 31, 39, 47, 55, 63], 
    [5, 14, 23], [4, 13, 22, 31], [3, 12, 21, 30, 39], [2, 11, 20, 29, 38, 47], [1, 10, 19, 28, 37, 46, 55], [0, 9, 18, 27, 36, 45, 54, 63], [8, 17, 26, 35, 44, 53, 62], [16, 25, 34, 43, 52, 61], [24, 33, 42, 51, 60], [32, 41, 50, 59], [40, 49, 58], 
    [2, 9, 16], [3, 10, 17, 24], [4, 11, 18, 25, 32], [5, 12, 19, 26, 33, 40], [6, 13, 20, 27, 34, 41, 48], [7, 14, 21, 28, 35, 42, 49, 56], [15, 22, 29, 36, 43, 50, 57], [23, 30, 37, 44, 51, 58], [31, 38, 45, 52, 59], [39, 46, 53, 60], [47, 54, 61]
]
same_param = [0, 1, 2, 3, 3, 2, 1, 0, 0, 1, 2, 3, 3, 2, 1, 0, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4]
'''
translate = []
eval_translate = []
each_param_num = []

edgex1 = [
    [54, 63, 62, 61, 60, 59, 58, 57, 56, 49],
    [49, 56, 48, 40, 32, 24, 16, 8, 0, 9],
    [9, 0, 1, 2, 3, 4, 5, 6, 7, 14],
    [14, 7, 15, 23, 31, 39, 47, 55, 63, 54]
]

edgex2 = []
for arr in edgex1:
    edgex2.append(arr)
    edgex2.append(list(reversed(arr)))
translate.append(edgex2)
eval_translate.append(edgex1)
each_param_num.append(3 ** 10)

corner1= [
    [3, 2, 1, 0, 9, 8, 16, 24],
    [4, 5, 6, 7, 14, 15, 23, 31],
    [60, 61, 62, 63, 54, 55, 47, 39],
    [59, 58, 57, 56, 49, 48, 40, 32]
]

corner2 = [
    [3, 2, 1, 0, 9, 8, 16, 24],
    [24, 16, 8, 0, 9, 1, 2, 3],
    [4, 5, 6, 7, 14, 15, 23, 31],
    [31, 23, 15, 7, 14, 6, 5, 4],
    [60, 61, 62, 63, 54, 55, 47, 39],
    [39, 47, 55, 63, 54, 62, 61, 60],
    [59, 58, 57, 56, 49, 48, 40, 32],
    [32, 40, 48, 56, 49, 57, 58, 59]
]

translate.append(corner2)
eval_translate.append(corner1)
each_param_num.append(3 ** 8)

corner24 = [
    [0, 1, 2, 3, 8, 9, 10, 11],
    [0, 8, 16, 24, 1, 9, 17, 25],
    [7, 6, 5, 4, 15, 14, 13, 12],
    [7, 15, 23, 31, 6, 14, 22, 30],
    [63, 62, 61, 60, 55, 54, 53, 52],
    [63, 55, 47, 39, 62, 54, 46, 38],
    [56, 57, 58, 59, 48, 49, 50, 51],
    [56, 48, 40, 32, 57, 49, 41, 33]
]

translate.append(corner24)
eval_translate.append(corner24)
each_param_num.append(3 ** 8)

diagonal1 = [
    [0, 9, 18, 27, 36, 45, 54, 63],
    [7, 14, 21, 28, 35, 42, 49, 56]
]

diagonal2 = []
for arr in diagonal1:
    diagonal2.append(arr)
    diagonal2.append(list(reversed(arr)))
translate.append(diagonal2)
eval_translate.append(diagonal1)
each_param_num.append(3 ** 8)

edge1 = [
    [0, 1, 2, 3, 4, 5, 6, 7],
    [7, 15, 23, 31, 39, 47, 55, 63],
    [63, 62, 61, 60, 59, 58, 57, 56],
    [56, 48, 40, 32, 24, 26, 8, 0]
]

edge2 = []
for arr in edge1:
    edge2.append(arr)
    edge2.append(list(reversed(arr)))
translate.append(edge2)
eval_translate.append(edge1)
each_param_num.append(3 ** 8)

'''
diagonal1 = [
    [0, 9, 18, 27, 36, 45, 54, 63],
    [7, 14, 21, 28, 35, 42, 49, 56]
]
diagonal2 = []
for arr in diagonal1:
    diagonal2.append(arr)
    diagonal2.append(list(reversed(arr)))
translate.append(diagonal2)
eval_translate.append(diagonal1)
each_param_num.append(3 ** 8)
'''

win_num = [[0 for _ in range(each_param_num[i])] for i in range(pattern_num)]
seen_num = [[0 for _ in range(each_param_num[i])] for i in range(pattern_num)]
ans = [[0 for _ in range(each_param_num[i])] for i in range(pattern_num)]
weight = [[1.0 for _ in range(3)] for _ in range(pattern_num)]
'''
with open('param_pattern.txt', 'r') as f:
    for i in range(pattern_num):
        for j in range(each_param_num[i]):
            ans[i][j] = float(f.readline())
'''
seen_grid = []


hw = 8
hw2 = 64
dy = [0, 1, 0, -1, 1, 1, -1, -1]
dx = [1, 0, -1, 0, 1, -1, 1, -1]

def empty(grid, y, x):
    return grid[y][x] == -1 or grid[y][x] == 2

def inside(y, x):
    return 0 <= y < hw and 0 <= x < hw

def check(grid, player, y, x):
    res_grid = [[False for _ in range(hw)] for _ in range(hw)]
    res = 0
    for dr in range(8):
        ny = y + dy[dr]
        nx = x + dx[dr]
        if not inside(ny, nx):
            continue
        if empty(grid, ny, nx):
            continue
        if grid[ny][nx] == player:
            continue
        #print(y, x, dr, ny, nx)
        plus = 0
        flag = False
        for d in range(hw):
            nny = ny + d * dy[dr]
            nnx = nx + d * dx[dr]
            if not inside(nny, nnx):
                break
            if empty(grid, nny, nnx):
                break
            if grid[nny][nnx] == player:
                flag = True
                break
            #print(y, x, dr, nny, nnx)
            plus += 1
        if flag:
            res += plus
            for d in range(plus):
                nny = ny + d * dy[dr]
                nnx = nx + d * dx[dr]
                res_grid[nny][nnx] = True
    return res, res_grid

class reversi:
    def __init__(self):
        self.grid = [[-1 for _ in range(hw)] for _ in range(hw)]
        self.grid[3][3] = 1
        self.grid[3][4] = 0
        self.grid[4][3] = 0
        self.grid[4][4] = 1
        self.player = 0 # 0: 黒 1: 白
        self.nums = [2, 2]

    def move(self, y, x):
        plus, plus_grid = check(self.grid, self.player, y, x)
        if (not empty(self.grid, y, x)) or (not inside(y, x)) or not plus:
            print('Please input a correct move')
            return 1
        self.grid[y][x] = self.player
        for ny in range(hw):
            for nx in range(hw):
                if plus_grid[ny][nx]:
                    self.grid[ny][nx] = self.player
        self.nums[self.player] += 1 + plus
        self.nums[1 - self.player] -= plus
        self.player = 1 - self.player
        return 0
    
    def check_pass(self):
        for y in range(hw):
            for x in range(hw):
                if self.grid[y][x] == 2:
                    self.grid[y][x] = -1
        res = True
        for y in range(hw):
            for x in range(hw):
                if not empty(self.grid, y, x):
                    continue
                plus, _ = check(self.grid, self.player, y, x)
                if plus:
                    res = False
                    self.grid[y][x] = 2
        if res:
            #print('Pass!')
            self.player = 1 - self.player
        return res

    def output(self):
        print('  ', end='')
        for i in range(hw):
            print(chr(ord('a') + i), end=' ')
        print('')
        for y in range(hw):
            print(str(y + 1) + ' ', end='')
            for x in range(hw):
                print('○' if self.grid[y][x] == 0 else '●' if self.grid[y][x] == 1 else '* ' if self.grid[y][x] == 2 else '. ', end='')
            print('')
    
    def output_file(self):
        res = ''
        for y in range(hw):
            for x in range(hw):
                res += '*' if self.grid[y][x] == 0 else 'O' if self.grid[y][x] == 1 else '-'
        res += ' *'
        return res

    def end(self):
        if min(self.nums) == 0:
            return True
        res = True
        for y in range(hw):
            for x in range(hw):
                if self.grid[y][x] == -1 or self.grid[y][x] == 2:
                    res = False
        return res
    
    def judge(self):
        if self.nums[0] > self.nums[1]:
            #print('Black won!', self.nums[0], '-', self.nums[1])
            return 0
        elif self.nums[1] > self.nums[0]:
            #print('White won!', self.nums[0], '-', self.nums[1])
            return 1
        else:
            #print('Draw!', self.nums[0], '-', self.nums[1])
            return -1

def translate_p(grid, arr):
    res = []
    for i in range(len(arr)):
        tmp = 0
        for j in reversed(range(len(arr[i]))):
            tmp *= 3
            tmp2 = grid[arr[i][j] // hw][arr[i][j] % hw]
            if tmp2 == 0:
                tmp += 1
            elif tmp2 == 1:
                tmp += 2
        res.append(tmp)
    return res

def translate_o(grid, arr):
    res = []
    for i in range(len(arr)):
        tmp = 0
        for j in reversed(range(len(arr[i]))):
            tmp *= 3
            tmp2 = grid[arr[i][j] // hw][arr[i][j] % hw]
            if tmp2 == 1:
                tmp += 1
            elif tmp2 == 0:
                tmp += 2
        res.append(tmp)
    return res

def collect(s):
    global seen_grid
    grids = []
    rv = reversi()
    idx = 2
    while True:
        if rv.check_pass() and rv.check_pass():
            break
        turn = 0 if s[idx] == '+' else 1
        x = ord(s[idx + 1]) - ord('a')
        y = int(s[idx + 2]) - 1
        idx += 3
        if rv.move(y, x):
            print('error')
            break
        grids.append([[i for i in j] for j in rv.grid])
        if rv.end():
            break
    rv.check_pass()
    #rv.output()
    #print(rv.nums[0], rv.nums[1])
    seen_grid.append([])
    #winner = rv.judge()
    score = 2.0 / (1.0 + exp(-(rv.nums[0] - rv.nums[1]) / 5)) - 1.0
    for turn, grid in enumerate(grids):
        tmp = [score, (turn + 4) / 64]
        for i in range(pattern_num):
            tmp.append(translate_p(grid, eval_translate[i]))
            for j in translate_p(grid, translate[i]):
                seen_num[i][j] += 1
                win_num[i][j] += tmp[0]
            for j in translate_o(grid, translate[i]):
                seen_num[i][j] += 1
                win_num[i][j] -= tmp[0]
        seen_grid[-1].append(tmp)
'''

def collect():
    global seen_grid
    with open('param0.txt', 'w') as f:
        for i in range(param_num):
            f.write(str(base_param[i] + random() * 0.4 - 0.2) + '\n')
    with open('param1.txt', 'w') as f:
        for i in range(param_num):
            f.write(str(base_param[i] + random() * 0.4 - 0.2) + '\n')
    ai = [subprocess.Popen(('./a.exe param' + str(i) + '.txt').split(), stdin=subprocess.PIPE, stdout=subprocess.PIPE) for i in range(2)]
    for i in range(2):
        ai[i].stdin.write((str(i) + '\n' + '100' + '\n').encode('utf-8'))
        ai[i].stdin.flush()
    grids = []
    rv = reversi()
    idx = 2
    while True:
        if rv.check_pass() and rv.check_pass():
            break
        stdin = ''
        for y in range(hw):
            for x in range(hw):
                stdin += str(rv.grid[y][x]) + ' '
            stdin += '\n'
        ai[rv.player].stdin.write(stdin.encode('utf-8'))
        ai[rv.player].stdin.flush()
        y, x, val = [float(i) for i in ai[rv.player].stdout.readline().decode().strip().split()]
        y = int(y)
        x = int(x)
        if rv.move(y, x):
            print('error')
            for i in range(2):
                ai[i].kill()
            return
        grids.append([val / 4 if rv.player == 0 else -val / 4, [[i for i in j] for j in rv.grid]])
        if rv.end():
            break
    for i in range(2):
        ai[i].kill()
    rv.check_pass()
    #rv.output()
    #print(rv.nums[0], rv.nums[1])
    seen_grid.append([])
    #winner = rv.judge()
    score = 2.0 / (1.0 + exp(-(rv.nums[0] - rv.nums[1]) / 5)) - 1.0
    for turn in range(len(grids)):
        if turn + 25 < len(grids):
            val = grids[turn + 25][0]
        else:
            val = score * turn / len(grids)
        grid = grids[turn][1]
        tmp = [score * turn / len(grids)]
        for i in range(pattern_num):
            tmp.append(translate_p(grid, eval_translate[i]))
            for j in translate_p(grid, translate[i]):
                seen_num[i][j] += 1
                win_num[i][j] += val
            for j in translate_o(grid, translate[i]):
                seen_num[i][j] += 1
                win_num[i][j] -= val
        seen_grid[-1].append(tmp)
'''

def calc_weight(idx, x):
    x1 = 4.0 / 64
    x2 = 32.0 / 64
    x3 = 64.0 / 64
    y1, y2, y3 = weight[idx]
    a = ((y1 - y2) * (x1 - x3) - (y1 - y3) * (x1 - x2)) / ((x1 - x2) * (x1 - x3) * (x2 - x3))
    b = (y1 - y2) / (x1 - x2) - a * (x1 + x2)
    c = y1 - a * x1 * x1 - b * x1
    return a * x * x + b * x + c

def scoring():
    res = 0.0
    cnt = 0
    for game in range(len(seen_grid)):
        for turn, arr in enumerate(seen_grid[game]):
            cnt += 1
            result = arr[0]
            val = 0.0
            for i in range(pattern_num):
                tmp = 0.0
                for j in arr[i + 2]:
                    tmp += ans[i][j]
                val += tmp * calc_weight(i, arr[1])
            res += (val - result) ** 2
            '''
            if val * result < 0.0:
                res += abs(val - result)
            else:
                res += abs(val - result) * 0.5
            '''
            '''
            #res *= pow(val, result) * pow(1 - val, 1 - result) # * 0.01 + 0.99
            if val != 0.0:
                res += result * log(val)
            if 1.0 - val != 0.0:
                res += (1.0 - result) * log(1.0 - val)
            '''
    return res / cnt

def anneal1(tl):
    global ans, start_temp, end_temp
    score = scoring()
    print('anneal1')
    print(score)
    strt = time()
    cnt = 0
    while time() - strt < tl:
        idx1 = randint(0, pattern_num - 1)
        idx2 = randint(0, 2)
        f_weight = weight[idx1][idx2]
        weight[idx1][idx2] += random() - 0.5
        n_score = scoring()
        if n_score < score:
            score = n_score
            print(score)
            cnt += 1
        else:
            weight[idx1][idx2] = f_weight
        if cnt % 10 == 0:
            output()

def anneal2(tl):
    global ans, start_temp, end_temp
    score = scoring()
    min_score = score
    print('anneal2')
    print(score)
    strt = time()
    cnt = 0
    while time() - strt < tl:
        idx1 = randint(0, pattern_num - 1)
        idx2 = randint(0, each_param_num[idx1] - 1)
        f_val = ans[idx1][idx2]
        ans[idx1][idx2] += random() * 0.01 - 0.005
        n_score = scoring()
        if n_score < score:
            score = n_score
            print(score)
            cnt += 1
        else:
            ans[idx1][idx2] = f_val
        if cnt % 10 == 0:
            output()


def output():
    with open('param_pattern.txt', 'w') as f:
        for i in range(pattern_num):
            for j in range(each_param_num[i]):
                f.write('{:f}'.format(ans[i][j]) + '\n')
    with open('patttern_weight.txt', 'w') as f:
        for i in range(pattern_num):
            for j in range(3):
                f.write('{:f}'.format(weight[i][j]) + '\n')

'''
g = [
    [-1, -1, -1, -1, 1, 0, 0, 0],
    [-1, -1, -1, 0, 0, 1, 0, 0],
    [1, 0, -1, -1, 0, 0, 1, 1],
    [0, 1, 0, 1, 1, 1, 1, 1],
    [-1, -1, -1, -1, -1, -1, -1, 1],
    [0, 1, 1, 0, -1, -1, -1, -1],
    [1, 1, 1, 0, 0, 1, 0, -1],
    [0, -1, 1, -1, 0, -1, 1, 1]
]
stdin = ''
for y in range(hw):
    for x in range(hw):
        stdin += str(g[y][x]) + ' '
    stdin += '\n'
print(0)
print(10)
print(stdin)
print('')
print(translate_p(g, edge1))
print(translate_p(g, corner1))
exit()
'''

with open('third_party/xxx.gam', 'rb') as f:
    raw_data = f.read()
games = [i for i in raw_data.splitlines()]


num = 1000
lst = [randint(0, 100000) for i in range(num)]
for i in trange(num):
    collect(str(games[lst[i]]))
'''
for _ in trange(100):
    collect()
'''
for i in range(pattern_num):
    for j in range(each_param_num[i]):
        ans[i][j] = win_num[i][j] / max(1, seen_num[i][j])

output()
#anneal0(10.0)
while True:
    anneal1(10.0)
    output()
    anneal2(10.0)
    output()
output()