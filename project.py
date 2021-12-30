#This is "auto-renaming"
import os
originalfilename=input("Enter File Path with File Name: ")
newfilename=input("Enter the File Path with New File Name: ")
os.rename(originalfilename,newfilename)
print("file renamed succesfully")
