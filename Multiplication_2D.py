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

def box_pos(i , j ,  matrix ):
    rows1 = len(matrix)
    cols1 = len(matrix[0])
    return i*cols1+j


def structure(screen, t):
    t.up()
    global m1list ,  m2list ,  m3list ,  matrix1 , matrix2 , matrix3 , labelx , labely ,lx ,ly

    r1=random.randint(2,3)
    c1=random.randint(1,3)
    #r2=random.randint(2,3)
    c2=random.randint(1,3)
    
    matrix1 = [[random.randint(1, 10) for _ in range(c1)] for _ in range(r1)]
    matrix2 = [[random.randint(1, 10) for _ in range(c2)] for _ in range(c1)]
    matrix3 = [[random.randint(1, 10) for _ in range(c2)] for _ in range(r1)]

    d.setPosition( 100 , -150)
    dd.twoDarray(screen, mrows=r1 , mcols=c1  , umatrix=matrix1 , plist=m1list)
   
    t.goto( dd.row.xcor()+dd.r_cols/2*150, dd.row.ycor()-160)
    t.write("X" , font=("Lobster" , 12 , 'bold') , align='center')
    labelx=t.xcor()
    labely=t.ycor()
    d.setPosition( 100 , r1*200+500)
    dd.twoDarray(screen, mrows=c1 , mcols=c2  ,umatrix=matrix2 , plist=m2list)
    
    t.goto( dd.row.xcor()+dd.r_cols/2*150, dd.row.ycor()-210)
    t.write("=" , font=("Lobster" , 20 , 'bold') , align='center')
    lx=t.xcor()
    ly=t.ycor()
    
    d.setPosition( 100 , c1*200+600)
    dd.twoDarray(screen, mrows=r1 , mcols=c2  ,  plist=m3list , fill=False)
    
def multiplication(screen):
    
    global matrix3 , matrix2 , matrix1

    d.createObject('label', screen ,  visibility=False, speed=6, color="black")
    label =d.label
    structure ( screen , label)
    d.createObject('traval1', screen ,  visibility=False, speed=6, color="black")
    d.createObject('traval2', screen ,  visibility=False, speed=6, color="black")
    d.createObject('traval3', screen ,  visibility=False, speed=6, color="black")
    
    traval1= d.traval1
    traval2 = d.traval2
    traval3 = d.traval3
    
    
    
    rows1 = len(matrix1)
    cols1 = len(matrix1[0])
    rows2 = len(matrix2)
    cols2 = len(matrix2[0])
    
    if cols1 != rows2:
        print("Cannot multiply the matrices. Invalid dimensions.")
        exit()
        
    #dimension = dd.r_rows*dd.r_cols
    
    for i in range(rows1):
         
         for j in range(cols2):
              ele=0
              for k in range(cols1):
                   
                   ind=box_pos(i , k , matrix1)
                   if ind < rows1*cols1:
                        d.rect( traval1 ,x=m1list[ind][0]-d.Blen*0.38 , y=m1list[ind][1]- d.Bwid*0.25,length= d.Blen , width=d.Bwid, cradius= 10 , stroke=3,fill_color="no" , color="#FF9A00" )
                        
                   label.pencolor('#FF9A00')
                   label.goto( labelx, labely)
                   label.write(" X " , font=("Lobster" , 12 , 'bold') , align='center')
                      
                   time.sleep(0.6)
                   ind=box_pos(k, j , matrix2)
                   if ind < rows2*cols2 :
                         d.rect( traval2 ,x=m2list[ind][0]-d.Blen*0.38 , y=m2list[ind][1]- d.Bwid*0.25,length= d.Blen , width=d.Bwid, cradius= 10 , stroke=3,fill_color="no" , color="#FF9A00")
                   
                   ele += matrix1[i][k] * matrix2[k][j]
                   time.sleep(0.6)
                   traval1.clear()
                   traval2.clear()  
                   label.pencolor('black')
                   label.goto( labelx, labely)
                   label.write(" X " , font=("Lobster" , 12 , 'bold') , align='center')
                  
                   
              label.pencolor('#FF9A00')
              label.goto( lx, ly)
              label.write(" = " , font=("Lobster" , 20 , 'bold') , align='center')            
              ind=box_pos(i , j  , matrix3)
              if ind < rows1*cols2:
                    d.rect( traval3 ,x=m3list[ind][0]-d.Blen*0.38 , y=m3list[ind][1]- d.Bwid*0.25,length= d.Blen , width=d.Bwid, cradius= 10 , data=ele , stroke=3,fill_color="yes" , color="#FF9A00")
                    label.pencolor('black')
                    label.goto( lx, ly)
                    label.write(" = " , font=("Lobster" , 20 , 'bold') , align='center')
                                    
    
    



def Multiplication(screen):
    try:
        d.setPosition( )
      
        multiplication( screen )
        d.setPosition()
    
        time.sleep(5)
        #d.screen.bye()  # Close the turtle window
    except turtle.Terminator:
        pass  # Catch the Terminator error and do nothing
    except Exception as e:
        pass 
        print("An error occurred:", str(e))  # Handle any other exception and print an error message              

Multiplication(screen )  
