from tkinter import *
from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfile 
import time
import cv2
import imageio
from tensorflow.keras.preprocessing.image import img_to_array, load_img
import tkinter as tk, threading
from tkinter.filedialog import askopenfile 
from tkinter import messagebox
import tensorflow as tf
import glob
import numpy as np




import tkinter
import os
from tkinter import *

import matplotlib.pyplot as plt    


from PIL import Image, ImageTk
path_to_model = r'A:\TechieYan projects\AI\Brain-Tumour-Detection-using-CNN-main\model\weights_best_87.hdf5'
model = tf.keras.models.load_model(path_to_model)

print(model)
root = Tk()
root.title('Brain Tumor Detection using CNN')
root.geometry("1200x600")
p = PhotoImage(file=r"brain2.png")
l = Label(root,image=p)
l.place(x=0,y=0)


file_path = ""
def open_file():
    global file_path
    file_path = askopenfile(mode='r', filetypes=[('Files', '*.*')])
    print(file_path.name)
    if file_path is not None:
        pass


def uploadFiles():
    pb1 = Progressbar(
        root, 
        orient=HORIZONTAL, 
        length=300, 
        mode='determinate'
        )
    pb1.pack()
    for i in range(5):
        root.update_idletasks()
        pb1['value'] += 20
        time.sleep(1)
    pb1.destroy()
    Label(root, text='File Uploaded Successfully!', foreground='green').pack()




def save_file():
    
    #print(file_path.name)
    _dRawMap = {8:r'\b', 7:r'\a', 12:r'\f', 10:r'\n', 13:r'\r', 9:r'\t', 11:r'\v'}

    def getRawGotStr(s):
        return r''.join( [ _dRawMap.get( ord(c), c ) for c in s ] )

    path = getRawGotStr(file_path.name) #This is your image file path
    #print("os ",path) 

    image_path = path
    #print(image_path)
    read_image = imageio.get_reader(image_path)
    #print(video)

    def stream(label):
        for image in read_image.iter_data():
            frame_image = ImageTk.PhotoImage(Image.fromarray(image))
            label.config(image=frame_image)
            label.image = frame_image

    if __name__ == "__main__":

        my_label = tk.Label(root)
        my_label.pack()
        thread = threading.Thread(target=stream, args=(my_label,))
        thread.daemon = 1
        thread.start()



    print("final ",path)


    img = plt.imread(path)

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(img_gray, (5, 5), 0)   
    thresh = cv2.threshold(gray, 45, 255, cv2.THRESH_BINARY)[1]
    thresh = cv2.erode(thresh, None, iterations=2)
    thresh = cv2.dilate(thresh, None, iterations=2)
    img_half = cv2.resize(img, (255, 255))
    img_half = cv2.cvtColor(img_half, cv2.COLOR_BGR2GRAY)
    x = img_to_array(img_half)
    x = np.array(x).reshape(-1, 255, 255, 1)
    #print(x.shape)


    prediction = model.predict(x)
    if prediction[0] > 0.5:
        print("YES")
        messagebox.showinfo("Result","The person is having Brain Tumor")
    else:
        print("NO")
        messagebox.showerror("Result","The Person is not having Brain Tumor.")
    



v_d = Label(root,text="Brain Tumor Detection using CNN", font=("Times New Roman",30), bd=8, relief=SUNKEN)
v_d.pack(side=TOP, padx=1.0, pady=0.5)


choose_file_button = Button(
    root, 
    text ='Choose File',        
    command = lambda:open_file())
choose_file_button.place(x=50, y=200)
#choose_file_button.pack()


upload_file_button = Button(
    root, 
    text='Upload Files', 
    command=uploadFiles
    )
upload_file_button.place(x=50, y=300)
#upload_file_button.pack(pady=10)



path_button = Button(root, text= "Click here to run the file", command= save_file)
path_button.place(x=50, y=400)
#path_button.pack(pady=80)



root.mainloop()