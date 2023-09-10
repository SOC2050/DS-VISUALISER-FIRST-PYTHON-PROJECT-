import turtle
from turtle import*
import __main as d
import two_Darray as dd
import time
import random 

screen=None

def box_index(i , j ):
    return i*dd.r_cols+j


def twoDtraversal(screen ):
    r=random.randint(2,5)
    c=random.randint(2,5)
    dd.twoDarray(screen , r , c  , plist=dd.poslist)
    d.createObject('traval', screen ,  visibility=False, speed=6, color="black")
    d.createObject('mdata', screen ,  x = d.horizontal- 50 , y = d.vertical- 900 , visibility=True, speed=6, color="black")
    
    
    travel = d.traval
    mdata = d.mdata
    mdata.up()
    mdata.write(f"Traversal In  { r } x { c }  Matrix : " , font=("Lobster" , 7 , 'bold'))
    mdata.goto(mdata.xcor() , mdata.ycor() - 50)
    xcor=mdata.xcor()
    ycor=mdata.ycor()
    
    dimension = dd.r_rows*dd.r_cols
    
    for i  in range (dd.r_rows+1):
        for j in range (dd.r_cols):
             ind=box_index(i, j)
             if ind < dimension:
                  d.rect( travel ,x=dd.poslist[ind][0]-d.Blen*0.38 , y=dd.poslist[ind][1]- d.Bwid*0.25,length= d.Blen , width=d.Bwid, cradius= 10 , stroke=3,fill_color="no" , color="#FF9A00")
                  mdata.goto(mdata.xcor() , mdata.ycor() - 50)
                  mdata.write(f"Element At ({ i } , { j })  =  { dd.matrix[i][j] }",  font=("Lobster" , 6 , 'normal'))
                  if i== dd.r_rows//2 and j==0  :
                      mdata.goto(xcor+ 410 , ycor )
                      
             
             time.sleep(0.7)
             travel.clear()
    
    



def two_D_traversal(screen):
    try:
        d.setPosition( )
        dd.poslist.clear()
        twoDtraversal( screen )
        d.setPosition()
        dd.poslist.clear()
        time.sleep(5)
        #d.screen.bye()  # Close the turtle window
    except turtle.Terminator:
        pass  # Catch the Terminator error and do nothing
    except Exception as e:
        pass 
        print("An error occurred:", str(e))  # Handle any other exception and print an error message              

two_D_traversal(screen )

