# 定義找尋最小值的函式
def find_smallest(ls):
    # 最小時初始化
    smallest = ls[0]
    smallest_index = 0
    for i in range(len(ls)):
        if(ls[i] < smallest):
            smallest = ls[i]
            smallest_index = i
    return smallest_index

# 定義select_sort
def select_sort(ls):
    sorted_ls = []
    for i in range(len(ls)):
        smallest_index = find_smallest(ls)
        sorted_ls.append(ls.pop(smallest_index))
    return sorted_ls

ls = [5, 3, 6, 2, 10]

print("排序前", ls)
sorted_ls = select_sort(ls)
print("排序後", sorted_ls)


