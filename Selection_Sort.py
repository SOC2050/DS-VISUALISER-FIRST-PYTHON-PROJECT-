from turtle import*
import turtle 
import time
import __main as d

se_Position=[]
screen=None
#---------------Function of Selection sort ---------------- #

def Selection_Sort(screen, arr):
    
    d.createObject('txi', screen , visibility=False ,speed=0)
    d.createObject('txj', screen, visibility=False , speed=0)
    d.createObject('se_title', screen, visibility=False ,speed=0)
    d.createObject('se_array', screen ,  visibility=False,speed=0)
    d.createObject('se_iarrow', screen , visibility=False,speed=0)
    d.createObject('se_jarrow', screen ,  visibility=False,speed=0)
    d.createObject('se_comparing', screen ,  visibility=False,speed=0)
    d.createObject('se_swap_i', screen ,  visibility=False,speed=0)
    d.createObject('se_swap_j', screen , visibility=False,speed=0)
    d.createObject('se_min_element', screen,  visibility=False,speed=0)
    # Accessing object create by function
    se_title = d.se_title
    se_array = d.se_array 
    se_iarrow = d.se_iarrow
    se_jarrow = d.se_jarrow
    se_comparing = d.se_comparing
    se_swap_i = d.se_swap_i
    se_swap_j = d.se_swap_j
    se_min_element = d.se_min_element
      
    n = len(arr)
    j=0
    verPos=d.vertical
    horPos=d.horizontal
    
    se_title.up()
    se_title.goto(horPos+len(arr)/2*100,verPos+250)
    se_title.write("Selection Sort ", font=("Lobster" , 12 , 'bold') ,align='center')
   
    # -> Traverse through all array elements
    for i in range(n-1):
        
        min=i
        d.Array(se_array , arr , length=100 , width=100 , xcor=horPos , ycor=verPos, IndexArray=True , nameA=se_Position )
        d.arrow( se_iarrow , i ,  col="green",text="i" , name=se_Position)
        # -> Find the minimum element in remaining unsorted array       
        for j in range(i+1, n):
                     
            d.arrow( se_jarrow , j  , col="red",text="j" , name=se_Position)
            
            d.Comparator( se_comparing , min, j, col="red",type="selection",insert=" " , name = se_Position)
                      
            if arr[min] > arr[j]:
                   se_min_element.clear()
                   d.arrow( se_min_element , j , col="red",text="Min" , name= se_Position)
                   min=j                                
            se_jarrow.clear()
            
        se_min_element.clear()
        d.Comparator( se_comparing ,  i , min, col="green",type="selection",insert="swap" , name= se_Position )
        d.swapBoxes( se_swap_i, se_swap_j  , i ,  min , name= se_Position )
        arr[i], arr[min] = arr[min], arr[i]
        se_iarrow.clear()
        verPos=verPos - 250
        se_Position.clear()

#--------------  Function to handle the window closing event -------------- #

def close_window_selection_sort( screen):
    try:    
        d.setPosition( )
        se_Position.clear()  
        Selection_Sort(screen , d.num)
        time.sleep(5)
        d.setPosition( )
        # Close the turtle window
    except turtle.Terminator:
        pass  # Catch the Terminator error and do nothing
    except Exception as e:
        pass 
        print("An error occurred:", str(e))  # Handle any other exception and print an error message


##### ----------------- Main Driver Program ------------------- #####

# Set the close_window function to handle the window closing event

#d.screen.onkey(close_window_Selection_sort, "q")
#d.screen.listen()

d.setPosition( 100 , 100)
close_window_selection_sort( screen )
