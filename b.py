n = int(input())
row = [0] * n
ans = []
sum_val = 0

for _ in range(n):
    s = input()
    ans.append(s)
    cnt = s.count('_')
    sum_val += cnt
    row[_] = cnt

s = input()
g = list(map(int, s.split(',')))

str_input = input()
mp = {}
k = 0
index = -1

for w in str_input.split():
    if w[0] == '?':
        index = k
    else:
        mp[k] = int(w)
    k += 1

tot = int(input())

vec = []

if len(g) % 2 == 0:
    mid = len(g) // 2
    idx = mid
    c = 1
    while idx < len(g):
        vec.append((c, g[idx]))
        idx += 1
        c += 1
    idx = mid - 1
    while idx >= 0:
        vec.append((c, g[idx]))
        idx -= 1
        c += 1
else:
    mid = len(g) // 2
    idx = mid
    c = 1
    while idx < len(g):
        vec.append((c, g[idx]))
        idx += 1
        c += 1
    idx = mid - 1
    while idx >= 0:
        vec.append((c, g[idx]))
        idx -= 1
        c += 1

v = []

for i in range(len(vec)):
    x, size = vec[i]
    f = True
    for j in range(n):
        if row[j] >= size:
            f = False
            s = list(ans[j])
            sum_val -= size
            row[j] -= size
            for i in range(len(s)):
                if size == 0:
                    continue
                if s[i] == '_':
                    s[i] = str(x)
                    size -= 1
            ans[j] = ''.join(s)
            break
    if f:
        v.append(x)

s = list(ans[index])
cnt = 0
idx = 0

for i in range(n):
    s = list(ans[i])
    c = 0
    for it in s:
        if it == '_' or it == 'X':
            print(it, end='')
        else:
            c += 1
            print(it, end='')
    if idx in mp:
        tot -= mp[idx] * c
    print()

    idx += 1

print(sum_val, end=' ')
for it in v:
    print(it, end=' ')

cnt = 0

for it in ans[index]:
    if it == 'X' or it == '_':
        pass
    else:
        cnt += 1

tot //= cnt

print()
print(tot)
