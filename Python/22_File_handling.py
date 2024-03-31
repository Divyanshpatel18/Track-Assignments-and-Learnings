# # File handling in Python allows you to perform various operations on files, such as reading from 
# # and writing to them.
# # Python provides built-in functions and methods for file handling.

# # Opening a File:
# # You can open a file using the open() function. 
# # It takes two arguments: the file path and the mode (e.g., 'r' for reading, 'w' for writing, 
# # 'a' for appending, etc.).

# # 1.Open a file for reading
# file=open("1_python.py","r")
# print(file.read()) #you can read file only in read mode

# # 2. Open a file for writing (creates a new file if it doesn't exist)
# file = open("example.txt", "w")
# file.write("bye")

# # 3. Open a file for appending (creates a new file if it doesn't exist)
# file = open("example.txt", "a")
# file.write("divyansh")

# #4."x" file is created if already exists throws an error

# #5. "rb" read as binary  for reading binary file

# # You can read the contents of a file using various methods like read(), readline(), or readlines().

# # 1.Read the entire content of the file
# content = file.read()

# # 2.Read one line at a time
# line = file.readline()

# # 3.Read all lines into a list
# lines = file.readlines()

# # Closing a File:
# # After performing operations on a file, it's
# # essential to close it using the close() method to release system resources.

# file.close()

# #AUTOMATICALLY CLOSES THE FILE WITH close()
# # Open the file in write mode
# with open("example.txt", "w") as file:
#     # Write data to the file
#     file.write("Hello, World!\n")


# f=open("example.txt","r")
# while True:
#      line=f.readline()
#      if not line:
#        break
#      print(line)

f=open("example.txt","r")
i=0
while True:
     i=i+1
     line=f.readline()
     if not line:
       break
     m1=int(line.split(",")[0])
     m2=int(line.split(",")[1])
     m3=int(line.split(",")[2])
     print(f"student{i} physics: {m1*2}")
     print(f"student{i} chemistry: {m2*2}")
     print(f"student{i} maths: {m3*3}")
     print(line)
# f=open("example.txt",'w')
# lines=['line1\n','line2\n','line3\n']
# f.writelines(lines)
# f.close()