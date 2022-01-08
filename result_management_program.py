from tkinter import *
from tkinter import ttk
#import mysql.connector as mys
from tkinter import messagebox as MessageBox
import sqlite3 as db
#root frame
root = Tk()

root.geometry("600x400")
root.title("STUDENT MANAGEMENT PROGRAM")
root.geometry("1200x800+0+0")
root.configure (bg='#5C6BC0')
#top title
con=db.connect("abhi.shek")
#con = mys.connect(host="localhost", user="root", password="1234", database="aman")
cursor = con.cursor()

cursor.execute("create table if not exists emp(adm_no int,roll_no int,name varchar(50), section varchar(50) , fname varchar(50),gender varchar(50))")
con.commit()

top_title=Label(root, text="STUDENT MANAGEMENT PROGRAM",bd=10,relief=GROOVE, font=("times new roman", 40 , "bold"),bg="#4DB6AC",fg="#F57F17")

top_title.pack(side=TOP ,fill=X)



### toplevel-add-marks



def Add_stud():
	add_stud=Toplevel(root)
	add_stud.geometry("700x700")
	frame_s1=Frame(add_stud,bd=4,relief=RIDGE,bg="#7ec0ee")
	frame_s1.place(x=20,y=100,width=500,height=560)

	eng=Label(frame_s1,text="ENGLISH",bg="#7ec0ee",fg="white",font=("times new roman",15,"bold"))

	eng.grid (row=7,column=0,pady=10,padx=20,sticky="w")
	e_eng=Entry(frame_s1,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
	
	e_eng.grid(row=7,column=1,pady=10,padx=20, sticky= "w")
	
	
	#entry for MATHEMATICS
	math=Label(frame_s1,text="MATH",bg="#7ec0ee",fg="white",font=("times new roman",15,"bold"))

	math.grid (row=6,column=0,pady=10,padx=20,sticky="w")
	e_math=Entry(frame_s1,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
	
	e_math.grid(row=6,column=1,pady=10,padx=20, sticky= "w")
	
	#HINDI label
	roll=Label(frame_s1,text="HINDI",bg="#7ec0ee",fg="white",font=("times new roman",15,"bold"))
	
	roll.grid (row=8,column=0,pady=10,padx=20,sticky="w")
	
	#entry for HINDI
	e_math=Entry(frame_s1,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
	
	e_math.grid(row=8,column=1,pady=10,padx=20, sticky= "w")
	exit=Button(frame_s1 ,text="EXIT",font=("times new roman",10,"bold"),command=add_stud.destroy,width=10).grid(row=11,column=0)
	
	frame_s2=Frame(add_stud,bd=4,relief=RIDGE,bg="#7ec0ee")
	frame_s2.place(x=500,y=100,width=750,height=560)
	
	
	#heading of frame2    0 row
	
	title2=Label(frame_s2,text="Student Marks",bg="#7ec0ee",fg="white",font=("times new roman", 20 , "bold"))
	
	title2.grid(row=0,columnspan=6)
	#grid(row=0,column=3,padx=7,pady=7,)
	
	
	
	
	#sub/exam label    1 row 
	sub_exam=Label(frame_s2,text="SUB./EXAM",bg="#7986CB",fg="white",font=("times new roman",15,"bold"))
	
	sub_exam.grid (row=1,column=0,pady=10,padx=20,sticky="w")
	
	def marks_tree():
	    tree=ttk.Treeview(frame2, columns=(1,2,3,4,5,6),show="headings",height=60)
	    tree.pack(expand=YES,padx=20,pady=20)
	    tree.heading(1,text="Adm_no")
	    tree.heading(2,text="roll no")
	    tree.heading(3,text="Name")
	    tree.heading(4,text="Section")
	    tree.heading(5,text="Father name")
	    tree.heading(6,text="Gender")
	    tree.column(1, minwidth=0, width=100, stretch=NO)
	    tree.column(2, minwidth=0, width=100, stretch=NO)
	    tree.column(3, minwidth=0, width=100, stretch=NO)
	    tree.column(4, minwidth=0, width=100, stretch=NO)
	    tree.column(5, minwidth=0, width=100, stretch=NO)
	    tree.column(6, minwidth=0, width=100, stretch=NO)
	
	    
	    
	    cursor.execute("Select * from emp")
	    rows=cursor.fetchall()
	    for row in rows:
	        tree.insert('',0,values=row)
	              
	def insert():
	    insert_adm_no=e_adm_no.get()
	    insert_name=e_name.get()
	    insert_roll=e_roll.get()
	    insert_section=e_section.get()
	    insert_father=e_father.get()
	    insert_gender=e_gender.get()
	
	    if(insert_adm_no=="" or insert_name=="" or insert_roll=="" or insert_section=="" or insert_father=="" or insert_gender=="" or insert_roll==""):
	        MessageBox.showinfo("Insert Status","All Fields are required")
	    else:
	        cursor.execute("insert into marks(sname,{},phy,chem,math,eng,ip) values({},{},{},{},{},{},{})".format(en,n,en,p,c,m,ip))
	        cursor.execute("commit");
	        clear_fields()
	
	        #e_adm_no.delete(0, 'end')
#	        e_name.delete(0, 'end')
#	        e_roll.delete(0, 'end')
#	        e_section.delete(0, 'end')
#	        e_father.delete(0, 'end')
#	        e_gender.delete(0, 'end')
	        
	        MessageBox.showinfo("insert status", "Inserted Successfully")
	        tree_view()
	        #con.close()
	

def tree_view():
    tree=ttk.Treeview(frame2, columns=(1,2,3,4,5,6),show="headings",height=60)
    tree.pack(expand=YES,padx=20,pady=20)
    tree.heading(1,text="Adm_no")
    tree.heading(2,text="roll no")
    tree.heading(3,text="Name")
    tree.heading(4,text="Section")
    tree.heading(5,text="Father name")
    tree.heading(6,text="Gender")
    tree.column(1, minwidth=0, width=100, stretch=NO)
    tree.column(2, minwidth=0, width=100, stretch=NO)
    tree.column(3, minwidth=0, width=100, stretch=NO)
    tree.column(4, minwidth=0, width=100, stretch=NO)
    tree.column(5, minwidth=0, width=100, stretch=NO)
    tree.column(6, minwidth=0, width=100, stretch=NO)

    
    
    cursor.execute("Select * from emp")
    rows=cursor.fetchall()
    for row in rows:
        tree.insert('','end',values=row)
              
   




def insert():
    insert_adm_no=e_adm_no.get()
    insert_name=e_name.get()
    insert_roll=e_roll.get()
    insert_section=e_section.get()
    insert_father=e_father.get()
    insert_gender=e_gender.get()

    if(insert_adm_no=="" or insert_name=="" or insert_roll=="" or insert_section=="" or insert_father=="" or insert_gender=="" or insert_roll==""):
        MessageBox.showinfo("Insert Status","All Fields are required")
    else:
        cursor.execute("insert into emp values('"+ insert_adm_no +"', '"+ insert_roll +"','"+ insert_name +"','"+ insert_section +"','"+ insert_father+"','"+ insert_gender+"')")
        cursor.execute("commit");
        

        e_adm_no.delete(0, 'end')
        e_name.delete(0, 'end')
        e_roll.delete(0, 'end')
        e_section.delete(0, 'end')
        e_father.delete(0, 'end')
        e_gender.delete(0, 'end')
        
        MessageBox.showinfo("insert status", "Inserted Successfully")
        tree_view()
        #con.close()
def update():
    a=e_adm_no.get()
    n=e_name.get()
    r=e_roll.get()
    s=e_section.get()
    f=e_father.get()
    g=e_gender.get()
    cursor.execute("update emp set roll_no={},name={},section={},fname={},gender={} where adm_no={}",format(r,n,s,f,g,a))
    con.commit()

def Delete1():
    delete_adm_no=e_adm_no.get()
    delete_name=e_name.get()
    delete_roll=e_roll.get()
    
    if( delete_adm_no==""):
        MessageBox.showinfo("Delete Status","ID Fields is required")
    else:
        cursor.execute("delete from emp where adm_no= {}".format(delete_adm_no))
        cursor.execute("commit");

        delete_adm_no=e_adm_no.get()
        delete_name=e_name.get()
        delete_roll=e_roll.get()
        delete_section=e_section.get()
        delete_father=e_father.get()
        delete_gender=e_gender.get()
        delete_roll=e_roll.get()
        MessageBox.showinfo("Delete status", "Delete Successfully")
        tree_view()
        





def Search():
    search_adm_no=e_adm_no.get()
    search_name=e_name.get()
    search_roll=e_roll.get()
    search_section=e_section.get()
    search_father=e_father.get()
    search_gender=e_gender.get()
    #search_dob=e_dob.get()

    
    if(search_adm_no==""):
        MessageBox.showinfo("Delete Status","ID Fields is required")
    else:
        cursor.execute("Select * from emp where adm_no= {} ".format(search_adm_no))
        rows = cursor.fetchall()
        clear_fields()
        #e_adm_no.delete(0, 'end')
#        e_adm_no.delete(0,'end')
#        e_name.delete(0,'end')
#        e_roll.delete(0,'end')
#        e_section.delete(0,'end')
#        e_father.delete(0,'end')
#        e_gender.set('')
        for row in rows:
            e_adm_no.delete(0, 'end')
            e_adm_no.insert(0,row[0])
            e_name.insert(0,row[2])
            e_roll.insert(0,row[1])
            e_section.insert(0,row[3])
            e_father.insert(0,row[4])
            e_gender.set(row[5])  
            tree_view()
        


def on_click(event):
    e_dob.configure(state=NORMAL)
    e_dob.delete(0, END)

    # make the callback only work once
    e_dob.unbind('<Button-1>', on_click_id)


#---------------frame1 entries frame---------------

frame1=Frame(root,bd=4,relief=RIDGE,bg="#7ec0ee")
frame1.place(x=20,y=100,width=500,height=560)

#heading of frame1

title=Label(frame1,text="Student Entries",bg="#7ec0ee",fg="white",font=("times new roman", 20 , "bold"))

title.grid(row=0,columnspan=2)

#adm_no label
adm_no=Label(frame1,text="ADM_NO.",bg="#7ec0ee",fg="white",font=("times new roman",15,"bold"))

adm_no.grid (row=1,column=0,pady=10,padx=20,sticky="w")

#entry for adm_no
e_adm_no=Entry(frame1,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)

e_adm_no.grid(row=1,column=1,pady=10,padx=20, sticky= "w")

#name label
name=Label(frame1,text="NAME",bg="#7ec0ee",fg="white",font=("times new roman",15,"bold"))

name.grid (row=2,column=0,pady=10,padx=20,sticky="w")

#entry for name
e_name=Entry(frame1,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)

e_name.grid(row=2,column=1,pady=10,padx=20, sticky= "w")


#ROLL NO label
roll=Label(frame1,text="ROLL NO",bg="#7ec0ee",fg="white",font=("times new roman",15,"bold"))

roll.grid (row=3,column=0,pady=10,padx=20,sticky="w")

#entry for roll no
e_roll=Entry(frame1,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)

e_roll.grid(row=3,column=1,pady=10,padx=20, sticky= "w")

#section label
section=Label(frame1,text="SECTION",bg="#7ec0ee",fg="white",font=("times new roman",15,"bold"))

section.grid (row=4,column=0,pady=10,padx=20,sticky="w")

#entry for section
e_section=Entry(frame1,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)

e_section.grid(row=4,column=1,pady=10,padx=20, sticky= "w")




#father label
father=Label(frame1,text="FATHER'S NAME",bg="#7ec0ee",fg="white",font=("times new roman",15,"bold"))

father.grid (row=5,column=0,pady=10,padx=20,sticky="w")

#entry for father
e_father=Entry(frame1,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)

e_father.grid(row=5,column=1,pady=10,padx=20, sticky= "w")

#gender label
gender=Label(frame1,text="GENDER",bg="#7ec0ee",fg="white",font=("times new roman",15,"bold"))

gender.grid(row=6,column=0,pady=10,padx=20,sticky="w")

#combo box for gender
e_gender=ttk.Combobox(frame1,font=("times new roman", 15 , "bold"),state='readonly')
e_gender['values']=("MALE","FEMALE")

e_gender.grid(row=6,column=1,padx=20,pady=10)


#DOB label
dob=Label(frame1,text="DATE OF BIRTH",bg="#7ec0ee",fg="white",font=("times new roman",15,"bold"))

dob.grid (row=7,column=0,pady=10,padx=20,sticky="w")

#entry for dob
e_dob=Entry(frame1,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)

e_dob.grid(row=7,column=1,pady=10,padx=20, sticky= "w")
e_dob.insert(0,"YYYY-MM-DD")

on_click_id = e_dob.bind('<Button-1>', on_click)


#ENGLISH label
#eng=Label(frame1,text="ENGLISH",bg="#7ec0ee",fg="white",font=("times new roman",15,"bold"))

#eng.grid (row=7,column=0,pady=10,padx=20,sticky="w")



#entry for MATHEMATICS
#e_math=Entry(frame1,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)

#e_math.grid(row=6,column=1,pady=10,padx=20, sticky= "w")

#HINDI label
#roll=Label(frame1,text="HINDI",bg="#7ec0ee",fg="white",font=("times new roman",15,"bold"))

#roll.grid (row=8,column=0,pady=10,padx=20,sticky="w")

#entry for HINDI
#e_math=Entry(frame1,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)

#e_math.grid(row=8,column=1,pady=10,padx=20, sticky= "w")





#---x--x-----x---x-----x-----frame1completed------x-----x----x-----x




#------------------frame2 -entries frame----------------

frame2=Frame(root,bd=4,relief=RIDGE,bg="#7ec0ee")
frame2.place(x=500,y=100,width=750,height=560)


#heading of frame2    0 row

title2=Label(frame2,text="Student Marks",bg="#7ec0ee",fg="white",font=("times new roman", 20 , "bold"))

title2.grid(row=0,columnspan=6)
#grid(row=0,column=3,padx=7,pady=7,)




#sub/exam label    1 row 
sub_exam=Label(frame2,text="SUB./EXAM",bg="#7986CB",fg="white",font=("times new roman",15,"bold"))

sub_exam.grid (row=1,column=0,pady=10,padx=20,sticky="w")























#--------------frame3 -button frame----------------------






frame3=Frame(root,bd=4,relief=RIDGE,bg="white")
frame3.place(x=30,y=600,width=401)
add_mark=Button(frame3 ,text="add marks",font=("times new roman",10,"bold"),command=Add_stud,width=10).grid(row=1,column=1,padx=7,pady=7)

save_btn=Button(frame3,text="INSERT",font=("times new roman",10,"bold"),command=insert,width=10).grid(row=0,column=1,padx=7,pady=7)

delete_btn=Button(frame3,text="DELETE",font=("times new roman",10,"bold"),command=Delete1,width=10).grid(row=0,column=4,padx=7,pady=7)

update_btn=Button(frame3,text="UPDATE",font=("times new roman",10,"bold"),width=10,command=update).grid(row=0,column=2,padx=7,pady=7)

search_btn=Button(frame3,text="SEARCH",font=("times new roman",10,"bold"),command=Search,width=10).grid(row=0,column=3,padx=7,pady=7)

'''
btn1=PhotoImage(file='insert-button-png-hi2.png')
btn2=PhotoImage(file='delete-button-png-hi.png')
btn3=PhotoImage(file='Update-Button-Transparent-Image.png')
btn4=PhotoImage(file='search-button-png-md.png')


insert_btn=Button(frame3,text="INSERT",image=btn1,borderwidth=5).grid(row=0,column=0,padx=7,pady=7)

delete_btn=Button(frame3,text="DELETE",image=btn2,borderwidth=5).grid(row=0,column=1,padx=7,pady=7)

update_btn=Button(frame3,text="UPDATE",image=btn3,borderwidth=5).grid(row=0,column=2,padx=7,pady=7)

search_btn=Button(frame3,text="SEARCH",image=btn4,borderwidth=5).grid(row=0,column=3,padx=7,pady=7)

'''

'''
insert_btn.pack(pady=20)
delete_btn.pack(pady=20)
update_btn.pack(pady=20)
search_btn.pack(pady=20)
'''











#------------------frame2 -entries frame----------------



frame2=Frame(root,bd=4,relief=RIDGE,bg="#7ec0ee")
frame2.place(x=500,y=100,height=560)

tree_view()











root.mainloop()
