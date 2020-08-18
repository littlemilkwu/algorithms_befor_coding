def counter(num):
    if(num == 0):
        print(num)
    elif(num < 0):
        return 0
    else:
        print(num)
        counter(num - 1)


num = int(input("請輸入倒數數字："))
counter(num)