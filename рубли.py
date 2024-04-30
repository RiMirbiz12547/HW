s = int(input("Введите число "))
if s % 10 == 1 and not s == 11:
    print(str(s) + " рубль ")
elif s % 10 == 2 or s % 10 == 3 or s % 10 == 4 and not s == 12 and not s == 13 and not s == 14:
    print(str(s) + " рубля ")
elif s == 11 or s == 12 or s == 13 or s == 14:
    print(str(s) + " рублей ")
else:
    print(str(s) + " рублей ")
