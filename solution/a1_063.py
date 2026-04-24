import sys

data = sys.stdin.read().split()

seats = int(data[0])
i = 1

while seats > 0 and i + 1 < len(data):
    age = int(data[i])
    n = int(data[i + 1])
    i += 2

    if age < 15:
        print(-1)

    elif n > seats:
        print(-2)

    else:
        price = 150 * n

        if age >= 15 and age <= 22:
            price = price * 80 // 100
        elif age >= 60:
            price = price * 50 // 100

        seats -= n
        print(price, seats)