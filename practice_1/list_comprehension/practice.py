lst = [1,2,3,4,5]
lst_2 = [3,4,5,7,8,9]
lst_3 =[]
for i in lst:
    if i not in lst_2:
        lst_2.append(i)
print(lst_2)
result = sorted(lst_2)
print(result)

