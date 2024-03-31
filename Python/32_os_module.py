import os

# if(not os.path.exists("exFolder")):
#    os.mkdir("exFolder")

# creating 100 folders in one go
# for i in range(1,101):
#     os.mkdir(f"exFolder/Day_{i}")

# rename the folders
# for i in range(1,101):
#     os.rename(f"exFolder/Tutorial_{i}",f"exFolder/Day_{i}")


#listing all the folder

folders=os.listdir("exFolder")
# print(folders)
# for folder in folders:
#    print(folder)

# listing the files inside all  the folders

for folder in folders:
   print(folder)
   print(os.listdir(f"exFolder/{folder}"))











# The os module in Python provides a portable way to interact with the operating system. 
# It allows you to perform various operations such as navigating the file system, manipulating files and 
# directories, and executing system commands.

# Here are some commonly used functions and attributes provided by the os module:

# os.getcwd(): Returns the current working directory as a string.
# os.chdir(path): Changes the current working directory to the specified path.
# os.listdir(path='.'): Returns a list containing the names of the entries in the directory given by path.
# os.mkdir(path): Creates a new directory with the specified path.
# os.makedirs(path): Recursively creates directories with the specified path.
# os.remove(path): Removes (deletes) the file .
# os.rmdir(path): Removes (deletes) the directory . It must be empty.
# os.removedirs(path): Removes (deletes) directories recursively. If any intermediate level
#   directory is empty after removal, it's removed as well.
# os.rename(src, dst): Renames the file or directory from src to dst.
# os.path.exists(path): Returns True if the path exists, otherwise False.
# os.path.isdir(path): Returns True if the path is a directory, otherwise False.
# os.path.isfile(path): Returns True if the path is a file, otherwise False.
# os.path.join(path1, path2, ...): Joins path components intelligently.
# os.path.basename(path): Returns the base name of the specified path.
# os.path.dirname(path): Returns the directory name of the specified path.

