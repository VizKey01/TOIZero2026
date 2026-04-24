s = input()

current = s[0]
count = 0
ans = ""

for ch in s:
    if ch == current:
        count += 1
    else:
        ans += str(count) + current
        current = ch
        count = 1

ans += str(count) + current

print(ans)