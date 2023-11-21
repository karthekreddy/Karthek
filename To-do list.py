#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Dolist=[]
while True:
    print("enter your choice\n")
    choice=float(input(" 1.Add_task\n 2.Delete_task\n 3.View_task\n 4.Exit\n"))
    if choice == 1:
        Add_task= input("enter your task\n")
        Dolist.append(Add_task)
           
    elif choice == 2:
        Delete_task=input("enter task to be deleted\n")
        Dolist.remove(Delete_task)
        print("task is deleted")
        for i in Dolist:
            print(i)
    
    elif choice == 3:
        for i in Dolist:
            print( i)
    
    else:
        break;



# In[ ]:





# In[ ]:




