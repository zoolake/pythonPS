# 가장 왼쪽 좌표 3,'3'
# 가장 상단 좌표 '1',5
# 가장 오른쪽 좌표 2,'7'
# 가장 하단 좌표 '4',4
def solution(wallpaper):
    answer = []

    row_size, col_size = len(wallpaper), len(wallpaper[0])
    left_up_row, left_up_col, right_down_row, right_down_col = row_size + 1, col_size + 1, 0, 0

    for i in range(row_size):
        for j in range(col_size):
            # File 인 경우
            if wallpaper[i][j] == '#':
                left_up_row = min(left_up_row, i)
                left_up_col = min(left_up_col, j)
                right_down_row = max(right_down_row, i + 1)
                right_down_col = max(right_down_col, j + 1)

    answer = [left_up_row, left_up_col, right_down_row, right_down_col]
    return answer