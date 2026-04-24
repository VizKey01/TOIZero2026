nums = []

for i in range(3):
    x = int(input())
    nums.append(x)
    print("Input number", i + 1, "stored.")

menu = int(input())

if menu == 1:
    print("Original order:", nums[0], nums[1], nums[2])

elif menu == 2:
    arr = nums[:]
    arr.sort(reverse=True)
    print("Descending order:", arr[0], arr[1], arr[2])

elif menu == 3:
    arr = nums[:]
    arr.sort()
    print("Ascending order:", arr[0], arr[1], arr[2])