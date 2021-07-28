from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Adding Icons and Images')
# Changing icon
root.iconbitmap('C:/Users/Helen/Downloads/startup_rocket_spaceship_launch_business_icon_191142 (1).ico')

# Adding an image
my_img = ImageTk.PhotoImage(Image.open('C:/Users/Helen/Desktop/cute.jpg'))
my_label = Label(image=my_img)
my_label.pack()

# Button for ending program
button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()

root.mainloop()