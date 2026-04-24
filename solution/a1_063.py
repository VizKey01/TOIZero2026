seats = int(input())

while seats > 0:
    try:
        age, n = map(int, input().split())
    except:
        break

    if age < 15:
        print(-1)
    elif n > seats:
        print(-2)
        break
    else:
        price = 150 * n

        if age >= 15 and age <= 22:
            price = int(price * 0.8)
        elif age >= 60:
            price = int(price * 0.5)

        seats -= n
        print(price, seats)