#python 3.5.2
import os
def print_directory_contents(sPath):
    #import os                                       
    for sChild in os.listdir(sPath):                
        sChildPath = os.path.join(sPath,sChild)
        if os.path.isdir(sChildPath):
            print_directory_contents(sChildPath)
        else:
            print (sChildPath)
#print(os.listdir("C:\\Users\\user\\Desktop\\问题汇总"))
print_directory_contents("C:\\Users\\user\\Desktop\\问题汇总")
