import __main as d
import turtle
from turtle import*
import time
import math

nodelen=0
nodewid=0
llGap=40
arrowPos =[]




def node (t , xcor=None , ycor=None , lengthN=None , widthN=None , cradiusN=None , dataN=None  ,IndexN=True , indexN=None):
         
         global nodelen 
         global nodewid
         nodelen=lengthN
         nodewid=widthN
         
         t.hideturtle()
         d. rect(t, x=d.horizontal+xcor , y=d.vertical - ycor  , length=lengthN , width=widthN , cradius=cradiusN , data=dataN , stroke= 1 , color="#B799FF", Index=IndexN, index=indexN)
        
         currentPos=[]
         x1=t.xcor()
         y1 =t.ycor()
         currentPos.append(x1)
         currentPos.append(y1)
         arrowPos.append(currentPos)
               
         t.up()
         
         t.goto(t.xcor()+lengthN//2+16 , t.ycor() - widthN*1/4)
         t.down()
         d. rect(t  , length=lengthN*0.4 , width=widthN , cradius=cradiusN ,  data=" " , stroke=1,color="#9575DE" )
      
#------- Function to create LinkedList ---------#

def LinkedList(t , t1, start ,end , arr, xPos=0 , yPos=0 , length=None , width=None  ,clear="yes", null=None ):
       
      xpos=xPos 
      hxprev=0
      hyprev=0
      x1=0
      y1=0
      
      for i in range (len(arr)):
             node (t , xcor=xpos , ycor=yPos , lengthN=length , widthN=width , cradiusN=10 , dataN=arr[i] , indexN=i )
             link(t1  , xcor=t.xcor()+4, ycor=t.ycor()+width*0.25 )
             
             xpos+=llGap+nodelen+(nodelen*0.4)+17
                        
             d.rect(null, x=t1.xcor()+17 ,y=t1.ycor()-width*0.5,length=90, width=100, cradius=10,data="Null",stroke=1,color="#C1AEFC")
                         
             if i ==0:
                   hxprev=t.xcor()-nodelen*0.75
                   hyprev=t.ycor()+width*0.81
                   head( start , x=hxprev , y=hyprev ,col="green",text="head=tail")
             
             if i >=1:
                   if i == 1:
                         start.clear()
                         head( start , x=arrowPos[0][0] , y=arrowPos[0][1]+80,col="green",text="head")
                   end.clear()
                   head( end , x=arrowPos[i][i-i],y=arrowPos[i][i - i +1]+80,col="green",text="tail")
                              
             #time.sleep(1.4)
            
      if clear=="yes":       
          arrowPos.clear()
             
             
#------Function for Creating Single Link of LinkedList-----

def link(t ,  xcor= None , ycor = None, Gap =40 ,  color ="red" , size=5):       
                        x=nodelen*0.4
                        xx=x/2+2
                        t.up()
                        t.goto(xcor+xx  , ycor )
                        t.pencolor(color)
                        t.pensize(size)
                        t.down()
                        t.forward(Gap)
                        t.right(30.9573)
                        t.backward(10)
                        t.forward(10)
                        t.left(30.9573+30.9573)
                        t.backward(10)
                        t.pensize(1)
                        t.pencolor('purple')
                        t.up()
                        t.forward(10)
                        t.left(90-30.9573)
                        t.right(90)
                        t.down()
      
#------Function for Creating Single Link of LinkedList is Finished------


#------------ Function for Creating Arrow on i th position for everyy iteration -------------#
                  
def head( t , pos =0 , x=0 ,y=0 , col="green",text=None,dir=None) :
           
     # t - turtle object for creating Arrow
     # pos - It is the position where arrow would be draw i.e i th or j th position of the array 
     # x -  x coordinate of arrow
     # y - y coordinate of arrow
     # col -  color which user want to give arrow 
     # text - Text Massage that user want to print top of arrow
     
      #if not isinstance(t, Turtle) :
           #raise TypeError("t must be Turtle object")
          
      t.speed(0)
      
      ln=nodelen *70/100
  
      _ln=ln//3
      _hig=math.sqrt(math.pow(ln,2)-math.pow(ln/2,2)) +_ln
      arrow_length= 34.9857
      deviation_angle = 120.9641     
     
      t.up()
      
      t.goto(x,y)
  
      t.left((90-30))
    
      t.down()              
      t.hideturtle()
      
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
      t.left(90)
      if dir is None :
          t.forward(_hig)
      else :
          t.forward(_hig+_hig*0.75)
      t.down()
      t.right(90)
      
      
      if text is not None :
            t.write(text,font=("verydana",7, "normal"),align='center')
      if pos is not None :
           d.rect(t,x=arrowPos[pos][0]-nodelen*0.37 , y=arrowPos[pos][1]- nodewid*0.25,length= nodelen, width=nodewid , cradius= 10 , stroke=2 ,fill_color="no" , color="#FF9A00")
      
#------------ End of Drawing Arrow in i th position---------------
