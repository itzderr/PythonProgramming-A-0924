# 3
s = "hello world"

reversed_s = ""
for i in range(len(s) - 1, -1, -1):
    reversed_s += s[i]

reversed_s2 = ""
for i in range(len(s)):
    reversed_s2 += s[len(s) - 1 - i]

reversed_s3 = ""
j = len(s) - 1
while j >= 0:
    reversed_s3 += s[j]
    j -= 1

print(reversed_s3)

# 4
word = "coding"
for ch in word:
    print(ord(ch), end=" ")
print()

# 5
s = "experience"
count_e = 0
for ch in s:
    if ch == "e":
        count_e += 1

print(count_e)

# 7
s = "looping"
res = ""
for i in range(0, len(s), 2):
    res += s[i]
    # print(s[i], end="")
print(res)

# 8
seen = []
country = "swiss"
for ch in country:
    if ch in seen:
        print(ch)
        break
    else:
        seen.append(ch)

# 9
s = "machine learning is fun"
cap_s = ""
l = s.split(" ")

for w in l:
    cap_s += w.capitalize() + " "

print(cap_s)


