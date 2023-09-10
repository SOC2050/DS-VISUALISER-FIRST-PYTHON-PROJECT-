from turtle import*
import turtle 
import time
import __main as d


screen=None
b_Position=[]

#-------------------Bubble sort function-------------------

def bubble_Sort( screen, arr ):
    d.createObject('txi', screen , visibility=False ,speed=0)
    d.createObject('txj', screen, visibility=False , speed=0) 
    d.createObject('b_title', screen , visibility=False ,speed=0)
    d.createObject('b_array', screen, visibility=False , speed=0)
    d.createObject('b_jarrow', screen , visibility=False ,speed=0)
    d.createObject('b_j1arrow', screen,  visibility=False ,speed=0)
    d.createObject('b_comparing', screen ,  visibility=False ,speed=3)
    d.createObject('b_swap_j', screen , visibility=False,speed=0)
    d.createObject('b_swap_j1', screen ,  visibility = False, speed=0)      
    b_title = d.b_title
    b_array = d.b_array # Accessing object create by function
    b_jarrow = d.b_jarrow
    b_j1arrow = d.b_j1arrow
    b_comparing = d.b_comparing
    b_swap_j = d.b_swap_j
    b_swap_j1 = d.b_swap_j1  
      
  
    d.setPosition( -100 , -300)
    
    verPos=d.vertical
    horPos=d.horizontal
    b_title.up()
    b_title.goto(horPos+len(arr)/2*100,verPos+250)
    b_title.write("Bubble Sort ", font=("Lobster" , 12 , 'bold') ,align='center')
    """Function for Drawing Arrays According to Bubble sort"""
    
    if not isinstance (arr,list):
          raise TypeError ("arr must be list")
          
    # Outer loop for traveryse the entire list
    
    for i in range(0,len( arr )-1 ):
        
        #Innir loop fro traveryse the entire list
        b_Position.clear()
        d.Array(b_array , arr , length=100 , width=100 , xcor=horPos , ycor=verPos,IndexArray=True , nameA=b_Position)
           
        for j in range( len( arr )-1-i ):
            b_jarrow.clear()
            b_j1arrow.clear()
            d.arrow( b_jarrow , j  , col="#09CC12",text="j" ,name=b_Position)
            d.arrow( b_j1arrow, j+1 ,  col="#3ED32E",text="j+1" , name=b_Position)

                  
            if arr[j] > arr[j+1] :
                  
                  d.Comparator( b_comparing   , j , j+1,col="#F54444" ,name=b_Position)
                                             
            else :
                   d.Comparator( b_comparing   , j , j+1 ,name=b_Position)          
                      
            if( arr[j] > arr[j+1] ):                
                #d.Comparator( comparing ,  horPos , verPos , j , j+1 , col="green")
           
                d.swapBoxes( b_swap_j , b_swap_j1  , j ,  j +1 ,name=b_Position)
                
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                
        verPos=verPos - 250
        

#---------------Bubble sort end--------------- 


#--------------  Function to handle the window closing event -------------- #

def close_window_bubble_sort(screen):
    try:
        d.setPosition( )
        b_Position.clear()
        bubble_Sort(screen , d.num)
        d.setPosition()
        time.sleep(5)
        #d.screen.bye()  # Close the turtle window
    except turtle.Terminator:
        pass  # Catch the Terminator error and do nothing
    except Exception as e:
        pass 
        print("An error occurred:", str(e))  # Handle any other exception and print an error message


##### ----------------- Main Driver Program ------------------- #####

# Set the close_window function to handle the window closing event




#d.setPosition( -300 , -700)
close_window_bubble_sort( screen)
#stop(screen)




