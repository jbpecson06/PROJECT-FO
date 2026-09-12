import os
import shutil


folder_path = input("What folder path? ")


if os.path.exists("c:/Users/STUDENT/Desktop/test_PecsonJohnBrian"):
    print("The file exists!")
else:
    print("The file does not exist.")


list_of_files = os.listdir()
print(list_of_files)

images = 0
documents = 0
videos = 0
others = 0