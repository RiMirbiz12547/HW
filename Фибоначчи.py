n = int(input("Введите номер числа Фибоначчи: "))

f0 = 0
f1 = 1

if n == 0:
    fn = f0
elif n == 1:
    fn = f1
else:
    for i in range(2, n + 1):
        fn = f0 + f1
        f0, f1 = f1, fn

print("Число Фибоначчи под номером", n, ":", fn)

