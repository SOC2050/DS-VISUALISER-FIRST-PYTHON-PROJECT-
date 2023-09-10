from turtle import*
import turtle 
import time
import __main as d

screen=None
s_Position=[]
# ------------- Function  of Shell Sort --------------
 
def shell_Sort( screen , arr):
  
    verPos=d.vertical
    horPos=d.horizontal
    
    d.createObject('txi', screen , visibility=False ,speed=0)
    d.createObject('txj', screen, visibility=False , speed=0)

    d.createObject('s_title', screen , visibility=False ,speed=0)
    d.createObject('s_array', screen ,  visibility=False,speed=0)
    d.createObject('s_iarrow', screen , visibility=False,speed=0)
    d.createObject('s_jarrow', screen ,  visibility=False,speed=0)
    d.createObject('s_comparing', screen ,  visibility=False,speed=0)
    d.createObject('s_swap_j', screen ,  visibility=False,speed=0)
    d.createObject('s_swap_j1', screen ,  visibility=False,speed=0)
    d.createObject('s_swap_j1_dup', screen ,  visibility=False,speed=0)
    d.createObject('s_tempbox', screen , visibility=False,speed=0)
    d.createObject('s__tempbox', screen ,   visibility=False,speed=0)
    d.createObject('s_temparrow', screen,  visibility=False,speed=0)
    # Accessing object create by function
    s_title = d.s_title
    s_array = d.s_array 
    s_iarrow = d.s_iarrow
    s_jarrow = d.s_jarrow
    s_comparing = d.s_comparing
    s_swap_j = d.s_swap_j
    s_swap_j1 = d.s_swap_j1
    s_swap_j1_dup= d.s_swap_j1_dup
    s_tempbox = d.s_tempbox
    s__tempbox = d.s__tempbox
    s_temparrow = d.s_temparrow
        
    s_title.up()
    s_title.goto(horPos+len(arr)/2*100,verPos+250)
    s_title.write("Shell Sort ", font=("Lobster" , 12 , 'bold') ,align='center')
    n=len(arr)
    # Start with a big gap, then reduce the gap
    gap= n//2   
    dis = horPos-104
    
    while gap > 0:
        d.Array(s_array , arr , length=100 , width=100 , xcor=horPos , ycor=verPos, IndexArray=True , nameA=s_Position)
        
        for i in range(gap,n):
            j = i 
   
            #add a[i] to the elements that have been gap sorted               
            temp = arr[i]
            d.num.append(temp)
            N=len(d.num)
            
            d.rect(s_tempbox, x=s_array.xcor()+68.5 ,y=verPos ,  length=100 , width=100 , cradius=10, data=arr[N-1],stroke=1, color="green" ,name=s_Position )
            d.rect(s__tempbox , x=horPos+ i*104+5 ,y=verPos ,  length=100 , width=100 , cradius=10, data="Null" , stroke=1 ,color="green")

            d.arrow( s_iarrow , i  , col="red",text="I" , name=s_Position)
            d.arrow( s_jarrow , j - gap  , col="red",text="j" , name=s_Position)
            d.arrow( s_temparrow , N-1 , col="green",text="temp" , name=s_Position)
            
            #d.Comparator( comparing ,  horPos , verPos ,  j - gap ,i)
            d.Comparator( s_comparing  , j - gap , N-1, datai=arr [i] , dataj = arr[j-gap], type="selection",insert="shellc" , name=s_Position)
            
           
            
            # shift earlier gap-sorted elements up until the correct
            # location for a[i] is found
             
            while  j >= gap and arr[j-gap] >temp:
                     if j==gap and arr[j - gap ] :                           
                           d.Comparator( s_comparing , j - gap ,gap,name=s_Position)
                           
                     arr[j] = arr[j-gap]
                     d.swapBoxes( s_swap_j , s_swap_j1  , j- gap  ,  j ,  verPos , idata =arr[j- gap], jdata="Null" , name=s_Position)

                     j -= gap
                     
            #put temp (the original a[i]) in its correct location      
            s_iarrow.clear()
            s_jarrow.clear()
            arr[j] = temp

            d.arrow( s_jarrow , j  , col="red",text="j" , name=s_Position)
            d.Comparator( s_comparing , j , N-1 ,col="green",type="selection",insert="shell" , name=s_Position)
            
            d.swapBoxes( s_swap_j1 , s_swap_j1_dup  , j  , N- 1 , idata="Null" , jdata = temp , name=s_Position)
            arr.pop()
            s_jarrow.clear()
         
        # decreasing gap   by 2                
        gap //= 2
        
        verPos=verPos - 250
        s_temparrow.clear()
        s_tempbox.clear()
        s_swap_j1_dup.clear()
        s_Position.clear()
        

#--------------  Function to handle the window closing event -------------- #

def close_window_shell_sort(screen  ):
    try:
        d.setPosition( )       
        shell_Sort( screen , d.num)
        time.sleep(5)
        d.setPosition( )
        #d.screen.bye()  # Close the turtle window
    except turtle.Terminator:
        pass  # Catch the Terminator error and do nothing
    except Exception as e:
        pass 
        print("An error occurred:", str(e))  # Handle any other exception and print an error message


##### ----------------- Main Driver Program ------------------- #####

# Set the close_window function to handle the window closing event

#d.screen.onkey(close_window_shell_sort, "q")
#d.screen.listen()

d.setPosition( -200 , -350)
close_window_shell_sort( screen )
