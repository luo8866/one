import os
import zipfile
import csv
           
    
a = 1    
filepath = 'D:\software\python\code\people'
for root, dirs, files in os.walk(filepath): 
    #dirs[:] = []     
    print(root)        
    print("*****************")        
    print(dirs)        
    print("************")        
    print(files)        
    print(a)        
    a +=1
