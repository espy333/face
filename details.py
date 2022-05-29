from tkinter import*
from tkinter import ttk
from PIL import Image
from PIL import ImageTk
from tkinter import messagebox
import mysql.connector

class Details:
  def __init__(self,root):
    self.root=root
    self.root.geometry("1530x790+0+0")
    self.root.title("Face Recognition System")
    
    #variables
    self.var_name=StringVar()
    self.var_age=StringVar()
    self.var_phno=StringVar()
    self.var_gender=StringVar()
    self.var_proff=StringVar()
    self.var_ls=StringVar()
    self.var_desc=StringVar()




   #bg image
    img3=Image.open(r"C:\Users\admin\Desktop\face recog\collage_images\bgcolour3.png")
    img3=img3.resize((1530,790),Image.ANTIALIAS)
    self.photoimg3=ImageTk.PhotoImage(img3)

    bg_img=Label(self.root,image=self.photoimg3)
    bg_img.place(x=0,y=0,width=1530,height=790)

    title_lbl=Label(bg_img,text="Management System",font=("Cambria",40,),bg="#376E6F",fg="white",justify=CENTER)
    title_lbl.place(x=0,y=0,width=1530,height=55)
    
    main_frame=Frame(bg_img,bd=2)
    main_frame.place(x=0,y=55,width =1530,height=650)

    #left label frame
    Left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Enter details",bg="#a1c3d1",font=("Cambria",28))
    Left_frame.place(x=10,y=10,width=660,height=580)
    

   #Name
    name_label=Label(Left_frame,text="Name : ",font=("Cambria",20),fg="white",bg="#376E6F")
    name_label.grid(row=0,column=0,padx=2,pady=2,sticky=W)
    name_label.place(x=20,y=50,width=150,height=55)
    
    name_entry=ttk.Entry(Left_frame,textvariable=self.var_name,width=250,font=("Cambria",20))
    name_entry.grid(row=0,column=1,padx=2,pady=2,sticky=W)
    name_entry.place(x=180,y=50,width=250,height=55)

   #age
    age_label=Label(Left_frame,text="Age : ",font=("Cambria",20),fg="white",bg="#376E6F")
    age_label.grid(row=1,column=0,padx=2,pady=2,sticky=W)
    age_label.place(x=20,y=120,width=150,height=55)
    
    age_entry=ttk.Entry(Left_frame,textvariable=self.var_age,width=250,font=("Cambria",20))
    age_entry.grid(row=1,column=1,padx=2,pady=2,sticky=W)
    age_entry.place(x=180,y=120,width=250,height=55)
    

    #phno
    phno_label=Label(Left_frame,text="Phone no.: ",font=("Cambria",20),fg="white",bg="#376E6F")
    phno_label.grid(row=2,column=0,padx=2,pady=2,sticky=W)
    phno_label.place(x=20,y=190,width=150,height=55)
    
    phno_entry=ttk.Entry(Left_frame,textvariable=self.var_phno,width=250,font=("Cambria",20))
    phno_entry.grid(row=2,column=1,padx=2,pady=2,sticky=W)
    phno_entry.place(x=180,y=190,width=250,height=55)

   #gender
    gender_label=Label(Left_frame,text="Gender",font=("Cambria",20),fg="white",bg="#376E6F")
    gender_label.grid(row=3,column=0,padx=2,pady=2,sticky=W)
    gender_label.place(x=20,y=260,width=150,height=55)
    
    gender_combo=ttk.Combobox(Left_frame,textvariable=self.var_gender,font=("Cambria",16),width=17,state="read only")
    gender_combo["values"]=("Select Gender","Male","Female","Prefer not to say")
    gender_combo.current(0)
    gender_combo.grid(row=3,column=1,padx=2,pady=2,sticky=W)
    gender_combo.place(x=180,y=260,width=250,height=55)
    
    #radio button
    self.var_radio1=StringVar()
    radiobutn1=ttk.Radiobutton(Left_frame,variable=self.var_radio1,text="Take photo sample",value="Yes")
    radiobutn1.grid(row=4,column=0,padx=2,pady=2,sticky=W)
    radiobutn1.place(x=20,y=350,width=150,height=60)

    #buttons frame
    button_frame=LabelFrame(Left_frame,bd=2,relief=RIDGE,bg= "#a1c3d1")
    button_frame.place(x=20,y=400,width=526,height=45)
    
    #save button
    save_btn=Button(button_frame,command=self.add_data,width=10,text="Save",font=("Cambria",16),fg="white",bg="#376E6F")
    save_btn.grid(row=0,column=0)

    #update button
    up_btn=Button(button_frame,command=self.update_data,width=10,text="Update",font=("Cambria",16),fg="white",bg="#376E6F")
    up_btn.grid(row=0,column=1)

    #delete button
    del_btn=Button(button_frame,width=10,text="Delete",command=self.delete_data,font=("Cambria",16),fg="white",bg="#376E6F")
    del_btn.grid(row=0,column=2)

    #reset button
    re_btn=Button(button_frame,command=self.reset_data,width=10,text="Reset",font=("Cambria",16),fg="white",bg="#376E6F")
    re_btn.grid(row=0,column=3)
    
    #buttons2 frame
    button2_frame=LabelFrame(Left_frame,bd=2,relief=RIDGE,bg= "#a1c3d1")
    button2_frame.place(x=20,y=445,width=526,height=45)
    #photo sample button
    ps_btn=Button(button2_frame,width=21,text="Take photo",font=("Cambria",16),fg="white",bg="#376E6F")
    ps_btn.grid(row=0,column=0)
    #update sample button
    ups_btn=Button(button2_frame,width=21,text="Update photo",font=("Cambria",16),fg="white",bg="#376E6F")
    ups_btn.grid(row=0,column=1)


   
    #right label frame
    Right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Enter details",bg= "#a1c3d1",font=("Cambria",28))
    Right_frame.place(x=685,y=10,width=660,height=580)
    
    #profession
    ps_label=Label(Right_frame,text="Profession : ",font=("Cambria",20),fg="white",bg="#376E6F")
    ps_label.grid(row=0,column=0,padx=2,pady=2,sticky=W)
    ps_label.place(x=20,y=50,width=150,height=55)
    
    ps_entry=ttk.Entry(Right_frame,textvariable=self.var_proff,width=250,font=("Cambria",20))
    ps_entry.grid(row=0,column=1,padx=2,pady=2,sticky=W)
    ps_entry.place(x=180,y=50,width=250,height=55)

    #Last seen
    le_label=Label(Right_frame,text="Last Seen : ",font=("Cambria",20),fg="white",bg="#376E6F")
    le_label.grid(row=1,column=0,padx=2,pady=2,sticky=W)
    le_label.place(x=20,y=120,width=150,height=55)
    
    le_entry=ttk.Entry(Right_frame,textvariable=self.var_ls,width=250,font=("Cambria",20))
    le_entry.grid(row=1,column=1,padx=2,pady=2,sticky=W)
    le_entry.place(x=180,y=120,width=250,height=55)
    

    #description
    de_label=Label(Right_frame,text="Description : ",font=("Cambria",20),fg="white",bg="#376E6F")
    de_label.grid(row=1,column=0,padx=2,pady=2,sticky=W)
    de_label.place(x=20,y=190,width=150,height=55)
    
    de_entry=ttk.Entry(Right_frame,textvariable=self.var_desc,width=250,font=("Cambria",20))
    de_entry.grid(row=1,column=1,padx=2,pady=2,sticky=W)
    de_entry.place(x=180,y=190,width=250,height=55)

    #searching system
    #Search label frame
    Search_frame=LabelFrame(Right_frame,bd=2,relief=RIDGE,bg="#a1c3d1",text="Search System",font=("Cambria",25))
    Search_frame.place(x=0,y=260,width=657,height=85)

    Search_label=Label(Search_frame,text="Search by : ",font=("Cambria",15),fg="white",bg="#376E6F")
    Search_label.grid(row=0,column=0,padx=2,pady=2,sticky=W)
    
    #search comobobox
    search_combo=ttk.Combobox(Search_frame,font=("Cambria",16),width=10,state="read only")
    search_combo["values"]=("Select","Name","Last seen")
    search_combo.current(0)
    search_combo.grid(row=0,column=1,padx=2,pady=2,sticky=W)
    
    search_entry=ttk.Entry(Search_frame,width=10,font=("Cambria",20))
    search_entry.grid(row=0,column=2,padx=2,pady=2,sticky=W)

   #Search button
    search_btn=Button(Search_frame,width=8,text="Search",font=("Cambria",16),fg="white",bg="#376E6F")
    search_btn.grid(row=0,column=3,padx=2)

    #reset button
    showall_btn=Button(Search_frame,width=8,text="Show All",font=("Cambria",16),fg="white",bg="#376E6F")
    showall_btn.grid(row=0,column=4,padx=2)
    
    #table frame
    table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="#a1c3d1")
    table_frame.place(x=0,y=350,width=657,height=180)
    
    scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
    scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

    self.info_table=ttk.Treeview(table_frame,column=("Name","Age","Phone no.","Gender","Profession","Last seen","Description",),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)
    scroll_x.config(command=self.info_table.xview)
    scroll_y.config(command=self.info_table.yview)
    self.info_table.heading("Name",text="NAME")
    self.info_table.heading("Age",text="AGE")
    self.info_table.heading("Phone no.",text="PHONE NO.")
    self.info_table.heading("Gender",text="GENDER")
    self.info_table.heading("Profession",text="PROFESSION")
    self.info_table.heading("Last seen",text="LAST SEEN")
    self.info_table.heading("Description",text="DESCRIPTION")
    #self.info_table.heading("photo",text="PhotoSampleStatus")

    self.info_table["show"]="headings"
    self.info_table.column("Name",width=100)
    self.info_table.column("Age",width=50)
    self.info_table.column("Phone no.",width=100)
    self.info_table.column("Gender",width=100)
    self.info_table.column("Profession",width=100)
    self.info_table.column("Last seen",width=100)
    self.info_table.column("Description",width=100)
    #self.info_table.column("photo",width=100)


    self.info_table.pack(fill=BOTH,expand=1)
    self.info_table.bind("<ButtonRelease>",self.get_cursor)
    self.fetch_data()
  #function declaration

  def add_data(self):
   if self.var_name.get()=="" or self.var_age.get()==""  or self.var_phno.get()==""  or self.var_gender.get()=="" or self.var_proff.get()==""  or self.var_ls.get()==""  or self.var_desc.get()=="" :
     messagebox.showerror("Error","All fields are required",parent=self.root)
   else:
    try:
      conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="face_recognizer")
      my_cursor=conn.cursor()
      my_cursor.execute("insert into info values(%s,%s,%s,%s,%s,%s,%s)",(self.var_name.get(),self.var_age.get(),self.var_phno.get(),self.var_gender.get(),self.var_proff.get(),self.var_ls.get(),self.var_desc.get()))
      
      conn.commit()
      self.fetch_data()
      conn.close()
      messagebox.showinfo("successfully added")
    except Exception as es:
      messagebox.showerror("Error",f"due to:{str(es)}",parent=self.root)
    

  #function fetch data
  def fetch_data(self):
    conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="face_recognizer")
    my_cursor=conn.cursor()
    my_cursor.execute("select * from info")
    data=my_cursor.fetchall()
    if len(data)!=0:
      self.info_table.delete(*self.info_table.get_children())
      for i in data:
        self.info_table.insert("",END,values=i)
      conn.commit()
    conn.close()

  def get_cursor(self,event=""):
    cursor_focus=self.info_table.focus()
    content=self.info_table.item(cursor_focus)
    data=content["values"] 
    self.var_name.set(data[0]),self.var_age.set(data[1]),self.var_phno.set(data[2]),self.var_gender.set(data[3]),self.var_proff.set(data[4]),self.var_ls.set(data[5]),self.var_desc.set(data[6])

  #update
  def update_data(self):
    if self.var_name.get()=="" or self.var_age.get()==""  or self.var_phno.get()==""  or self.var_gender.get()=="" or self.var_proff.get()==""  or self.var_ls.get()==""  or self.var_desc.get()=="" :
     messagebox.showerror("Error","All fields are required",parent=self.root)
    else:
      try:
        Update=messagebox.askyesno("update","Do you want to update",parent=self.root)
        if Update>0:
         conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="face_recognizer")
         my_cursor=conn.cursor()
         my_cursor.execute("update info set NAME=%s,AGE=%s,PHONE NO. =%s,GENDER=%s,PROFESSION=%s,LAST SEEN=%s,DESCRIPTION=%s where NAME=%s",(self.var_age.get(),self.var_phno.get(),self.var_gender.get(),self.var_proff.get(),self.var_ls.get(),self.var_desc.get(),self.var_name.get()))
        else:
          if not Update:
            return
          messagebox.showinfo("success","Details successfully updated",parent=self.root)
          conn.commit()
          self.fetch_data()
          conn.close()
      except Exception as es:
       messagebox.showerror("Error",f"due to:{str(es)}",parent=self.root)


  #delete
  def delete_data(self):
    if self.var_name.get()=="":
      messagebox.showerror("Error",f"due to:{str(es)}",parent=self.root)
    else:
      try:
        delete=messagebox.askyesno("Delete page","Do you want to delete this",parent=self.root)
        if delete>0:
          conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="face_recognizer")
          my_cursor=conn.cursor()
          sql="delete from info where NAME=%s"
          val=(self.var_name.get(),)
          my_cursor.execute(sql,val)
        else:
          if not delete:
            return
        
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Delete","Successfully deleted",parent=self.root)
      except Exception as es:
       messagebox.showerror("Error",f"due to:{str(es)}",parent=self.root)

  #reset
  def reset_data(self):
    self.var_name.set("")
    self.var_age.set("")
    self.var_phno.set("")
    self.var_gender.set("")
    self.var_proff.set("")
    self.var_ls.set("")
    self.var_desc.set("")




if __name__=="__main__":
  root=Tk()
  obj=Details(root) 
  root.mainloop()