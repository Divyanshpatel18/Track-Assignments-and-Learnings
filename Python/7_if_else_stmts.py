# In Python,you can use the if,elif (short for "else if"),and else statements to perform conditional execution. 
age=int(input(" enter your age "))
if(age>18):
    print("you can drive")
elif(age==18):
    print("drive bicycle")
else:
    print("you cannot drive")
print("will always printed") #bcoz outside the block