def bubble_sort(arry):
    n = len(arry)                   #获得数组的长度
    for i in range(0,n-1):
        for j in range(i+1,n):
            if arry[i] > arry[j] :       #如果前者比后者大
                arry[i],arry[j] = arry[j],arry[i]      #则交换两者
    return arry

# def bubble_sort(arry):
#     n = len(arry)                   #获得数组的长度
#     for i in range(n):
#         for j in range(1,n-i):
#             if  arry[j-1] > arry[j] :       #如果前者比后者大
#                 arry[j-1],arry[j] = arry[j],arry[j-1]      #则交换两者
#     return arry
print(bubble_sort([3,1,5,5,9,2]))