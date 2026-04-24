n = int(input())

count = 0

for i in range(n):
    ch = input()

    if ch == "A" or ch == "E" or ch == "I" or ch == "O" or ch == "U":
        count += 1

print(count)