T = "⏹️"  # tuong
D = "⬜"  # duong
BD = "⭐"  # diem bat dau
DICH = "🚾" # dich den
MT = {
    "tren": "⬆",
    "duoi": "⬇",
    "trai": "⬅",
    "phai": "➡"
    }  # mui ten
DD = "⬛"  # duong da di

def draw_maze(maze):
    n = len(maze)
    m = len(maze[0])
    for i in range(n):
        for j in range(m):
            print(maze[i][j], end = '')
        print()
    print()

def get_start(maze):
    n = len(maze)
    m = len(maze[0])
    for i in range(n):
        for j in range(m):
            if maze[i][j] == BD:
                return [i, j]

def get_end(maze):
    n = len(maze)
    m = len(maze[0])
    for i in range(n):
        for j in range(m):
            if maze[i][j] == DICH:
                return [i, j]
            
def get_neighbors(x, y):
    tren = [x-1, y]
    duoi = [x+1, y]
    trai = [x, y-1]
    phai = [x, y+1]
    return [tren, duoi, trai, phai]

def BFS(maze):
    bat_dau = get_start(maze)
    ket_thuc = get_end(maze)
    n, m = len(maze), len(maze[0])
    queue = [bat_dau]
    da_di = []
    cha = dict()
    while queue:
        x, y = queue.pop(0)  # o hien tai
        da_di.append([x, y])
        
        if [x, y] == ket_thuc:
            return da_di, cha
        # them neighbors vao queue
        for u, v in get_neighbors(x, y):
            if u < 0 or v < 0 or u >= n or v >=m:
                continue
            elif [u, v] in da_di or [u, v] in queue:
                continue
            elif maze[u][v] != T:
                queue.append([u, v])
                uv = ",".join([str(u), str(v)])
                xy = ",".join([str(x), str(y)]) 
                cha[uv] = xy
    return da_di, cha

def get_path(cha, bat_dau, ket_thuc):
    x0, y0 = bat_dau
    node_0 = ",".join([str(x0), str(y0)])
    x, y = ket_thuc
    node = ",".join([str(x), str(y)])

    duong_di = []
    while node != node_0:
        array = list(map(int, node.split(",")))
        duong_di.append(array)
        node = cha[node]
    duong_di = duong_di[::-1]
    return duong_di

def get_vi_tri(x, y, o_sau):
    if o_sau == [x-1, y]:
        return "tren"
    if o_sau == [x+1, y]:
        return "duoi"
    if o_sau == [x, y-1]:
        return "trai"
    if o_sau == [x, y+1]:
        return "phai"
    
def update_maze(maze, da_di, cha):
    bat_dau = get_start(maze)
    ket_thuc = get_end(maze)
    duong_di = get_path(cha, bat_dau, ket_thuc)
    # update duong di
    i = 0
    while i < len(duong_di)-1:
        x, y = duong_di[i]
        vi_tri = get_vi_tri(x, y, duong_di[i+1])
        maze[x][y] = MT[vi_tri]
        i += 1
    # update cac o da di
    for x, y in da_di:
        if [x, y] == bat_dau or [x, y] in duong_di:
            continue
        else:
            maze[x][y] = DD
    return duong_di

# main
maze = [
    [BD, D, T, T, T, T, T, T, T, T],
    [D, D, D, D, D, D, T, T, T, T],
    [T, T, D, T, T, D, T, D, D, T],
    [T, T, D, T, T, D, T, D, T, T],
    [T, T, D, D, D, D, D, D, D, T],
    [T, T, T, D, T, T, T, T, D, T],
    [T, T, T, D, T, T, T, D, D, T],
    [T, T, D, D, D, D, T, D, T, T],
    [T, T, T, T, T, D, D, D, T, T],
    [T, T, T, T, T, T, T, D, D, DICH],
]

print("Mê cung:\n")
draw_maze(maze)
da_di, cha = BFS(maze)
duong_di = update_maze(maze, da_di, cha)
print("Đường đi theo BFS:\n")
draw_maze(maze)
print("Độ dài đường đi:", len(duong_di))
