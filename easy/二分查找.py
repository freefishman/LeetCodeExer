# 递归实现
def binary_search(lis, left, right, num):
    if left > right:
        return -1
    mid = (left + right) // 2
    if lis[mid] > num:
        right = mid - 1
    elif lis[mid] < num:
        left = mid + 1
    else:
        return mid
    return binary_search(lis, left, right, num)

lis = [2,6,8,12,56]
print(binary_search(lis,0,len(lis),56))