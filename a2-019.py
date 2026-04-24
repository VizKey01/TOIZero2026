s = input()
text = s.upper()

max_u = 0

# หา B ทุกตัว แล้วนับ U ที่ติดกันหลัง B
for i in range(len(text)):
    if text[i] == "B":
        count_u = 0

        j = i + 1
        while j < len(text) and text[j] == "U":
            count_u += 1
            j += 1

        if count_u > max_u:
            max_u = count_u

# กรณีที่ 1: มี BUU
if max_u >= 2:
    print("Yes", max_u)

else:
    found_b = False
    first_b = -1

    # หา B ตัวแรก
    for i in range(len(text)):
        if text[i] == "B":
            found_b = True
            first_b = i
            break

    # กรณีที่ 2: ไม่มี BUU แต่มี B
    if found_b == True:
        ans = ""

        for i in range(len(s)):
            if i <= first_b:
                ans += s[i]
            else:
                ans += "U"

        print(ans)

    # กรณีที่ 3: ไม่มี B เลย
    else:
        pattern = "BUU"
        ans = ""

        for i in range(len(s)):
            ans += pattern[i % 3]

        print(ans)