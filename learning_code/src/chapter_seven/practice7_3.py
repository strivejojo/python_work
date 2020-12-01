# 10的整数倍
num = input('Please input a number: ')
num = int(num)
if num % 10 == 0:
    print(f"{num} 是10的倍数。")
else:
    print(f"{num} 不是10的倍数。")
