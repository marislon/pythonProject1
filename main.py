# n = int(input('Input n: '))
# num = 1
# while num ** 2 <= n:
#     print(num ** 2)
#     num = num + 1
# print('end')
number = int(input())

result = 1
while number > 0:
    n = number % 10
    if n > 7:
        result = result * n
    number = number // 10
if result == 1:
    print()
