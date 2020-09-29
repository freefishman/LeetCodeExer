# 1.给定两个数，输出R的n次方，其中0.0<R<99.999，0<n<=25

r=95.123
n=12
num=1
for i in range(1,n+1):
    num = num * r
print(num)
