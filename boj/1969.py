N, M = map(int, input().split())
dna_list = [input() for _ in range(N)]

index_table = {"A": 0, "C": 1, "G": 2, "T": 3}
alphabet_table = {0: "A", 1: "C", 2: "G", 3: "T"}

counter = [[0] * 4 for _ in range(M)]
for dna in dna_list:
    for i in range(M):
        alphabet = dna[i]
        counter[i][index_table[alphabet]] += 1

s = ""
for i in range(M):
    max_count = 0
    max_index = 0
    for j in range(4):
        if max_count < counter[i][j]:
            max_count = counter[i][j]
            max_index = j

    s += alphabet_table[max_index]

count = 0
for dna in dna_list:
    for i in range(M):
        if dna[i] != s[i]:
            count += 1

print(s)
print(count)
