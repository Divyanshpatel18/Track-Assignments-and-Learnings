import shutil
import os
# shutil.copy("example.txt","example2.txt")#copying the file
# shutil.copytree("exFolder","exFolder2")# copying the  directory
# shutil.move("exFolder2/Day_1","day1") #moving the file out
# shutil.move("day1","exFolder2/Day_1") #moving the file again to it original location
# shutil.rmtree("exFolder2")# deleting the directory
# os.remove("example2.txt")# shutil do not have command for deleting the file



# The shutil module in Python provides a higher-level interface for file operations. 
# It builds on top of the functionality provided by the os module and includes additional functions for
# # file copying, removal, and archiving.

# Here are some commonly used functions in the shutil module:

# shutil.copy(src, dst): Copies the file src to the file or directory dst.
# shutil.copy2(src, dst): Similar to copy(), but also preserves the file's metadata (timestamp and permission).
# shutil.copyfile(src, dst): Copies the contents of the file src to the file dst.
# shutil.copyfileobj(src, dst[, length]): Copies the contents of the file-like object src to the file-like object dst.
#    It can be used to copy between file objects, such as file handles or BytesIO objects.
# shutil.move(src, dst): Moves the file or directory src to dst.
# shutil.rmtree(path[, ignore_errors[, onerror]]): Deletes the directory tree rooted at path.
# shutil.rmtree(path[, ignore_errors[, onerror]]): Deletes the directory tree rooted at path.
# shutil.make_archive(base_name, format[, root_dir[, base_dir[, verbose[, dry_run[, owner[, group[, logger]]]]]]]): 
#    Creates an archive file (e.g., zip, tar) from the specified directory root_dir and returns its name.
# shutil.unpack_archive(filename[, extract_dir[, format]]): Extracts the contents of the archive file
#      specified by filename into the directory extract_dir.
# shutil.disk_usage(path): Returns a named tuple with the total, used, and free disk space (in bytes) for 
#      the filesystem containing path.
# shutil.which(cmd[, mode=os.F_OK | os.X_OK[, path=None]]): Returns the path to an executable file that
#      would be run if cmd were called, or None if no such file is found.
# shutil.get_terminal_size(fallback=(columns, lines)): Returns the size of the terminal window as a 
#      named tuple (columns, lines).