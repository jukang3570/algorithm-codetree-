import sys


arr = [list(map(int, input().split())) for _ in range(19)]

def five_check(stat, x, y, dx, dy):
    positions = [(x, y)]

    for _ in range(4):
        x += dx
        y += dy
        if 0 <= x < 19 and 0 <= y < 19 and arr[x][y] == stat:
            positions.append((x, y))
        else:
            return False, None

    return True, positions[2]

dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [1, 0, 1, -1, -1, 0, -1, 1]

for i in range(19):
    for j in range(19):
        if arr[i][j] > 0:
            for d in range(8):
                found, center_pos = five_check(arr[i][j], i, j, dx[d], dy[d])
                if found:
                    print(arr[i][j])
                    print(center_pos[0] + 1, center_pos[1] + 1)
                    exit()

print(0)
