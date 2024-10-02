# 4
l = [1, 4, 4, 2, 4, 3]
count_4 = 0
for e in l:
    if e == 4:
        count_4 += 1

print(count_4)

# 9
l = [1, 3, 3, 4, 3, 5, 3]

for i in range(len(l) - 1, -1, -1):
    if l[i] == 3:
        l.pop(i)

print(l)

