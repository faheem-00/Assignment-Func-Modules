#q1 Creating and Accessing Dictionaries

student={
    "Faheem": 77,
    "Aqleem": 89,
    "Zamin": 88
}
print(student["Zamin"])

#Using dictionary methods

this_dict={}
#adding key-value pairs
this_dict["Faheem"]=88
this_dict["zamin"]=98
this_dict["aqleem"]=95

print(this_dict)
#updating a value
this_dict.update({"aqleem":99})
print(this_dict)

#using get() key method
x=this_dict.get("Faheem")
print(x)


# Write a program to count the occurrences of each character in a given string using a dictionary.

string=input("Enter a String:")
char_count={}

for i in string:
    if i in char_count:
        char_count[i]+=1
    else:
        char_count[i]=1
print(char_count)
