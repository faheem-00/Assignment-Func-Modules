tuple_1=(1,2,3,4,5)

sum=0
for i in tuple_1:
    sum=sum+i
    i+=1
print(f"The sum of the nos of Tuple is {sum}")

l_no=max(tuple_1)
s_no=min(tuple_1)
print(f"The largest no in the Tuple is {l_no} and the smallest no is {s_no}")



# Tuple- I Number exists

num=int(input("Enter the Number:"))
tuple_2=(2,56,3,8,1,4,2)
count=0

for i in tuple_2:
    if i==num:
        count+=1
    else:
        i+=1
if count>0:
    print(f"The Number {num} is in the Tuple {count} times.")
else:
    print(f"The Number {num} does not exist in the Tuple.")