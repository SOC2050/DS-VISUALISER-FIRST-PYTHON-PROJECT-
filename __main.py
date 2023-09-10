from turtle import *
import time 
import turtle 
import math


Width = 0
Height = 0
cnt=0

horizontal=-550
vertical= 1000

turtles = []
Blen=0
Bwid=0
cr=0
Gap=6
Position=[]
#num=[67,43,39,90,56,55,1]
num=[10,9,22,17,0,1,2]

extra=[]
extra=num.copy()
Input=[1,5,4,8,9,3,0,6]

# ------------ Function to set Position of Animation ------------- #

def setPosition( xPos=None , yPos=None ):
      
      # xPos - This is the x coordinate or x position of Animation where from start
      # yPos - This is the x coordinate or x position of Animation where from start
      
      global horizontal
      global vertical
      
      if xPos is not None and yPos is not None:
            horizontal+=xPos
            vertical -=yPos
      else:
          horizontal=-250
          vertical= 350
          



# ----------Function for creating turtle object ---------- #

def createObject(name_obj, window , x=0, y=0, visibility=True, speed=6, color="black"):
    
    # name_obj - This is the name of a turtle object that should be unique
    # x - x coordinate of Turtle object where want to set 
    # y - x coordinate of Turtle object where want to set
    # visibility - This is the mode of Turtle object i.e( show = True  or hide = False Turtle object )
    # speed - This is the speed of  working of a Turtle object
    # color - This is the color of pen of Turtle object
     
    """Function for creating turtle object with the object name , location , visibility , speed and colour"""
    global Width
    global Height 
    global cnt
    obj_name =RawTurtle( window , visible=visibility)
    obj_name.up()
    obj_name.goto(x, y)
    obj_name.down()
    obj_name.speed(speed)
    obj_name.pencolor(color)
    turtles.append(obj_name)
    globals()[name_obj] = obj_name
    
    if cnt <1:
         Width = window.window_width()
         Height = window.window_height()

    cnt+=1

# ----------Function for Destroying turtle object ---------- #

def destroyObjects():
    
    """Function for destroying objects means resetting all objects and clearing the drawing created by that particular object"""
    
    global turtles
    for obj in turtles:
        obj.up()
        obj.clear()
        obj.reset()
        obj.hideturtle()
        #screen.bey()
    turtles = []
   
 
# ----------Function for creating Ractangle ---------- #      
       
