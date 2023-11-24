import random
n=int(input('Введите количество элементов в списке :'))
a = [random.randint(-100000,100000) for i in range(n)]
# count_negative = 0
# for num in a:
#     if num < 0:
#         count_negative += 1
# print(count_negative)
# print(*a)
b=[]
for i in range(0,len(a)):
    if a[i]>0:
        b.append(a[i])
    else:
        b.append(a[i]*(-1))
c=0
for j in range(0,len(b))
print(a)
print(b)