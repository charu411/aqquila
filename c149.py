#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 16:49:27 2023

@author: aquilavijayanayagam
"""


from tkinter import*
import random
root=Tk()
root.title("lucky freind by aquila")
root.geometry("400x400")

enter_name= Entry(root)
enter_name.place(relx= 0.5,rely=0.2,anchor=CENTER)

freind_list = Label(root)
random_number_label = Label(root)
lucky_freind = Label(root)


list1 = []
def addfreind():
    freind_name = enter_name.get()
    list1.append(freind_name)
    freind_list["text"] = "your friendlist:"+ str(list1)
    
   
def random_numbers():
    length = len(list1)
    random_no = random.randint(0, length-1)
    random_number_label["text"] = str(random_no)
    generated_random_number = list1[random_no]
    lucky_freind["text"] = "your lucky freind is: "+ str(generated_random_number)
    

btn = Button(root,text="add to freindlist", command= addfreind)
btn.place(relx= 0.5, rely = 0.3, anchor = CENTER)

# next line function name called wrong 
btn1 = Button(root, text="Who is your Lucky Friend? ", command = random_numbers)
btn1.place(relx= 0.5,rely = 0.5, anchor = CENTER )

random_number_label.place(relx= 0.5,rely = 0.6, anchor = CENTER)
#next line spelling of friend 
lucky_freind.place(relx= 0.5,rely = 0.7, anchor = CENTER)
# freind_list was not placed
freind_list.place(relx= 0.5,rely = 0.8, anchor = CENTER)
# lot of errors with relx rely
root.mainloop()

