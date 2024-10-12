from tkinter import *
from tkinter.colorchooser import askcolor

class Paint(object):
    def __init__(self):
        self.default_color = "black"
        self.default_pensize = 3

        self.window = Tk()
        self.window.title("Colour paint")
        self.window.geometry("700x600")
        self.window.configure(background=("light grey"))

        self.penbutton = Button(self.window,text="pen",width=10,command=self.use_pen)
        self.penbutton.grid(row=1,column=0)

        self.brushbutton = Button(self.window,text="brush",width=10,command=self.use_brush)
        self.brushbutton.grid(row=1,column=1)

        self.colorbutton = Button(self.window,text="color",width=10,command=self.choose_colorbutton)
        self.colorbutton.grid(row=1,column=2)

        self.eraserbutton = Button(self.window,text="eraser",width=10,command=self.use_eraser)
        self.eraserbutton.grid(row=1,column=3)

        self.clearbutton = Button(self.window,text="clear",width=10,command=self.clear)
        self.clearbutton.grid(row=1,column=5)

        self.scale = Scale(self.window,from_=1,to=5,orient=HORIZONTAL)
        self.scale.grid(row=1,column=4)
        self.c = Canvas(self.window,bg="white",width=705,height=575)
        self.c.grid(row=2,columnspan=6)
        self.setup()
        self.window.mainloop()

    def setup(self):
        self.oldx = None
        self.oldy = None
        self.color = self.default_color
        self.eraser_on = False
        self.active_button = self.penbutton
        self.c.bind("<B1-Motion>",self.draw)
        self.c.bind("<ButtonRelease-1>",self.not_draw)

    def use_pen(self):
        self.Activate_button(self.penbutton)

    def use_eraser(self):
        self.Activate_button(self.eraserbutton,eraser_mode=True)

    def use_brush(self):
        self.Activate_button(self.brushbutton)
        self.line_width = 10

    def Activate_button(self,btn,eraser_mode=False):
        self.active_button.config(relief=RAISED)
        btn.config(relief=SUNKEN)
        self.active_button = btn
        self.eraser_on = eraser_mode

    def draw(self,event):
        if self.eraser_on == True:
            paint_color = "white"
        else:
            paint_color = self.color


        if self.active_button == self.brushbutton:
            self.line_width = self.scale.get()+10
        else:
            self.line_width = self.scale.get()


        if self.oldx and self.oldy:
            self.c.create_line(self.oldx,self.oldy,event.x,event.y,width=self.line_width,fill=paint_color,capstyle = ROUND,smooth = True,splinesteps=40)
        self.oldx = event.x
        self.oldy = event.y

    def not_draw(self,event):
        self.oldx = None
        self.oldy = None

    def choose_colorbutton(self):
        self.eraser_on = False
        self.color = askcolor(color=self.color)[1]

    def clear(self):
        self.c.delete("all")



        

Paint()
