def min_pos(a, b):
    if a < 0 and b > 0:
        return b
    if a > 0 and b < 0:
        return a
    return min(a, b)


arr = list(map(int, input().split()))

sub1 = []
sub2 = []
zero_found = False
count = 0

for i in range(len(arr)):
    if arr[i] == 0:
        zero_found = True
        count = 0
    if not zero_found:
        sub1.append(-1)
    if zero_found:
        sub1.append(count)
        count += 1

zero_found = False
count = 0
for i in range(len(arr)-1, -1, -1):
    if arr[i] == 0:
        zero_found = True
        count = 0
    if not zero_found:
        sub2.append(-1)
    if zero_found:
        sub2.append(count)
        count += 1

sub2 = sub2[::-1]
ans = []

for i in range(len(arr)):
    ans.append(min_pos(sub1[i], sub2[i]))

for i in range(len(ans)):
    print(ans[i], end=' ')
