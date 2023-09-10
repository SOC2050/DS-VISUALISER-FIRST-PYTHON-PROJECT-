from turtle import*
import turtle 
import time
import __main as d


screen=None
c_input_Position=[]
c_count_Position=[]
c_up_count_Position=[]
c_output_Position=[]

cnt=0
# --------- Function of Count Sort ------------- #

def count_Sort(arr,exp1 , screen):
    global cnt
    global c_input_Position
    global c_count_Position
    global c_up_count_Position
    global c_output_Position   
    d.createObject('c_title', screen , visibility=False ,speed=0)
    d.createObject('c_input_array', screen , visibility=False,speed=0)
    d.createObject('c_count_array', screen ,  visibility=False,speed=0)
    d.createObject('c_count_update_array', screen ,  visibility=False,speed=0)
    d.createObject('c_output_array', screen , visibility=False,speed=0)
    d.createObject('c_input_i_arrow', screen ,  visibility=False,speed=0)
    d.createObject('c_count_key_arrow', screen ,  visibility=False,speed=0)
    d.createObject('c_count_update_arrow', screen, visibility=False,speed=3)
    d.createObject('c_output_i_arrow', screen ,  visibility=False,speed=0)
    d.createObject('c_count_key_update', screen,  visibility=False,speed=0)
    d.createObject('c_count_update_key_update', screen,  visibility=False,speed=0)
    d.createObject('c_output_key_update', screen ,visibility=False,speed=0)
    # accessing Turtle object
    c_input_array = d.c_input_array
    c_count_array = d.c_count_array
    c_count_update_array = d.c_count_update_array
    c_output_array = d.c_output_array

    c_input_i_arrow = d.c_input_i_arrow
    c_count_key_arrow = d.c_count_key_arrow
    c_count_update_arrow = d.c_count_update_arrow
    c_output_i_arrow = d.c_output_i_arrow

    c_count_key_update = d.c_count_key_update
    c_count_update_key_update = d.       c_count_update_key_update
    c_output_key_update = d.c_output_key_update

    c_title = d.c_title
    
    
    ne= len(arr)
    verPos=d.vertical
    horPos=d.horizontal
    # num name list of displaying elements
    if cnt<=0:
         c_title.up()
         c_title.goto(horPos+len(arr)/2*100,verPos+250)
         c_title.write("Radix  Sort ", font=("Lobster" , 12 , 'bold') ,align='center')
         
    c_titlex=c_title.xcor()
    c_titley=c_title.ycor()   
    cnt+=2
    Count=[0] * (10)
    Output=[0]*(ne)
    OPA=[0]*(ne)
     
    d.Array(c_input_array , arr , length=100 , width=100 , xcor=horPos , ycor=verPos,IndexArray=True , nameA=c_input_Position)
    c_title.up()
    c_title.goto(c_title.xcor(),c_title.ycor()-350)
    
    c_title.write("Input Array ", font=("Lobster" , 10 , 'bold') ,align='center')
    
    for i in range(0, ne):  
        index = (arr[i]/exp1)
        d.arrow( c_input_i_arrow , i ,  col="#09CC12",text="i"+str(exp1) , name=c_input_Position)
     
        d.setPosition( -100, 400) 
        verPos=d.vertical
        horPos=d.horizontal
        
        if i == 0 :                          
              d.Array(c_count_array , Count , length=100 , width=100 , xcor=horPos , ycor=verPos,IndexArray=True,nameA=c_count_Position)
              c_title.goto(c_title.xcor(),c_title.ycor()-400)
              c_title.write("Count Array ", font=("Lobster" , 10 , 'bold') ,align='center')
        
        ind=int(index%10)      
        d.Blen=100
        d.Bwid=100 
        d.arrow( c_count_key_arrow , ind ,col="#09CC12",text="++ "+str(Count[ind]) , name=c_count_Position)
        Count[ind] += 1
        
        #dist=horPos+(104*ind)+(d.Gap*(ind-1))
        #time.sleep(0.6)
        
        
        d.rect(c_count_key_update , x=c_count_Position[ind][0]-d.Blen*0.38 , y=c_count_Position[ind][1]-d.Bwid*0.25 , length=100 , width=100 , cradius=10 ,data= Count[ind] ,stroke=1,color="#C1AEFC" )
        
        
        
        time.sleep(2)
        c_count_key_arrow.clear()
        c_input_i_arrow.clear()
        d.setPosition( 100, -400) 
        d.Blen=100
        verPos=d.vertical+10
        horPos=d.horizontal
      
    d.setPosition( -100, 800) 
    verPos=d.vertical
    horPos=d.horizontal 
    
    for i in range(1, 10):
            if i==1:
                  d.Array(c_count_update_array , Count , length=100 , width=100 , xcor=horPos , ycor=verPos,IndexArray=True, nameA=c_up_count_Position )
                  c_title.goto(c_title.xcor(),c_title.ycor()-400)
                  c_title.write("Count Update Array ", font=("Lobster" , 10 , 'bold') ,align='center')
                           
            d.arrow( c_count_update_arrow , i ,col="#09CC12",text=str(Count[i-1])+" + "+str(Count[i]) , name=c_up_count_Position)
          
            Count[i] += Count[i - 1]
          
            #dist=horPos+(104*i)+(d.Gap*(i-1))
            #time.sleep(0.7)
            d.rect(c_count_update_key_update , x=c_up_count_Position[i][0]-d.Blen*0.38 , y=c_up_count_Position[i][1]-d.Bwid*0.25 , length=100 , width=100 , cradius=10 ,data= Count[i] ,stroke=1,color="#C1AEFC" )
                  
            c_count_update_arrow.clear()
                
    d.setPosition( 100, 400) 
    verPos=d.vertical
    horPos=d.horizontal 
    d.Blen=100
    i=ne-1     
    
    while i >= 0:
        index = (arr[i]/exp1)
        
        x=Count[int(index)%10]-1
        if i == ne-1:    
              d.Array(c_output_array , Output , length=100 , width=100 , xcor=horPos , ycor=verPos,IndexArray=True , nameA=c_output_Position)  
              c_title.goto(c_title.xcor(),c_title.ycor()-400)
              c_title.write("Output Array ", font=("Lobster" , 10 , 'bold') ,align='center')          
        d.arrow( c_input_i_arrow , i ,  col="#09CC12",text="i" , name=c_input_Position)
        
        d.arrow( c_output_i_arrow , x ,  col="#09CC12",text="Place Input[ i ] at this index" , name=c_output_Position)
        
        #dist=horPos+(104*x)
        Output[x] = arr[i]
        
        Count[int((index)%10)] -= 1
        
        #time.sleep(0.7)
        d.rect(c_output_key_update , x=c_output_Position[x][0]-d.Blen*0.38 , y=c_output_Position[x][1]-d.Bwid*0.25, length=100 , width=100 , cradius=10 ,data= arr[i] ,stroke=1,color="#C1AEFC" )
        
        c_output_i_arrow.clear()
        c_input_i_arrow.clear()
        i -= 1  
        
    for i in range (ne):          
             arr[i]=OPA[i]= Output [i]          
             Output[i]=0
    for i in range (10):          
            Count [i] = 0 
    
    
    time.sleep(exp1)
    c_title.clear()
    c_title.up()
    c_title.goto(c_titlex , c_titley)
    c_count_key_update.clear()
    c_count_update_key_update.clear()
    c_output_key_update.clear()
    
    c_output_array.clear()
    c_count_update_array.clear()
    c_count_array.clear()
    c_input_array.clear()
    c_input_Position.clear()
    c_count_Position.clear()
    c_up_count_Position.clear()
    c_output_Position.clear()
    
