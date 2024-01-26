import os


folders_path = input("enter path of folders separated by spaces    ").split()
for folder in folders_path:
          try:
               files = os.listdir(folder)
          except FileNotFoundError:
               print("The folder  " + folder + "  does not exist")
               continue

          print (" \nfiles in   "+ folder + "  folder are\n ") 
   
          for file in files:
              print (file)
 
