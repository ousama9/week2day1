#1


list_num = []
for i in range(1,11):
    cube = i**3
    list_num.append(cube)
for cube in list_num:
    print(cube)


 #2
 


for i in range(2,101):
    for j in range(2,101):
        if i%j == 0:
            break
    if i == j:
        print(i,end=",")





