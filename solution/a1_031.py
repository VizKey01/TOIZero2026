s = input()

ans = ""
n = len(s)

for i in range(n):
    # จากตัวสุดท้าย อันนี้เป็นตัวที่เท่าไหร่
    digits_left = n - i
    # 1 | 234 | 567
    if i > 0 and digits_left % 3 == 0:
        ans += ","

    ans += s[i]

print(ans)