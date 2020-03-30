from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
#from tkinter import ttk
import tkinter.font as font
from irisclassifier import classify

master = Tk(className="  IRIS PROJECT  ")
master.geometry("800x500")

resultvar = StringVar()
resultvar.set("")
setosa_img = ImageTk.PhotoImage(Image.open("setosa.jpeg"))
vesicolor_img = ImageTk.PhotoImage(Image.open("versicolor.jpg"))
virginica_img = ImageTk.PhotoImage(Image.open("virginica.jpg"))

img_list = [ setosa_img,vesicolor_img,virginica_img,""]

img_index = 3


def calculateClick():
     #print(sp_sepal_ln.get()+" "+sp_sepal_wd.get()+" "+sp_petal_ln.get()+" "+sp_petal_wd.get())
     param_lst = []
     sepal_length = float(sp_sepal_ln.get())
     sepal_width = float(sp_sepal_wd.get())
     petal_length = float(sp_petal_ln.get())
     petal_width = float(sp_petal_wd.get())
     
     param_lst.append(sepal_length)
     param_lst.append(sepal_width)
     param_lst.append(petal_length)
     param_lst.append(petal_width)
     
     #print(classify(param_lst))
     
     #print(param_lst)
     outputList = classify(param_lst)
     resultvar.set(outputList[0].capitalize())
     img_index = outputList[1]
     lb_flowerimage.configure(image=img_list[img_index])

#sepal_lnvar = tk.DoubleVar()
#sepal_wdvar = tk.DoubleVar()
#petal_lnvar = tk.DoubleVar()
#petal_wdvar = tk.DoubleVar()

#sepal_lnvar = 6.0
#sepal_wdvar = 3.2
#petal_lnvar = 4.0
#petal_wdvar = 1.3

demoFont = font.Font(family="Arial",size=15)

lb_sepal_ln = Label(master,text="Sepal Length (cm)",font=("Arial",15))
sp_sepal_ln = Spinbox(master,font = demoFont,from_= 4.0,to=8.0,increment=0.1)

lb_sepal_wd = Label(master,text="Sepal Width (cm)",font=("Arial",15))
sp_sepal_wd = Spinbox(master, font = demoFont,from_= 1.9,to=4.5,increment=0.1)

lb_petal_ln = Label(master,text="Petal Length (cm)",font=("Arial",15))
sp_petal_ln = Spinbox(master, font = demoFont,from_= 0.9,to=7.0,increment=0.1)

lb_petal_wd = Label(master,text="Petal Width (cm)",font=("Arial",15))
sp_petal_wd = Spinbox(master, font = demoFont,from_= 0.0,to=2.6,increment=0.1)

lb_result = Label(master,text="Result",font=("Arial",15))
lb_flowername = Label(master,text="Demo Flower",font=("Arial",15),textvariable = resultvar)
lb_flowerimage = Label(master,font=("Arial",15),image=img_list[img_index])

calcBtn = Button(master,text="Predict",bg='skyblue',command = calculateClick)
demoFont = font.Font(family="Arial",size=15)
calcBtn['font'] = demoFont


iris_label = Label(master,text=" IRIS FLOWER CLASSIFIER ",font=("Arial",25))

lb_sepal_ln.place(x=30, y=47)
sp_sepal_ln.place(x=230,y=50,height=30,width=150)

lb_sepal_wd.place(x=30, y=97)
sp_sepal_wd.place(x=230,y=100,height=30,width=150)

lb_petal_ln.place(x=30, y=147)
sp_petal_ln.place(x=230,y=150,height=30,width=150)

lb_petal_wd.place(x=30, y=197)
sp_petal_wd.place(x=230,y=200,height=30,width=150)

lb_result.place(x = 570,y=47)
lb_flowername.place(x=550,y=97)
lb_flowerimage.place(x=450,y=127,height=250,width=250)

calcBtn.place(x = 100,y=270,height=50,width=100)

iris_label.place(x = 170, y = 400)



mainloop()