#!/usr/bin/env python
# coding: utf-8

# In[48]:


contact_book={}

def display_contact():
    print("name\t\t number")
    for key in contact_book:
        print("{}\t\t {}".format(key,contact_book.get(key)))
        
print("enter choice")             


while True:
    choice=int(input(" 1.Add contact\n 2.search_contact\n 3.Edit_contact \n 4.delete_contact\n 5. Exit\n"))
    
    if choice == 1:
        name= input("enter name\n")
        number=input("enter number\n")
        contact_book[name]= number
        display_contact()
    
    elif choice == 2:
        search_contact=input("enter your name to search\n")
        if search_contact in contact_book:
            print(search_contact, "contact number is",contact_book[search_contact])
        else:
            print("Name is not found in contact_book")
    
    elif choice == 3:
        Edit_contact=input("enter contact to be edited\n")
        if Edit_contact in contact_book:
            number=input("enter number\n")
            contact_book[Edit_contact]=number
            print("contact edited")
        else:
            print("contact not present")
    
    elif choice == 4:
        delete_contact=input("enter name to be deleted\n")
        if delete_contact in contact_book:
            contact_book.pop(delete_contact)
            print(delete_contact,"is deleted")
            display_contact()
        else:
            print("contact not present")
            
    else:
        break;
            


# In[ ]:





# In[ ]:





# In[ ]:




