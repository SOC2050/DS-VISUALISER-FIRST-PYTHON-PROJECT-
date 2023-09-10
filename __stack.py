import turtle
from turtle import*
import __main as d
import math 

stackx=0
stacky=0
smidx=0
smidy=0
startx =0
starty =0

#-------------- Function to create Stack Model ---------------- #

def stack( t , xcor = 0 , ycor = 0 , height = 1000 , width=300 ,    cradius=40 , color = "purple" ):
    
    global smidx
    global smidy
    global startx
    global starty
    global stackx
    global stacky

    stackx=xcor
    stacky=ycor
    t.up()
    t.goto( xcor , ycor )
    
    t.down()
    len = height - 2 * cradius 
    wed = width - 2 * cradius 
    t.pensize(15)
    t.pencolor(color)
    t.left(180)
    t.circle(cradius*0.5,-90)
    t.right(180)
    
    
    t.goto(t.xcor() , t.ycor() - len )
    smidx=t.xcor()
    smidy=t.ycor()
    t.circle(cradius,90)
    
    t.goto(t.xcor() + wed , t.ycor() )
    t.circle(cradius,90)
    t.goto(t.xcor() , t.ycor() + len )
    t.right(180)
    t.circle(cradius*0.5,-90)
    t.up()
    t.pensize(5)    
    t.goto(smidx+width/2 , smidy-cradius*4)
    t.write("Stack", align='center', font=("normal" , 15, 'bold'))
    startx=smidx+40
    starty=smidy- 23
    
    t.goto(smidx , starty)
    t.up()
    t.pensize(1)
    n=height//d.Bwid 
    dist=d.Bwid+7
    dis=dist
    for i in range (n-1):
        
        t.goto(smidx , starty+dis)
        t.goto(t.xcor()- 35, t.ycor()-50)
        t.write(i , align='center')
        t.goto(t.xcor()+ 35, t.ycor()+50)
        t.down()
        t.goto(smidx+width, t.ycor())
        dis+=dist+7
        t.up()




# ------------ Function for Creating Curve Arrow -----------

def curveArrow (t, xcor=0 , ycor =0 , radius=3 , base = 40 , height = 120 ,  color="#C1AEFC"):
      """ Function for creating Curve Arrow For showing elements are popping out from Stack"""
      
      t.hideturtle()  
      t.up()
      
      t.goto(xcor , ycor)
      
      t.pencolor(color)

      t.fillcolor(color)
      t.shapesize(9,5)
      t.begin_fill()
      t.speed(0)
      for x in range(90):
           if x > 20:
                 t.showturtle()
           t.forward(radius)
           t.right(1)
      t.speed(0)
      t.hideturtle()
      t.right(90)      
      t.forward(base)
      t.left(180-60)
      t.forward(height)
      t.left(180-60)      
      t.forward(height)
      t.left(180-60)
      t.forward(base)
      t.right(90)
      
      for x in range (97):
            t.forward(radius)
            t.left(1+x/3000)               
      t.end_fill()
      t.up()
      t.right(14)
      t.forward(9)
      t.right(180)
      t.left(5.5)

#-------------------- Function End ---------------------



#------------ Function for Creating Arrow on i th position for everyy iteration -------------#
                  
def arrow( t , pos , xcor=None , ycor =None , col="green", text=None , Position= None ) :
           
     # t - turtle object for creating Arrow
     # pos - It is the position where arrow would be draw i.e i th or j th position of the array 
     # x -  x coordinate of arrow
     # y - y coordinate of arrow
     # col -  color which user want to give arrow 
     # text - Text Massage that user want to print top of arrow
     

      
      #t.speed(0)
      
      ln=d.Bwid*0.5
  
      _ln=ln/3
      _hig=math.sqrt(math.pow(ln,2)-math.pow(ln/2,2)) +_ln
      arrow_length= 34.9857
      deviation_angle = 120.9641
     
      
     
      t.up()
      if xcor  is not None or  ycor is not None :
            t.goto(xcor , ycor)
      else :
            t.goto( Position [pos][0] + d.Blen*0.65  , Position [pos][1]+d.Bwid*0.25)
      t.right(90)
      
      t.left((90-30))
      
      t.down()              
      #t.hideturtle()
      
      t.pencolor(col)       
      t.fillcolor(col)
      t.begin_fill()
      
      t.forward(ln)
      t.left(120)
      t.forward(_ln)
      t.right(90)
      t.forward(_ln)
      t.left(90)
      t.forward(_ln)
      t.left(90)
      t.forward(_ln)
      t.right(90)
      t.forward(_ln)
      t.left(120)
      t.forward(ln)
      
      t.end_fill()
      t.up()
      t.left(60)
      t.goto(t.xcor()+_hig,t.ycor()-20)
      t.down()
      
      
      if text is not None :
            t.write(text,font=("verydana",7, "normal"),align='left')  
      t.left(90)
      #d.rect(t,x=Position[pos][0]-d.Blen*0.38 , y=Position[pos][1]- d.Bwid*0.25,length=d.Blen, width=d.Bwid , cradius= d.cr, stroke=3,fill_color="no" , color="#FF9A00")