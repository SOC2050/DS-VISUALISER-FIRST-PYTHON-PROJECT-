
import turtle
from turtle import*
import __main as d
import random

r_rows= 0
r_cols = 0
poslist=[]
matrix=[]
row=None
screen=None
def twoDarray( screen, mrows=None  , mcols=None  , umatrix=None , plist=None , fill=True  ):
    global r_rows
    global r_cols
    global row
   
    global matrix 
    
    
    d.setPosition( -100 , -450)
    
    verPos=d.vertical
    horPos=d.horizontal

    d.createObject('box', screen ,  visibility=False, speed=6, color="black")
    d.createObject('row', screen ,visibility=False, speed=6, color="black")
    d.createObject('col', screen ,visibility=False, speed=6, color="black")
    
    
    box = d.box
    row =d.row
    col = d.col
    # Create a 4 by 5 list with random values
    if mrows is not None and mcols is not None :
         r_rows= mrows 
         r_cols = mcols 
    else:
         r_rows= random.randint(2,7)
         r_cols = random.randint(2,6)
    my_list = [[random.randint(1, 10) for _ in range(mcols if mcols is not None  else r_cols ) ] for _ in range(mrows if mrows is not None  else r_rows)]
    
    if umatrix is not None :
        matrix=umatrix 
    else:
        matrix=my_list
    # Accessing elements using loops
    rows = len(matrix)  # Number of rows in the matrix
    cols = len(matrix[0])  # Number of columns in the matrix

    for i in range(rows):  # Iterate over rows
          verPos = verPos - 130
          
          for j in range(cols):  # Iterate over columns
                element = matrix[i][j]
                d.rect(box , x=horPos + j*120 , y=verPos , length=100 , width=100 , cradius=10 , data=element if fill==True else "  ", stroke=1 , fill_color="yes" , color="#C1AEFC",Index=True , index=f"({i} , {j})" , name=plist,  Font=6)
   
    
    dia=rows*cols
    num=0
    
    row.up()
    for i in range (0, dia , cols ):
           row.goto(plist[i][0] - d.Blen*1.2, plist[i][1])
           row.write(f"R{num}" , font=("Lobster" , 7 , 'bold') )
           num +=1
           
    col.up()        
    for i in range (cols):
           col.goto(plist[i][0] , plist[i][1] + d.Bwid*1.2)
           col.write(f"C{i}" , align='center' , font=("Lobster" , 7 , 'bold') )
    col.goto(plist[cols*rows-1][0]+d.Blen*0.7 , plist[cols*rows-1][1] - d.Bwid*0.4) 
    col.write(f"{rows} x {cols}" , font=("Lobster" , 6 , 'bold'))
                                                              

def two_D_array(screen ):
    try:
        d.setPosition( )
        poslist.clear()
        twoDarray( screen  , plist=poslist)
        d.setPosition()
        poslist.clear()
        time.sleep(5)
        #d.screen.bye()  # Close the turtle window
    except turtle.Terminator:
        pass  # Catch the Terminator error and do nothing
    except Exception as e:
        pass 
        print("An error occurred:", str(e))  # Handle any other exception and print an error message              

two_D_array(screen )

