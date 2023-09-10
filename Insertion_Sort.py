from turtle import*
import turtle 
import time
import __main as d

screen=None
i_Position=[]
#----------------- Function for Insertion Sort ------------------ #

def insertion_Sort(screen , arr):
    
    d.createObject('txi', screen , visibility=False ,speed=0)
    d.createObject('txj', screen, visibility=False , speed=0)
    d.createObject('i_title', screen ,  visibility=False ,speed=0)
    d.createObject('i_array1', screen ,  visibility=False,speed=0)
    d.createObject('i_keyarrow', screen , visibility=False,speed=0)
    d.createObject('i_keyshiftarrow', screen, visibility=False,speed=0)
    d.createObject('i_keybox', screen ,  visibility=False,speed=0)
    d.createObject('i__keybox', screen ,  visibility=True,speed=1)
    d.createObject('i_iarrow', screen ,  visibility=False,speed=0)
    d.createObject('i_jarrow', screen , visibility=False,speed=0)
    d.createObject('i_comparing', screen , visibility=False,speed=0)
    d.createObject('i_swap_j', screen ,  visibility=False,speed=0)
    d.createObject('i_swap_j1', screen , visibility=False,speed=0)
    d.createObject('i_swap_j1_dup', screen ,  visibility=False,speed=0)
    # Accessing object create by function
    i_title = d.i_title
    i_array1= d.i_array1
    i_keyshiftarrow = d.i_keyshiftarrow
    i_keyarrow = d.i_keyarrow
    i_keybox = d.i_keybox
    i__keybox = d.i__keybox
    i_iarrow = d.i_iarrow
    i_jarrow = d.i_jarrow
    i_comparing = d.i_comparing
    i_swap_j = d.i_swap_j
    i_swap_j1 = d.i_swap_j1
    i_swap_j1_dup = d.i_swap_j1_dup
    
            
    verPos=d.vertical
    horPos=d.horizontal
    
    i_title.up()
    i_title.goto(horPos+len(arr)/2*100,verPos+250)
    i_title.write("Insertion Sort ", font=("Lobster" , 12 , 'bold') ,align='center')
    n=len(arr)
    dis = horPos-104
    #jj=0
    if not isinstance (arr,list):
          raise TypeError ("arr must be List type")
    global very
    k=0
    for i in range(1, n):
        key = arr[i]
       
        d.Array(i_array1 , arr , length=100 , width=100 , xcor=horPos , ycor=verPos, IndexArray=True , nameA=i_Position)
        
        d.num.append(key)
        N=len(d.num)
        
        d.rect(i_keybox, x=i_array1.xcor()+68,y=verPos ,  length=100 , width=100 , cradius=10, data=arr[N-1],stroke=1, color="green" , name=i_Position)
        
        #d.rect(i__keybox , x=d.Position[i][0] ,y=verPos ,  length=100 , width=100 , cradius=10, data="Null" , stroke=1 ,color="green")
        d.rect(i__keybox , x=i_Position[i][0]-d.Blen*0.39 , y = verPos ,   length=100 , width=100 , cradius=10, data="Null" , stroke=1 ,color="green" )
        
        d.arrow(i_keyarrow , N-1 ,col="green",text="key" , name=i_Position)  
        d.arrow( i_iarrow , i , col="green",text="i" , name=i_Position )
        
        for j in range(i-1, -2, -1):
              k=j
              if j>=0:                
                d.arrow( i_jarrow , j  ,col="red",text="j" , name=i_Position)             
                  
              if j >=0 and arr[j] > key:
                               
                    d.Comparator( i_comparing , j ,  N-1,col="green" , name=i_Position)
                    d.Comparator( i_comparing  ,j , j+1 ,col="green",  datai=arr[j+1] , dataj=arr[j] , condition=False , name=i_Position)
                    
                    d.swapBoxes( i_swap_j , i_swap_j1  , j ,  j +1  ,idata=arr[j], jdata= "Null"  , name=i_Position)
                    arr[j + 1] = arr[j]
                  
                    i_jarrow.clear()                  
              else:                   
                    break

        d.arrow( i_keyshiftarrow , j+1   ,col="green",text="Shift  key" , name=i_Position)
        d.swapBoxes( i_swap_j1 , i_swap_j1_dup ,j+1 , N-1 , idata="Null" , jdata = key , name=i_Position )
        
        #finally shifting key to arr[ j+ 1] position which is correct position of that element in the array
        arr[j + 1] = key
       
        i_jarrow.clear()
        i_iarrow.clear()
        i_keyarrow.clear()
        i_keyshiftarrow.clear()
             
        verPos=verPos - 250
        arr.pop()
        i_keybox.clear()
        i_swap_j1_dup.clear()
        i_Position.clear()
        
#-----------------Insertion sort is end----------------- #

#--------  Function to handle the window closing event ------- #
def close_window_insertion_sort( screen):
    try:        
        d.setPosition( )
        i_Position.clear()
        insertion_Sort(screen , d.num)
        time.sleep(5)
        d.setPosition( )
        #d.screen.bye()  # Close the turtle window
    except turtle.Terminator:
       
        pass  # Catch the Terminator error and do nothing
        #d.destroyObjects()
    except Exception as e:
        pass 
        print("An error occurred:", str(e))  # Handle any other exception and print an error message


##### ----------------- Main Driver Program ------------------- #####

# Set the close_window function to handle the window closing event

#d.screen.onkey(close_window_insertion_sort, "q")
#d.screen.listen()

#d.setPosition( -100 , 200)
close_window_insertion_sort(screen)


