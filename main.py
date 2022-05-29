from tkinter import*
from tkinter import ttk
from PIL import Image
from PIL import ImageTk
from details import Details

class Face_Recognition_System:
  def __init__(self,root):
    self.root=root
    self.root.geometry("1530x790+0+0")
    self.root.title("Face Recognition System")

    

    #bg image
    img3=Image.open(r"C:\Users\admin\Desktop\face recog\collage_images\bgcolour3.png")
    img3=img3.resize((1530,790),Image.ANTIALIAS)
    self.photoimg3=ImageTk.PhotoImage(img3)

    bg_img=Label(self.root,image=self.photoimg3)
    bg_img.place(x=0,y=0,width=1530,height=790)

    title_lbl=Label(bg_img,text="Welcome",font=("Cambria",40,),bg="#376E6F",fg="white")
    title_lbl.place(x=0,y=0,width=1530,height=55)
    
    #student button
    img4=Image.open(r"C:\Users\admin\Desktop\face recog\collage_images\bgcolour1.png")
    img4=img4.resize((220,220),Image.ANTIALIAS)
    self.photoimg4=ImageTk.PhotoImage(img4)

    b1=Button(bg_img,image=self.photoimg4,command=self.details,cursor="hand2")
    b1.place(x=100,y=250,width=220,height=220)

    b1_1=Button(bg_img,text="Details",command=self.details,cursor="hand2",font=("Cambria",20,),bg="#376E6F",fg="white")
    b1_1.place(x=100,y=450,width=220,height=40)

     #detect button
    img5=Image.open(r"C:\Users\admin\Desktop\face recog\collage_images\bgcolour1.png")
    img5=img5.resize((220,220),Image.ANTIALIAS)
    self.photoimg5=ImageTk.PhotoImage(img5)

    b1=Button(bg_img,image=self.photoimg5,cursor="hand2")
    b1.place(x=400,y=250,width=220,height=220)

    b1_1=Button(bg_img,text="Detector",cursor="hand2",font=("Cambria",20,),bg="#376E6F",fg="white")
    b1_1.place(x=400,y=450,width=220,height=40)
    

    #found button
    img6=Image.open(r"C:\Users\admin\Desktop\face recog\collage_images\bgcolour1.png")
    img6=img6.resize((220,220),Image.ANTIALIAS)
    self.photoimg6=ImageTk.PhotoImage(img6)

    b1=Button(bg_img,image=self.photoimg6,cursor="hand2")
    b1.place(x=700,y=250,width=220,height=220)

    b1_1=Button(bg_img,text="Found",cursor="hand2",font=("Cambria",20,),bg="#376E6F",fg="white")
    b1_1.place(x=700,y=450,width=220,height=40)
    
    #train button
    img7=Image.open(r"C:\Users\admin\Desktop\face recog\collage_images\bgcolour1.png")
    img7=img7.resize((220,220),Image.ANTIALIAS)
    self.photoimg7=ImageTk.PhotoImage(img7)

    b1=Button(bg_img,image=self.photoimg7,cursor="hand2")
    b1.place(x=1000,y=250,width=220,height=220)

    b1_1=Button(bg_img,text="Train",cursor="hand2",font=("Cambria",20,),bg="#376E6F",fg="white")
    b1_1.place(x=1000,y=450,width=220,height=40)

 #function button

  def details(self):
    self.new_window=Toplevel(self.root)
    self.app=Details(self.new_window)








if __name__=="__main__":
     root=Tk()
     obj=Face_Recognition_System(root) 
     root.mainloop()

