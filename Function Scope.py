counter=0

# def increment_counter():
#     counter=counter+1  #Here the Variable Counter cant be accessed 
#     print(counter)
# increment_counter()

#modifyin the function to use Global Variable in it.

def increment_counter():
    global counter
    counter+=1  
    print(counter)
increment_counter()
