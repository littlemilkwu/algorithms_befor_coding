# 定義
def binary_search(ls, ans):
    low = 0
    high = len(ls) - 1
    while(low <= high):
        mid = int((low + high) / 2)
        if(ls[mid] == ans):
            # 找到答案，回傳位置
            return mid
        elif(ls[mid] < ans):
            # 若猜測小於答案，更正low範圍
            low = mid + 1
        elif(ls[mid] > ans):
            # 若餐側大於答案，更正high範圍
            high = mid - 1
    # 迴圈結束，代表沒有這個元素
    return None



# 輸入排序好的內容（小到大）
n = int(input("幾個數字？"))
ls = []
for i in range(n):
    print("輸入第", i, "位", end=" : ")
    num = int(input())
    ls.append(num)
# 輸入要找尋的數字
ans = int(input("要找哪個數字？（回傳位置）"))

# 二分搜尋
print(binary_search(ls, ans))
