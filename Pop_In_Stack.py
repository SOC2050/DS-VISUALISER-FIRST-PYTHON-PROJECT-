import turtle
from turtle import*
import __main as d
import __stack as s
import tkinter as tk

screen=None

stacklist =[ "a" , "D" , "H" , "S" , "K" , "A"]


def pop(stacklist , screen):
     pop_midposition=[]
     
     d.createObject('pop_position' , screen ,  visibility=True, speed=0, color="black")
     d.createObject('pop_stack' , screen ,  visibility=True, speed=0, color="black")
     d.createObject('pop_insert' , screen,  visibility=True, speed=1, color="black")
     d.createObject('pop_box' , screen,  visibility=True, speed=1, color="black")
     
     d.createObject('pop_arrow' , screen,  visibility=True, speed=1, color="black")
     d.createObject('pop_top' , screen,  visibility=True, speed=2, color="black")
     
     pop_position = d.pop_position
     pop_stack = d.pop_stack
     pop_insert = d.pop_insert
     pop_box = d.pop_box
     pop_arrow = d.pop_arrow
     pop_top = d.pop_top

     d.Bwid=150
     s.stack( pop_stack , xcor = -250 , ycor = 400 , height=1300)
     
     

     
     
     for  num in  stacklist:
         
         ind=stacklist.index(num)
         pos=(d.Bwid+14)*ind
         
         
         d.rect(pop_insert , x=s.startx,y= s.starty+pos ,length=260, width=150, cradius=20,data=num ,stroke=1, fill_color="yes" , color="#C1AEFC" , Font =12 )
         
         current=[]
         current.append(pop_insert.xcor())
         current.append(pop_insert.ycor())
         pop_midposition.append(current)
         
         #pop_iarrow.clear()
         pop_box.clear()

     
     
     for i in range (len(stacklist)-1 , -1 , -1):
         pos=(d.Bwid+14)*i
         s.arrow( pop_top , i ,  col="green", text="Top" , Position=pop_midposition )
         pop_arrow.left(90)
         s.curveArrow (pop_arrow, xcor=-90 , ycor =350 , radius=3 , base = 40 , height = 120 ,  color="#C1AEFC")
         pop_arrow.right(90)         
         d.rect(pop_box , x=210 , y= 480 ,length=260, width=150, cradius=20,data=stacklist[i]  ,stroke=2 , fill_color="yes" , color="#C1AEFC" , Font =12 )
     
         
         d.rect(pop_position , x=pop_midposition[i][0] - d.Blen*0.422  , y= pop_midposition[i][1] - d.Bwid*0.25   ,length=260, width=150, cradius=20,data=" " ,stroke=2 , fill_color="yes" , color="white" , Font =12 )
         
         pop_top.clear()
         pop_arrow.clear()
         pop_box.clear()
     
     
     
     
     

#--------------  Function to handle the window closing event -------------- #

def Pop(screen):
    try:
  
        pop(stacklist , screen)
        d.setPosition()
        time.sleep(5)
        
    except turtle.Terminator:
        pass  # Catch the Terminator error and do nothing
    except Exception as e:
        pass 
        print("An error occurred:", str(e))  # Handle any other exception and print an error message


##### ----------------- Main Driver Program ------------------- #####

# Set the close_window function to handle the window closing event


Pop(screen)

