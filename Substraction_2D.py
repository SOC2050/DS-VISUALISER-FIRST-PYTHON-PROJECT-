import turtle
from turtle import*
import __main as d 
import two_Darray as dd
import two_Dtraversal as tt
import random 
import time


m1list=[]
m2list=[]
m3list=[]
matrix1=[]
matrix2=[]
matrix3=[]
screen= None


labelx=0
labely=0
lx=0
lu=0
def box_pos(i , j ):
    return i*dd.r_cols+j


def structure( screen , t):
    t.up()
    global m1list ,  m2list ,  m3list ,  matrix1 , matrix2 ,matrix3  , labelx , labely ,lx ,ly

    r=random.randint(2,3)
    c=random.randint(2,5)
    
    matrix1 = [[random.randint(1, 10) for _ in range(c)] for _ in range(r)]
    matrix2 = [[random.randint(1, 10) for _ in range(c)] for _ in range(r)]
    matrix3= [[0 for _ in range(c)] for _ in range(r)]

    d.setPosition( 100 , -150)
    dd.twoDarray(screen, mrows=r , mcols=c  , umatrix=matrix1 , plist=m1list)
   
    t.goto( dd.row.xcor()+dd.r_cols/2*150, dd.row.ycor()-160)
    t.write(" - " , font=("Lobster" , 20 , 'bold') , align='center')
    labelx=t.xcor()
    labely=t.ycor()
    d.setPosition( 100 , r*200+500)
    dd.twoDarray(screen, mrows=r , mcols=c  ,umatrix=matrix2 , plist=m2list)
    
    t.goto( dd.row.xcor()+dd.r_cols/2*150, dd.row.ycor()-220)
    t.write("=" , font=("Lobster" , 20 , 'bold') , align='center')
    lx=t.xcor()
    ly=t.ycor()
    
    d.setPosition( 100 , r*200+600)
    dd.twoDarray(screen, mrows=r , mcols=c  , umatrix=matrix3 ,  plist=m3list )
    
def substraction(screen):
    global matrix3 , matrix2 , matrix1

    d.createObject('label', screen ,  visibility=False, speed=6, color="black")
    label =d.label
    structure (screen ,  label)
    d.createObject('traval1', screen ,  visibility=False, speed=6, color="black")
    d.createObject('traval2', screen ,  visibility=False, speed=6, color="black")
    d.createObject('traval3', screen ,  visibility=False, speed=6, color="black")
    
    traval1= d.traval1
    traval2 = d.traval2
    traval3 = d.traval3
        
    dimension = dd.r_rows*dd.r_cols
    
    for i  in range (dd.r_rows):
        row=[]
        for j in range (dd.r_cols):
             ind=box_pos(i , j )
             if ind < dimension:
                  d.rect( traval1 ,x=m1list[ind][0]-d.Blen*0.38 , y=m1list[ind][1]- d.Bwid*0.25,length= d.Blen , width=d.Bwid, cradius= 10 , stroke=3,fill_color="no" , color="#FF9A00")
                  
                  label.pencolor('#FF9A00')
                  label.goto( labelx, labely)
                  label.write(" - " , font=("Lobster" , 20 , 'bold') , align='center')
                  
                  d.rect( traval2 ,x=m2list[ind][0]-d.Blen*0.38 , y=m2list[ind][1]- d.Bwid*0.25,length= d.Blen , width=d.Bwid, cradius= 10 , stroke=3,fill_color="no" , color="#FF9A00")
                  
                  
                  label.goto( lx, ly)
                  label.write(" = " , font=("Lobster" , 20 , 'bold') , align='center')
                                    
                  
                  
                  d.rect( traval3 ,x=m3list[ind][0]-d.Blen*0.38 , y=m3list[ind][1]- d.Bwid*0.25,length= d.Blen , width=d.Bwid, cradius= 10 , stroke=3,fill_color="no" , color="#FF9A00")
                  
                  element = matrix1[i][j] -  matrix2[i][j]
                  
                  d.rect( traval3 ,x=m3list[ind][0]-d.Blen*0.38 , y=m3list[ind][1]- d.Bwid*0.25,length= d.Blen , width=d.Bwid, cradius= 10 , data=element , stroke=3,fill_color="yes" , color="#FF9A00")
                  traval1.clear()
                  traval2.clear()
                  
                  label.pencolor('black')
                  label.goto( labelx, labely)
                  label.write(" - " , font=("Lobster" , 20 , 'bold') , align='center')
                                    
                  
                  label.goto( lx, ly)
                  label.write(" = " , font=("Lobster" , 20 , 'bold') , align='center')
                                    
                  
                  row.append(element)
                  time.sleep(0.7)
                  
        matrix3.append(row)
                  

    


def Substraction(screen):
    try:
        d.setPosition( )
      
        substraction( screen )
        d.setPosition()
    
        time.sleep(5)
        #d.screen.bye()  # Close the turtle window
    except turtle.Terminator:
        pass  # Catch the Terminator error and do nothing
    except Exception as e:
        pass 
        print("An error occurred:", str(e))  # Handle any other exception and print an error message              

Substraction(screen )  