#-----------end Method to do Radix Sort-----------

def radix_Sort(screen , arr):
 
    # Find the maximum number to know number of digits

    max1 = max(arr) 
    # Do counting sort for every digit. Note that instead
    # of passing digit number, exp is passed. exp is 10^i
    # where i is current digit number
    exp = 1

    while max1//exp > 0:
        count_Sort(arr,exp , screen)
        d.setPosition( 50 , -1200) 
        exp *= 10 
        
    
#-------------  Function to handle the window closing event -------------- #

def close_window_radix_sort(screen ):
    try:
        d.setPosition( )
        c_input_Position.clear()
        c_count_Position.clear()
        c_up_count_Position.clear()
        c_output_Position.clear()
        
        radix_Sort(screen , d.num)
        d.setPosition( )
        time.sleep(5)
        #d.screen.bye()  # Close the turtle window
    except turtle.Terminator:
        pass  # Catch the Terminator error and do nothing
    except Exception as e:
        pass 
        print("An error occurred:", str(e))  # Handle any other exception and print an error message


##### ----------------- Main Driver Program ------------------- #####

# Set the close_window function to handle the window closing event

#d.screen.onkey(close_window_count_sort, "q")
#d.screen.listen()

d.setPosition( 0 , -50)
close_window_radix_sort( screen )

