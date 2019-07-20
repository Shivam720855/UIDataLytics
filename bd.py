from tkinter import *


root=Tk()
canvas=Canvas(width=800,height=500,bg="aqua")
canvas.pack()
photo=PhotoImage( file="C://Users//Shivamani//Desktop//kkk.png" )
canvas.create_image(0,0,image=photo,anchor="center")
 
textv='Starting'
def countdown(count):
    global l
    textv='Starting'
    l=Label(root,text='{0}'.format(textv),font=("arial",25),fg="green")
    l.pack() 
 
    
    if textv=='Starting':
        textv=textv+'.'
        l=Label(root,text='{0}'.format(textv),font=("arial",25),fg="green")
        l.pack()
    elif textv=='Starting.':
        textv=textv+'.'
        l=Label(root,text='{0}'.format(textv),font=("arial",25),fg="green")
        l.pack()   
    elif textv=='Starting..':
        textv=textv+'.'
        l=Label(root,text='{0}'.format(textv),font=("arial",25),fg="green")
        l.pack()   
    #elif textv=='Starting...'
        

        
    
    if count>1:
        root.after(1000,countdown,count-1)
""" else:
        l=Label(root,text="Starting",font=("arial",25),fg="green")
        global User_Temp
        #Listen_Temp()
        User_Temp=return_Temp[:5]
        l=Label(root,text=User_Temp+".",font=("arial",25),fg="green")
"""
     

       # l.pack()

 
 

countdown(3)
root.mainloop()
