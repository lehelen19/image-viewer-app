from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Adding Icons and Images')

my_img1 = ImageTk.PhotoImage(Image.open('C:/Users/Helen/Desktop/cute.jpg'))
my_img2 = ImageTk.PhotoImage(Image.open('C:/Users/Helen/Desktop/mit.png'))
my_img3 = ImageTk.PhotoImage(Image.open('C:/Users/Helen/Desktop/saved/swag space.jpg'))

img_list = [my_img1, my_img2, my_img3]

my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3) # Below the image, 3 buttons

# Create buttons for moving pictures
button_back = Button(root, text="<<")
button_exit = Button(root, text="EXXIT PROGRAM", command=root.quit)
button_forward = Button(root, text=">>")

root.mainloop()