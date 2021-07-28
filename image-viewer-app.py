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

# Defining functionalities of buttons
def forward(image_num):
    global my_label
    global button_forward
    global button_back

    # want to take the image that's already there and get rid of it
    my_label.grid_forget()

    # creating next image and changing button meanings
    my_label = Label(image=img_list[image_num-1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_num+1))
    button_back = Button(root, text="<<", command=lambda: back(image_num-1))

    # exception: end of list
    if image_num == len(img_list):
        button_forward = Button(root, text=">>", state=DISABLED)

    # placing new image and buttons on screen
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

def back(image_num):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()

    my_label = Label(image=img_list[image_num-1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_num+1))
    button_back = Button(root, text="<<", command=lambda: back(image_num-1))

    if image_num == 1:
        button_back = Button(root, text="<<", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

# Create buttons for moving pictures
button_back = Button(root, text="<<", command=back, state=DISABLED)
button_exit = Button(root, text="Exit Program", command=root.quit)
button_forward = Button(root, text=">>", command=lambda: forward(2))

# Placing buttons on screen
button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)

root.mainloop()