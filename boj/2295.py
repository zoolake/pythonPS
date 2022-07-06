import collections

# input
N = int(input())
nums = [int(input()) for _ in range(N)]
# solution
nums.sort()
# a+b
temp_a = set()
for i in range(N):
    for j in range(N):
        temp_a.add(nums[i] + nums[j])
# d-c
temp_b = collections.defaultdict(int)
for i in range(N):
    for j in range(N):
        # map<key:(d-c) / value:max(d)>
        temp_b[(nums[i] - nums[j])] = max(temp_b[(nums[i] - nums[j])], nums[i])
answer = 0
for key in temp_a:
    answer = max(answer, temp_b[key])
print(answer)