def rect(t, x=None,y=None,length=0, width=0, cradius=0,data=None,stroke=1, fill_color="yes" , color="#C1AEFC",Index=False,index=None , name=None , Font=6):
    
    # t - turtle object for creating Arrow
    # x -  x coordinate of Ractangle 
    # y - y coordinate of Ractangle
    # length - Length of a Ractangle of an Array   
    # width - Width of a Ractangle of an Array
    # (Note : The above lenth and width would set to Orginal Length  and Width of Ractangle everywhere in the whole Program)
    # cradius - This is a corner radius of Ractangle box (i.e who much corner should be round )
    # data - Original Array i th position data which would printed at centre , left , right of the Ractangle i.e( array [ i ] )
    # stroke - This is the size of Edge of a Ractangle 
    # color - This is the color which user wants to give to Ractangles 
    
    
    """ function for drawing rectangle """
    try :
        
        global Blen
        Blen=length
        global Bwid
        Bwid=width
        global cr
        cr=cradius

        len=length-2*cradius 
        wed=width-2*cradius 
        t.speed(0)
        t.pensize(stroke)
        t.pencolor(color)
        t.hideturtle()
        if x is not None and y is not None:
              t.up()
              t.goto(x , y)
              t.down()
        if fill_color == "yes":
               t.fillcolor(color)
               t.begin_fill()
        else :
              t.pencolor(color) 
        for _ in range (2):
              t.goto(t.xcor()+len , t.ycor())
              t.circle(cradius,90)
              t.goto(t.xcor() , t.ycor()+wed)
              t.circle(cradius,90)
              len = - len 
              wed = - wed
        t.end_fill()
        if Index==True:
              t.up()
              t.pencolor("black")
              t.goto(t.xcor()-12,t.ycor()+width)
              t.write(index, align='left',font=("normal" , Font//2, 'bold'))
              t.goto(t.xcor()+10,t.ycor()-width)
              
              
              
        if data is not None:
            t.up()
            t.goto(t.xcor()+length/2-cradius,t.ycor()+width*0.25)
            t.down()
            t.pencolor("black")
           
            t.write(data, align='center',font=("normal" , Font , 'bold'))
            if name is not None:
                currentPos=[]
                x1=t.xcor()
                y1 =t.ycor()
                currentPos.append(x1)
                currentPos.append(y1)
                name.append(currentPos)
        else:
               pass

    except :
          pass
    
          

# ----------Function for creating Array of size n ---------- #

def Array(t , arr, length= None , width=None , xcor=None , ycor=None , colora ="#C1AEFC" , IndexArray=False , nameA=None):
      
      # t - turtle object for creating Array 
      # arr - Original Array which is going to be Drawn 
      # length - Length of a Ractangle of an Array   
      # width - Width of a Ractangle of an Array
      #(Note : The above lenth and width would set to Orginal Length  and Width of Ractangle everywhere in the whole Program)
      # xcor  -  x coordinate of Array where from Array drawing Start (Note : This coordinate would decrease along with drawing rectangle in Array i.e ( horizontal ))
      # ycor - y coordinate of Array where from Array drawing Start i.e ( vertical position )
      dist=length+Gap
      if xcor is not None and ycor is not None :
          x=xcor
          
          if length is not None and width is not None :
             for i in range (len(arr)):
                   rect(t , x , ycor , length , width , 10 ,data=arr[i],color=colora, name=nameA ,Index= True if IndexArray==True else False ,index=i  )
                   x=x+dist


                                                                                                          # ----------Function for Mapping values to another ---------- #                                                                                              
def map(x):
    
    # x - x is the input that would be maped into another range of set 
    
    """ Mapping Ranges of different Scales"""
    
    input_min = 0
    input_max = 200
    output_min = 0
    output_max = 9.8
    scaling_factor = (output_max - output_min) / (input_max - input_min)
    
    return (x - input_min) * scaling_factor + output_min


# ----------Function for Swapping Animation  ---------- #

def swapBoxes( ti , tj , xi=0 , xj=0 , y=0 , idata=None , jdata=None , name=None):
      
      # ti - turtle object for creating Animation of i th element 
      # tj - turtle object for creating Animation of j th element 
      # xi - position of i th element in array i.e ( i th position )
      # xj - position of j th element in array i.e ( j th position )
      # y  -  y coordinate of swapBoxes function i.e (vertical )
      # datai - Original data of array on i th position i.e (array [ i ] )
      # dataj - Original data of array on j th position i.e (array [ j ] )
      
      ti.up()
      tj.up()
      txi.up()
      txj.up()
      #ti.speed(0)
      #tj.speed(0)
      if idata is None and jdata is None :
            datai=num[xi]
            dataj=num[xj]          
      else :
            datai=idata 
            dataj=jdata
      xipos = xi*Blen + xi*Gap
      xjpos = xj*Blen + xj*Gap

      dis=abs(xj-xi)*Blen +Gap*abs(xj-xi)+2
           
      #ti.goto( horizontal+40 + xipos , y+Bwid/2 )
      #tj.goto(horizontal+40 + xjpos, y+Bwid/2)
      ti.goto( name[xi][xi - xi]+2 , name[xi][xi - xi +1]+0.25*Bwid)
      tj.goto( name [xj][xj - xj]+2 , name [xj][xj - xj +1]+0.25*Bwid)
      
      
      ti.showturtle()
      tj.showturtle()
      #ti.pencolor("#C1AEFC")
      #tj.pencolor("#C1AEFC")
      ti.fillcolor("#C1AEFC")
      tj.fillcolor("#C1AEFC")
      ti.shape("square")
      ti.shapesize(map(Bwid),map(Blen))
      tj.shape("square")
      tj.shapesize(map(Bwid),map(Blen))
           
      # Going Upward.
      var=ti.ycor()
      
      for i in range (0,120,10):
            
            ti.goto(ti.xcor(),var+i)
                      
            if datai is not None:
               txi.goto(ti.xcor(),var+i-25)
               txi.clear()
               txi.pencolor('black')
               txi.write( datai , font=("normal" , 8 , 'bold') ,align='center')
         
            tj.goto(tj.xcor(),var+ i)
          
            if dataj is not None:
               txj.goto(tj.xcor(),var+i-25)
               txj.clear()
               txj.pencolor('black')
               txj.write( dataj , font=("normal" , 8 , 'bold') ,align='center')
          
                  
      pos=ti.xcor()
      pos1=tj.xcor()
      
      # Going left and right
 
      for j in range (0,dis,5):
            
            ti.goto( pos+j , ti.ycor())
            
            if datai is not None:
                txi.goto(pos+j,txi.ycor())
                txi.clear()
                txi.pencolor('black')
                txi.write( datai , font=("normal" , 8 , 'bold') ,align='center')
            
            tj.goto( pos1- j , tj.ycor())
            
            if dataj is not None:
                txj.goto(pos1 -j,txj.ycor())
                txj.clear()
                txj.pencolor('black')
                txj.write( dataj , font=("normal" , 8 , 'bold') ,align='center')
            
      pos=ti.ycor()
      pos1=tj.ycor()
      
      # Going downward
      
      for i in range (0,125,10):
         if i < 120:  
         
            ti.goto(ti.xcor(),pos-i)
            
            if datai is not None:
                txi.goto(txi.xcor(),pos - 30-i)
                txi.clear()
                txi.pencolor('black')
                txi.write( datai , font=("normal" , 8 , 'bold') ,align='center')
            
            tj.goto(tj.xcor(),pos1 - i) 
            if dataj is not None:
                txj.goto(txj.xcor(),pos1 - 30-i)
                txj.clear()
                txj.pencolor('black')
                txj.write( dataj , font=("normal" , 8 , 'bold') ,align='center')
         else :                     
                      txi.clear()
                      txj.clear()
                      ti.hideturtle()
                      tj.hideturtle()
                      rect(ti, name [xi][xi - xi] - Blen/2+cr+1 ,  name [xi][xi - xi +1] - Bwid*0.25 , Blen , Bwid ,10 ,data=dataj , stroke=1)
                      rect(tj, name[xj][xj - xj] - Blen/2+cr+1 , name[xj][xj - xj +1] - Bwid*0.25, Blen , Bwid , 10 , data=datai ,  stroke=1)
        

# ----------Function for Comparison of values ---------- #
                                                
def  Comparator( t , ipos , jpos , xcor=0, ycor=0 , col="red",datai=None , dataj=None, condition=True,type=None,insert=None , name=None):
      
      # t -  object of turtle from creating  Comparator arrows 
      # x - x coordinate of Comparator arrows
      # y - y coordinate of Comparator arrows
      # ipos - Position of i th element in every iteration
      # jpos - Postion of j th element which is to be comparing with i th element
      # col - color which user want to give Comparator arrows
      # gap - Gap between two adjacent two Rectangle 
     

      # Validate the input parameters
      #if not isinstance(t,Turtle):
          #raise TypeError("t must be an instance of turtle.Turtle")
      
      t.speed(0)
      t.hideturtle()
      dwed=Bwid
      dlen=Blen
      d=Blen*0.6
      s_len=d/3
      arrow_length=d
      bend_angle = 30
      side_angle = 60
      #if ipos == len(num)-1:
          #ipos=-1
          #dis=abs(jpos)
      #else :
      dis=abs(jpos-ipos)
      t.up()
      if xcor != 0 or ycor != 0 :
            t.goto(xcor , ycor)
      else :
            t.goto(name[ipos][ipos - ipos],name[ipos][ipos - ipos+1]-Bwid*0.35)
                
      t.right(90)          
      
      t.pencolor(col)
      t.fillcolor(col)
      t.begin_fill()
      
      # for Triangle shape

      t.right(bend_angle)
      t.forward(arrow_length)
      t.left(180-side_angle)
      
      t.forward(s_len)
      t.right(90)
      
      t.goto(t.xcor(),t.ycor()-30)
      #variable length of y for outer length
      
      x = ( dis*dlen) - s_len+dis*Gap
      y = ( dis*dlen ) + s_len+dis *Gap
      
      y1 = y - s_len/2 - (y/2)
      
      t.goto(t.xcor()+y1,t.ycor())
  
      t.goto(t.xcor(),t.ycor()-s_len)

      t.goto(t.xcor()+s_len,t.ycor())
      Crx=t.xcor()-s_len/2
      Cry=t.ycor()-s_len/2
      
      t.goto(t.xcor(),t.ycor()+s_len)
   
      t.goto(t.xcor()+y1,t.ycor())

      t.goto(t.xcor(),t.ycor()+30)
      
      t.left(90)
      t.forward(s_len)
      
      # For Triangle shape
      
      t.left(180-side_angle)      
      t.forward(arrow_length)
      t.left(180-side_angle)
      
      t.forward(arrow_length)
      t.left(180-side_angle)
      
      t.forward(s_len)
      t.right(90)
      
      t.goto(t.xcor(),t.ycor()-20)
      
      # Variable length of x for inner length
    
      t.goto(t.xcor()-x,t.ycor())
            
      t.goto(t.xcor(),t.ycor()+20)
      
      t.left(90)
      t.forward(s_len)
      
      t.left(180-side_angle)
      t.forward(arrow_length)
      t.end_fill()
       
      t.up()
      t.right(bend_angle)
      t.right(90)
     
      t.goto(Crx,Cry-20)
      
      if type =="selection":
            if insert == "swap":
                  t.goto(Crx,Cry-30)
                  t.write("Swap Min with i th Index",font=("verydana",4, "normal"), align='center')
            elif insert=="shell":
                  t.goto(Crx,Cry-30)
                  t.write("Swap temp with j th Index",font=("verydana",4, "normal"), align='center')
            elif insert=="shellc":
                  if(datai < dataj ):
                          t.write(str(datai)+" < "+str(dataj),font=("verydana",4, "normal"), align='center')
                          t.goto(Crx,Cry-45)
                          t.write("Swap",font=("verydana",4, "normal"), align='center')
                  else:
                          t.write(str(datai)+" > "+str(dataj),font=("verydana",4, "normal"), align='center')
                          t.goto(Crx,Cry-45)
                          t.write("Don't Swap",font=("verydana",4, "normal"), align='center')
                                 
            else :
                  t.goto(Crx,Cry-30)
                  t.write("j++ ,To Find Next Min",font=("verydana",4, "normal"), align='center')
                  
      elif type=="quick":
              
              if insert=="lb":
                     
                     if datai is None and dataj is None :
                            if(num[ipos]>=num[jpos]):
                                 t.write(str(num[ipos])+" >= "+str(num[jpos]),font=("verydana",4, "normal"), align='center')
                                 t.goto(Crx,Cry-45)
                                 t.write("start ++",font=("verydana",4, "normal"), align='center')           
                            else:            
                                 t.write(str(num[ipos])+" < "+str(num[jpos]), font=("verydana",4, "normal"), align='center')
                                 t.goto(Crx,Cry-45)
                                 t.write("shift start to current index",font=("verydana",4, "normal"), align='center')
                                 
              if insert=="ub":
                     
                     if datai is None and dataj is None :
                            if(num[ipos]< num[jpos]):
                                 t.write(str(num[ipos])+" < "+str(num[jpos]),font=("verydana",4, "normal"), align='center')
                                 t.goto(Crx,Cry-45)
                                 t.write("end --",font=("verydana",4, "normal"), align='center')           
                            else:            
                                 t.write(str(num[ipos])+" > "+str(num[jpos]), font=("verydana",4, "normal"), align='center')
                                 t.goto(Crx,Cry-45)
                                 t.write("shift end to current index",font=("verydana",4, "normal"), align='center')   
                                 
              if insert == "start_end":
                       t.write("swap start = "+str(num[jpos])+" with end = "+str(num[ipos]), font=("verydana",4, "normal"), align='center')
                       
              if insert == "pvt_end":
                       t.write("swap Pvoit = "+str(num[jpos])+" with end = "+str(num[ipos]), font=("verydana",4, "normal"), align='center')                                                                                    
      elif type == "binary" :
                
                if insert =="not_find" :
                     if datai is not None and dataj is not None :
                          if(datai != dataj ):
                             t.write(str(datai)+" ! = "+str(dataj),font=("verydana",4, "normal"), align='center')
                             t.goto(Crx,Cry-45)
                             t.write(" i ++ ",font=("verydana",4, "normal"), align='center')           
                     
                elif insert =="find" :
                     if datai is not None and dataj is not None :
                         if(datai == dataj ):
                             t.write(str(datai)+" == "+str(dataj),font=("verydana",4, "normal"), align='center')
                             t.goto(Crx,Cry-45)
                             t.write("data is found at "+str(ipos)+" index" ,font=("verydana",4, "normal"), align='center')           
                else :                     
                    if datai is not None and dataj is not None :
                         if(datai > dataj ):
                              t.write(str(datai)+" > "+str(dataj),font=("verydana",4, "normal"), align='center')
                              t.goto(Crx,Cry-45)
                              t.write("Shift High to Mid - 1",font=("verydana",4, "normal"), align='center')           
                         elif(datai < dataj ):            
                              t.write(str(datai)+" < "+str(dataj), font=("verydana",4, "normal"), align='center')
                              t.goto(Crx,Cry-45)
                              t.write("Shift Low to Mid + 1",font=("verydana",4, "normal"), align='center') 
                         else :            
                              t.write(str(datai)+" == "+str(dataj), font=("verydana",4, "normal"), align='center')
                              t.goto(Crx,Cry-45)
                              t.write("Data Is Found At "+str(ipos)+" Index " ,font=("verydana",4, "normal"), align='center') 
                                                             
                                                                                                                                                                                       
      else:            
           if datai is None and dataj is None :
                  if(num[ipos]>num[jpos]):
                       t.write(str(num[ipos])+" > "+str(num[jpos]),font=("verydana",4, "normal"), align='center')
                       t.goto(Crx,Cry-45)
                       t.write("Swap",font=("verydana",4, "normal"), align='center')           
                  else:            
                       t.write(str(num[ipos])+" < "+str(num[jpos]), font=("verydana",4, "normal"), align='center')
                       t.goto(Crx,Cry-45)
                       t.write("don't Swap",font=("verydana",4, "normal"), align='center') 
           else :
               if condition ==True:
                       if(datai < dataj ):
                          t.write(str(num[ipos])+" < "+str(num[jpos]),font=("verydana",4, "normal"), align='center')
                          t.goto(Crx,Cry-45)
                          t.write("Swap",font=("verydana",4, "normal"), align='center')           
                       else:            
                          t.write(str(num[ipos])+" > "+str(num[jpos]), font=("verydana",4, "normal"), align='center')
                          t.goto(Crx,Cry-45)
                          t.write("don't Swap",font=("verydana",4, "normal"), align='center')
               else:
                    t.goto(Crx,Cry-30)
                    t.write("Swap",font=("verydana",4, "normal"), align='center')
               
               
               
      time.sleep(1.5)
      
      t.clear()      
      t.down()
      





#------------ Function for Creating Arrow on i th position for everyy iteration -------------#
                  
def arrow( t , pos , xcor=None , ycor =None , col="green", text=None , name=None) :
           
     # t - turtle object for creating Arrow
     # pos - It is the position where arrow would be draw i.e i th or j th position of the array 
     # x -  x coordinate of arrow
     # y - y coordinate of arrow
     # col -  color which user want to give arrow 
     # text - Text Massage that user want to print top of arrow
     
      #if not isinstance(t, Turtle) :
           #raise TypeError("t must be Turtle object")
    
      #if not isinstance (pos,int)  :
            #raise ValueError ("ipos out of index")
      
      t.speed(0)
      
      ln=Blen*0.6
  
      _ln=ln/3
      _hig=math.sqrt(math.pow(ln,2)-math.pow(ln/2,2)) +_ln
      arrow_length= 34.9857
      deviation_angle = 120.9641
     
      
     
      t.up()
      if xcor  is not None or  ycor is not None :
            t.goto(xcor , ycor)
      else :
            t.goto( name[pos][pos-pos] , name[pos][pos - pos +1]+Bwid*0.81)
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
      t.goto(t.xcor(),t.ycor()+_hig)
      t.down()
      
      
      if text is not None :
            t.write(text,font=("verydana",7, "normal"),align='center')  
      
      if pos is not None :
            rect(t,x=name[pos][0]-Blen*0.38 , y=name[pos][1]- Bwid*0.25,length= Blen, width=Bwid , cradius= cr, stroke=3,fill_color="no" , color="#FF9A00")
      
#------------ End of Drawing Arrow in i th position---------------



#l_color="no" , color="#FF9A00")
      
#------------ End of Drawing Arrow in i th position---------------


      

