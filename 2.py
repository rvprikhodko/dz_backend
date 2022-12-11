k = int(input())
dictionary = {}

for i in range(10):
    dictionary[i] = 0

for i in range(4):
    string = input()
    for j in string:
        if j != '.':
            dictionary[int(j)] += 1

ans = 0
for i in range(10):
    if dictionary[i] < k * 2 and dictionary[i] != 0:
        ans += 1

print(ans)
