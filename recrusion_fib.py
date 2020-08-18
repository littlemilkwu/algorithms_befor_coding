# 定義費氏數列
def f(num):
    if(num == 0):   return 0
    elif(num == 1): return 1
    else:   return (f(num-1) + f(num-2))

print(f(10))