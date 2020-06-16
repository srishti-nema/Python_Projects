try:
    # for Python2
    from Tkinter import *   ## notice capitalized T in Tkinter
except ImportError:
    # for Python3
    from tkinter import *   ## notice lowercase 't' in tkinter here
from PIL import ImageTk,Image

root=Tk()

root.title('Memes that make you cry+laugh')
#root.iconbitmap('/home/srishti/Python_Projects/Image_viewer/pics_viewer/meme_icon.ico')

my_img1=ImageTk.PhotoImage(Image.open('/home/srishti/Python_Projects/Image_viewer/pics_viewer/1.jpg'))
my_img2=ImageTk.PhotoImage(Image.open('/home/srishti/Python_Projects/Image_viewer/pics_viewer/2.jpg'))
my_img3=ImageTk.PhotoImage(Image.open('/home/srishti/Python_Projects/Image_viewer/pics_viewer/3.jpg'))
my_img4=ImageTk.PhotoImage(Image.open('/home/srishti/Python_Projects/Image_viewer/pics_viewer/4.jpg'))
my_img5=ImageTk.PhotoImage(Image.open('/home/srishti/Python_Projects/Image_viewer/pics_viewer/5.jpg'))

image_list=[my_img1,my_img2,my_img3,my_img4,my_img5]

status=Label(root,text="Image 1 of "+str(len(image_list)),bd=1,relief=SUNKEN,anchor=E)#status bar sunken down at the bottom and bd for border and anchor is the direction of the text
my_label=Label(image=my_img1)
my_label.grid(row=0,column=0,columnspan=3)

def forward(image_number):
	global my_label
	global button_forward
	global button_back

	my_label.grid_forget()
	my_label=Label(image=image_list[image_number-1])
	button_forward=Button(root,text=">>",command=lambda:forward(image_number+1))
	button_back=Button(root,text="<<",command=lambda:back(image_number-1))

	if image_number==5:
		button_forward=Button(root,text=">>",state=DISABLED)

	my_label.grid(row=0,column=0,columnspan=3)
	button_back.grid(row=1,column=0)
	button_forward.grid(row=1,column=2)

	status=Label(root,text="Image "+ str(image_number)+  " of "+str(len(image_list)),bd=1,relief=SUNKEN,anchor=E)
	status.grid(row=2,column=0,columnspan=3,sticky=W+E)#sticky to west and east


def back(image_number):
	global my_label
	global button_forward
	global button_back

	my_label.grid_forget()
	my_label=Label(image=image_list[image_number-1])
	button_forward=Button(root,text=">>",command=lambda:forward(image_number+1))
	button_back=Button(root,text="<<",command=lambda:back(image_number-1))

	if image_number==1:
		button_back=Button(root,text="<<",state=DISABLED)

	my_label.grid(row=0,column=0,columnspan=3)
	button_back.grid(row=1,column=0)
	button_forward.grid(row=1,column=2)

	status=Label(root,text="Image " + str(image_number) +" of "+str(len(image_list)),bd=1,relief=SUNKEN,anchor=E)
	status.grid(row=2,column=0,columnspan=3,sticky=W+E)#sticky to west and east



button_back=Button(root,text="<<",command=back,state=DISABLED)#lambda not needed for first image, initial state is disabled for back button
button_exit=Button(root,text="Exit",command=root.quit)
button_forward=Button(root,text=">>",command=lambda:forward(2))

button_back.grid(row=1,column=0)
button_exit.grid(row=1,column=1)
button_forward.grid(row=1,column=2,pady=10)

status.grid(row=2,column=0,columnspan=3,sticky=W+E)#sticky to west and east

root.mainloop()