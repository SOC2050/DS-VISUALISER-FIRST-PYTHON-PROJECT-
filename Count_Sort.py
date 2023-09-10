
from turtle import *
import turtle
import time
import __main as d

r_input_Position = []
r_count_Position = []
r_up_count_Position = []
r_output_Position = []

screen=None


# --------- Function of Count Sort ------------- #

def count_Sort(screen ,arr):
    global r_input_Position 
    global r_count_Position 
    global r_up_count_Position
    global r_output_Position
    
    ne = len(arr)
    verPos = d.vertical
    horPos = d.horizontal
    r_input_Position.clear()
    r_count_Position.clear()
    r_up_count_Position.clear()
    r_output_Position.clear()
    
    
    
    d.createObject('r_title', screen, visibility=False, speed=0)
    d.createObject('r_input_array', screen, visibility=False, speed=0)
    d.createObject('r_count_array', screen, visibility=False, speed=0)
    d.createObject('r_count_update_array', screen, visibility=False, speed=0)
    d.createObject('r_output_array', screen, visibility=False, speed=0)
    d.createObject('r_input_i_arrow', screen, visibility=False, speed=0)
    d.createObject('r_count_key_arrow', screen, visibility=False, speed=0)
    d.createObject('r_count_update_arrow', screen, visibility=False, speed=3)
    d.createObject('r_output_i_arrow', screen, visibility=False, speed=0)
    d.createObject('r_count_key_update', screen, visibility=False, speed=0)
    d.createObject('r_count_update_key_update', screen, visibility=False, speed=0)
    d.createObject('r_output_key_update', screen, visibility=False, speed=0)

    # accessing Turtle object

    r_input_array = d.r_input_array
    r_count_array = d.r_count_array
    r_count_update_array = d.r_count_update_array
    r_output_array = d.r_output_array

    r_input_i_arrow = d.r_input_i_arrow
    r_count_key_arrow = d.r_count_key_arrow
    r_count_update_arrow = d.r_count_update_arrow
    r_output_i_arrow = d.r_output_i_arrow

    r_count_key_update = d.r_count_key_update
    r_count_update_key_update = d.    r_count_update_key_update
    r_output_key_update = d.r_output_key_update

    r_title = d.r_title
    d.setPosition(-150, -300)
    verPos = d.vertical
    horPos = d.horizontal
    # num name list of displaying elements
    r_title.up()
    r_title.goto(horPos + len(arr) / 2 * 100, verPos + 250)
    r_title.write("Count Sort", font=("Lobster", 12, 'bold'), align='center')
    key = max(arr) + 1
    Count = [0] * (key)
    Output = [0] * (ne)
     
    d.Array(r_input_array, arr, length=100, width=100, xcor=horPos, ycor=verPos, IndexArray=True, nameA=r_input_Position)
    r_title.goto(r_title.xcor(), r_title.ycor() - 350)
    r_title.write("Input Array", font=("Lobster", 10, 'bold'), align='center')
    
    for i in range(0, ne):  
        d.arrow(r_input_i_arrow, i,  col="#09CC12", text="ip", name=r_input_Position)
     
        d.setPosition(-100, 400) 
        verPos = d.vertical
        horPos = d.horizontal
        
        if i == 0:                          
            d.Array(r_count_array, Count, length=100, width=100, xcor=horPos, ycor=verPos, IndexArray=True, nameA=r_count_Position)
            r_title.goto(r_title.xcor(), r_title.ycor() - 400)
            r_title.write("Count Array", font=("Lobster", 10, 'bold'), align='center')
              
        d.Blen = 100
        d.arrow(r_count_key_arrow, arr[i], col="#09CC12", text="++ " + str(Count[arr[i]]), name=r_count_Position)
        Count[arr[i]] += 1
        
        #dist = horPos + (94 * arr[i])
        
        time.sleep(0.6)
        d.rect(r_count_key_update, x=r_count_Position[arr[i]][0]-d.Blen*0.38, y=r_count_Position[arr[i]][1]-d.Bwid*0.25 , length=100, width=100, cradius=10, data=Count[arr[i]], stroke=1, color="#C1AEFC" )
        
        #time.sleep(2)
        r_count_key_arrow.clear()
        r_input_i_arrow.clear()
        d.setPosition(100, -400) 
        d.Blen = 100
        verPos = d.vertical + 10
        horPos = d.horizontal
      
    d.setPosition(-100, 800) 
    verPos = d.vertical
    horPos = d.horizontal 
    for i in range(1, key):
        if i == 1:
            d.Array(r_count_update_array, Count, length=100, width=100, xcor=horPos, ycor=verPos, IndexArray=True, nameA=r_up_count_Position)
            r_title.goto(r_title.xcor(), r_title.ycor() - 400)
            r_title.write("Count Update Array", font=("Lobster", 10, 'bold'), align='center')
              
        d.arrow(r_count_update_arrow, i, col="#09CC12", text=str(Count[i - 1]) + " + " + str(Count[i]), name=r_up_count_Position)
        Count[i] += Count[i - 1]
          
        #dist = horPos + (94 * i)
        #time.sleep(0.7)
        d.rect(r_count_update_key_update, x=r_up_count_Position[i][0]-d.Blen*0.38 , y=r_up_count_Position[i][1]-d.Bwid*0.25 , length=100, width=100, cradius=10, data=Count[i], stroke=1, color="#C1AEFC")
                  
        r_count_update_arrow.clear()
                
    d.setPosition(100, 400) 
    verPos = d.vertical
    horPos = d.horizontal 
    d.Blen = 100
    i = ne - 1     
    
    while i >= 0:
        x = Count[arr[i]] - 1
        if i == ne - 1:    
            d.Array(r_output_array, Output, length=100, width=100, xcor=horPos, ycor=verPos, IndexArray=True, nameA=r_output_Position )
            r_title.goto(r_title.xcor(), r_title.ycor() - 400)
            r_title.write("Output Array", font=("Lobster", 10, 'bold'), align='center')          
        d.arrow(r_input_i_arrow, i , col="#09CC12", text="i", name=r_input_Position)
        
        d.arrow(r_output_i_arrow, x,  col="#09CC12", text="Place Input[i] at this index", name=r_output_Position)
        
        dist = horPos + (104 * x)
        Output[Count[arr[i]] - 1] = arr[i]
        
        Count[arr[i]] -= 1
        
        #time.sleep(0.7)
        d.rect(r_output_key_update, x=r_output_Position[x][0]-d.Blen*0.38 , y=r_output_Position[x][1]-d.Bwid*0.25 ,  length=100, width=100, cradius=10, data=arr[i], stroke=1, color="#C1AEFC" )
        
        r_output_i_arrow.clear()
        r_input_i_arrow.clear()
        i -= 1   
    
        
#-------------  Function to handle the window closing event -------------- #

def close_window_count_sort(screen):
    try:
        d.setPosition()
        r_input_Position.clear()
        r_count_Position.clear()
        r_up_count_Position.clear()
        r_output_Position.clear()
        count_Sort(screen , d.Input)
        d.setPosition()
        time.sleep(5)
        #d.screen.bye()  # Close the turtle window
    except turtle.Terminator:
        pass  # Catch the Terminator error and do nothing
    except Exception as e:
        pass 
        print("An error occurred:", str(e))  # Handle any other exception and print an

# Create the screen
#screen = turtle.Screen()

# Set up the close_window function to handle the window closing event
#screen.onkey(close_window_count_sort, "q")
#screen.listen()

#d.setPosition(150, 200)
close_window_count_sort(screen )




