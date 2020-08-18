# 遞迴加總陣列內容
def recrusion_sum(ls):
    # 基本情況
    if(len(ls) == 0):    return None
    elif(len(ls) == 1):  return ls[0]
    # 遞迴情況
    else:
        temp = ls.pop(0)
        return (temp + recrusion_sum(ls))


a = [1, 2, 3, 4, 5]
print(recrusion_sum(a))