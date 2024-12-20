import math
import random

# Rhombus Area

def area_rhombus(d1,d2):
    area=1/2*(d1*d2)
    print(area)
area_rhombus(2,4)



#Generate Random Nos
def generate_random_numbers(a,b):
    num_list=[]
    for i in range(a,b):
        num_list.append(random.randrange(a,b))
        i+=1
    print(num_list)
generate_random_numbers(10,30)