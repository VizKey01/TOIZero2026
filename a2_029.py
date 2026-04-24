n = int(input())

for i in range(1, n + 1):
    for j in range(1, i + 1):
        if j == 1 or j == i or i == n:
            print(0, end="")
        else:
            print(1, end="")

        if j < i:
            print(" ", end="")

    print()

# แปลว่า ถ้าตำแหน่งนี้อยู่บนขอบสามเหลี่ยม ให้พิมพ์ 0

# j == 1 → ขอบซ้าย
# j == i → ขอบทแยง
# i == n → ฐานสามเหลี่ยม

# ซ้าย = j == 1
# ทแยง = j == i
# ฐาน = i == n
# ที่เหลือ = 1