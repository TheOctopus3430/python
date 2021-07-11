num = input('please input number: ')

num = int(num)
result = 1
for i in range(1, num):
    result = result * i

print(result)