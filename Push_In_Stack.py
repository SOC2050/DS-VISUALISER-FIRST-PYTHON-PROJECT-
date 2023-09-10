
import turtle
from turtle import*
import __main as d
import __stack as s
import tkinter as tk

screen=None

stacklist =[ "a" , "D" , "H" , "S" , "K" , "A"]


def push(stacklist , screen):
     midposition=[]
     
     d.createObject('p_position' , screen ,  visibility=True, speed=0, color="black")
     d.createObject('p_stack' , screen ,  visibility=True, speed=0, color="black")
     d.createObject('p_insert' , screen,  visibility=True, speed=0 , color="black")
     d.createObject('p_box' , screen,  visibility=True, speed=0, color="black")
     
     d.createObject('p_iarrow' , screen,  visibility=True, speed=0 , color="black")
     d.createObject('p_top' , screen,  visibility=True, speed=0 , color="black")
     
     p_position = d.p_position
     p_stack = d.p_stack
     p_insert = d.p_insert
     p_box = d.p_box
     p_iarrow = d.p_iarrow
     p_top = d.p_top

     d.Bwid=150
     s.stack( p_stack , xcor = -50 , ycor = 400 , height=1300)
     for i in range (len(stacklist)):
         pos=(d.Bwid+14)*i
         
         d.rect(p_position , x=s.startx,y= s.starty+pos ,length=260, width=150, cradius=20,data=" " ,stroke=0 , fill_color="no" , color="#C1AEFC" , Font =12 )
         current=[]
         current.append(p_position.xcor())
         current.append(p_position.ycor())
         midposition.append(current)
     
     for  num in  stacklist:
         
         ind=stacklist.index(num)
         pos=(d.Bwid+14)*ind
         
         d.rect(p_box , x=s.stackx - 255 ,y= s.stacky + 120 ,length=260, width=150, cradius=20,data=num ,stroke=1, fill_color="yes" , color="#C1AEFC" , Font = 12 )
         s.curveArrow (p_iarrow , xcor = s.stackx-30 , ycor =s.stacky+200  , color="#C1AEFC")         
         
         p_top.clear()
         s.arrow( p_top , ind  ,  col="green", text="Top" , Position=midposition )
         d.rect(p_insert , x=s.startx,y= s.starty+pos ,length=260, width=150, cradius=20,data=num ,stroke=1, fill_color="yes" , color="#C1AEFC" , Font =12 )
         
         p_iarrow.clear()
         p_box.clear()



#--------------  Function to handle the window closing event -------------- #

def Push(screen):
    try:
  
        push(stacklist , screen)
        d.setPosition()
        time.sleep(5)
        
    except turtle.Terminator:
        pass  # Catch the Terminator error and do nothing
    except Exception as e:
        pass 
        print("An error occurred:", str(e))  # Handle any other exception and print an error message


##### ----------------- Main Driver Program ------------------- #####

# Set the close_window function to handle the window closing event

Push(screen)

