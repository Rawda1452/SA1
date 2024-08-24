my_list=[1,2,3,4,5]
n=len(my_list)
for i in range(0,n):
    for j in range (i+1,n):
        if my_list[i]>my_list[j]:
            x=my_list[i]
            my_list[i]=my_list[j]
            my_list[j]=x
print(my_list[-2])
  