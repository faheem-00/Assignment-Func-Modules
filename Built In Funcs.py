# Longest Word finder
def longest_word(*y):
    word=""
    for i in range(len(y)):
        if len(y[i])> len(y):
            word=y[i]
        i+=1
    print(f"The longest word in the list is {word}")

longest_word("cherry", "Apple", "banana", "pineapple")


# Type checker
def type_checker(a):
    return type(a)
print(type_checker(42))
print(type_checker(a=[2,4,32]))


#Sum of evens - Using Range
def sum_of_evens(a):
    sum=0
    for i in range(0,a+1):
        if i%2==0:
            sum=sum+i
        i+=1
    return sum
print(sum_of_evens(10))