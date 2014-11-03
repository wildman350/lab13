#########################################
#
#         70-100pt - Making a game
#
#########################################


# 70pt - Add buttons for left, right and down that move the player circle
# 100pt - using lab 11 as an example, add in three horizontally scrolling "enemies"
# Make them scroll at different speeds and directions.



from Tkinter import *
root = Tk()

drawpad = Canvas(root, width=800,height=600, background='white')
player = drawpad.create_oval(390,580,410,600, fill="red")
rectangle = drawpad.create_rectangle(140, 100, 100, 120, fill='blue')
rectangle2 = drawpad.create_rectangle(600, 490, 540, 510, fill='green')
rectangle3 = drawpad.create_rectangle(300, 300, 320, 320, fill='red')
dir1 = 5
dir2 = 5
dir3 = 5


def animate2():
    global dir1
    x1, y1, x2, y2 = drawpad.coords(rectangle)
    if x2 > drawpad.winfo_width(): 
        dir1 = -6
    elif x1 < 0:
        dir1 = 6
    drawpad.move(rectangle,dir1,0)
    drawpad.after(5, animate2)
animate2()

def animate3():
    global dir2
    x1, y1, x2, y2 = drawpad.coords(rectangle2)
    if x2 > drawpad.winfo_width(): 
        dir2 = -5
    elif x1 < 0:
        dir2 = 5
    drawpad.move(rectangle2,dir2,0)
    drawpad.after(5, animate3)
animate3()

def animate4():
    global dir3
    x1, y1, x2, y2 = drawpad.coords(rectangle3)
    if x2 > drawpad.winfo_width(): 
        dir3 = - 3
    elif x1 < 0:
        dir3 = 3
    drawpad.move(rectangle3,dir3,0)
    drawpad.after(5, animate4)
animate4()

class MyApp:
	def __init__(self, parent):
       	    global drawpad
       	    self.myParent = parent  
       	    self.myContainer1 = Frame(parent)
       	    self.myContainer1.pack()
       	    self.up = Button(self.myContainer1)
       	    self.up.configure(text="up", background= "yellow")
       	    self.up.grid(row=0,column=0)
       	    self.up.bind("<Button-1>", self.upClicked)
       	    
       	    self.down = Button(self.myContainer1)
       	    self.down.configure(text="down", background= "green")
       	    self.down.grid(row=0,column=1)
       	    self.down.bind("<Button-1>", self.downClicked)
       	    
       	    self.right = Button(self.myContainer1)
       	    self.right.configure(text="right", background= "red")
       	    self.right.grid(row=0,column=3)
       	    self.right.bind("<Button-1>", self.rightClicked)
       	    
       	    self.left = Button(self.myContainer1)
       	    self.left.configure(text="left", background= "blue")
       	    self.left.grid(row=0,column=2)
       	    self.left.bind("<Button-1>", self.leftClicked)
       	    
       	    
       	    drawpad.pack(side=BOTTOM)
	
	def animate(self):
	    global drawpad
	    global player
	    	
		
	def upClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,0,-20)
        
        def downClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,0,20)
	
	def rightClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,20,0)
	   
	def leftClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,-20,0)
		
app = MyApp(root)
root.mainloop()