# ==== DINH NGHIA CAC O TRONG ME CUNG ====
T = '⏹️'  # tuong
D = '⬜'  # duong
H = '⭐'  # nguoi choi
V = '⬛'  # duong da di

# ==== DU LIEU ME CUNG ====
maze = [
    [D, D, T, T, T, T, T, T, T, T],
    [T, D, D, D, D, D, T, T, T, T],
    [T, T, D, T, T, D, T, D, D, T],
    [T, T, D, T, T, D, T, D, T, T],
    [T, T, D, D, D, D, D, D, D, T],
    [T, T, T, D, T, T, T, T, D, T],
    [T, T, T, D, T, T, T, D, D, T],
    [T, T, D, D, D, D, T, D, T, T],
    [T, T, T, T, T, D, D, D, T, T],
    [T, T, T, T, T, T, T, D, D, D],
]


# ==== CAC HAM SE DUOC GOI ====
def draw_maze(maze):
    # Ve me cung
    n, m = len(maze), len(maze[0])
    for i in range(n):
        for j in range(m):
            print(maze[i][j], end='')
        print()


def get_neighbors(x, y):
    # Lay toa do cua 4 o xung quanh: tren, duoi, trai, phai
    return [[x - 1, y], [x + 1, y], [x, y - 1], [x, y + 1]]


def dfs(maze, start, end):
    # Lay kich thuoc me cung
    n, m = len(maze), len(maze[0])

    # Khoi tao stack
    stack = [start]

    # DFS
    while stack:
        # Lay ra mot o de xu ly
        x, y = stack.pop()
        maze[x][y] = H

        # Thoat khoi ham neu gap loi ra
        if [x, y] == end:
            return

        # Nhin 4 o xung quanh, them o duong di vao stack
        for u, v in get_neighbors(x, y):
            if u < 0 or v < 0 or u >= n or v >= m:
                # Truong hop 1: (u, v) nam ngoai me cung
                continue
            elif maze[u][v] == D:
                # Truong hop 2: (u, v) la duong chua di
                stack.append([u, v])

        # Ve me cung hien tai
        draw_maze(maze)
        maze[x][y] = V
        input()


# ==== CHUONG TRINH CHINH ====
draw_maze(maze)

input('\nChay Thuat Toan DFS:')
n, m = len(maze), len(maze[0])
dfs(maze, [0, 0], [n - 1, m - 1])

print('Ket Thuc Thuat Toan DFS:')
draw_maze(maze)
