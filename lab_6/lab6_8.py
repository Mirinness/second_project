import os
import shutil  # import os module

os.mkdir("folder_zip")  # Create my_zip.zip file in current work directory

for filename in range(3):  # Create files with data in current folder
    f = open("folder_zip/file_%s" % filename, "w")
    f.write('some data')
    f.close()

shutil.make_archive("my_zip", "zip", root_dir=".",
                    base_dir="./folder_zip")  # Create my_zip.zip file in current work directory
shutil.copy("my_zip.zip", "../my_zip.zip")  # Copy archive into folder above
shutil.rmtree("folder_zip")  # Remove folder_zip
input()  # Wait for user input and check the data here
shutil.unpack_archive("../my_zip.zip")  # Unpack files into folder_zip
os.remove("my_zip.zip")  # Remove archive from current folder
os.remove("../my_zip.zip")  # Remove archive from folder above
print(shutil.disk_usage("."))  # Print disk Usage of current folder
