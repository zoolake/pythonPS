answer = set()


def dfs(key, nums, visited, values):
    global answer

    # 방문한적이 있다면
    if visited[key]:
        for i in range(len(visited)):
            if visited[i] and i not in values:
                return False
        else:
            for value in values:
                answer.add(value)
            return True

    visited[key] = True
    value = nums[key]
    dfs(value, nums, visited, values + [value])


# input
N = int(input())
nums = [0] * (N + 1)
for i in range(1, N + 1):
    nums[i] = int(input())

for i in range(1, N + 1):
    visited = [False] * (N + 1)
    dfs(i, nums, visited, [])

answer = list(answer)
answer.sort()
print(len(answer))
for i in answer:
    print(i)
