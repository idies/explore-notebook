
# coding: utf-8

# In[ ]:


## Add getJpeg and Imgcutout
# connect DB and add user input


# In[ ]:


# coding: utf-8


import os
import sys


# In[ ]:


def id_chk(): 
# Checking to see if the Id number entered has a corresponding image/values in the databse
    x= 0
    print("Enter ID number")
    df=input()
    x=SciServer.SkyServer.objectSearch(objId=df)
    try:       
        if (x== 0):
            print("There is no object with that Id. Please try again")
            id_chk()
        else: ##invalid syntax?##
            print("#CALL THE PROCESSING FUNCTION#")
        #var_init_.obj(df)    
    
    except MemoryError:
        print("try again")
        sys.exit()


# In[ ]:


def main():
    
    z=7
    while (z != 4): #turn them into buttons and user input is click
        print("1. Search with object Id")
        print("2. Search with object co-ordinates")
        print("3. search with common name")
        print("4. Hide ?")
        z = input("Option: ")    
        
        try :
            if (z==1):
                id_chk()
                z=4
            elif (z==2):
                coordinate_chk()
                z=4
                
            elif(z==3):
                nm_chk()
                z=4
            elif(z==4):
                print("...")
        ## Hide panel ##
                
            else : ##invalid syntax?##
                print("Error")
                z=4
                main()
            
        except MemoryError:
            pass
            
            

if (__name__ == "__main__"):
    pass
    main()
else: 
    sys.exit()
  


# In[2]:


import setup

setup.py

