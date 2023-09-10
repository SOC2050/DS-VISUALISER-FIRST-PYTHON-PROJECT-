from turtle import*
import turtle 
import time
import __main as d

hig=0   
bi_Position=[]      
screen=None          

array=[5,7,12,17,34,42,67]
def binary_search(arr, low, high, data , screen ):
    global hig
    global array

    d.createObject('bi_title', screen , visibility=False ,speed=0)
    d.createObject('bi_array', screen, visibility=False , speed=0)
    d.createObject('bi_low', screen , visibility=False ,speed=0)
    d.createObject('bi_mid', screen,  visibility=False ,speed=0)
    d.createObject('bi_high', screen ,  visibility=False ,speed=3)
    d.createObject('bi_comparing', screen , visibility=False,speed=0)
    d.createObject('bi_data', screen , visibility=False,speed=0)
  
    bi_title = d.bi_title
    bi_array = d.bi_array # Accessing object create by function
    bi_low = d.bi_low
    bi_mid = d.bi_mid
    bi_high = d.bi_high
    bi_comparing = d.bi_comparing
    bi_data = d.bi_data
    
    # Check base case

    n=len(arr)
    midm=0
    
    
    
    verPos=d.vertical
    horPos=d.horizontal
    bi_title.up()
    bi_title.goto(horPos+len(arr)/2*100,verPos+250)
    bi_title.write("Binary Search ", font=("Lobster" , 12 , 'bold') ,align='center')
    bi_Position.clear()
    d.Array(bi_array , arr , length=100 , width=100 , xcor=horPos , ycor=verPos - hig*300 ,IndexArray=True , nameA=bi_Position)
    
    d.rect(bi_array, x=bi_array.xcor() + d.Blen*0.7,y=bi_array.ycor() - d.Bwid*0.25 ,length=100,  width=100 , cradius=10 ,data=data ,stroke=1, fill_color="yes" , color="green",Index=False,index=None , name=None ,  Font=6)
    d.arrow( bi_data, None , xcor=bi_array.xcor() , ycor=bi_array.ycor() + d.Bwid*0.8  , col="green",text="data" )
    
    hig=hig+1   
    
    if high >= low :
        
        d.arrow( bi_low, low  , col="green",text="low" ,name=bi_Position)
        d.arrow( bi_high, high  , col="blue",text="high" ,name=bi_Position)
 
 
       
        mid = (high + low) // 2
        midm=mid
    
        
        d.arrow( bi_mid ,mid  , col="red",text="mid" ,name=bi_Position)
 
        time.sleep(1.5)

        # If element is present at the middle itself

        if arr[mid] == data:
       
            bi_low.clear()
            bi_high.clear()
            
            d.Comparator( bi_comparing , mid , n , col="red",datai= arr[mid] , dataj=data , type="binary" ,  name=bi_Position )
      
            bi_mid.clear()
            d.arrow( bi_mid , mid   , col="green",text="Element Found" ,name=bi_Position)
 
            time.sleep(1.5)
         
            bi_mid.clear()
            
            return mid
 

        # If element is smaller than mid, then it can only
 
        # be present in left subarray

        elif arr[mid] > data:
       
            bi_low.clear()
            bi_high.clear()
           
            d.Comparator( bi_comparing , mid , n , col="red",datai= arr[mid] , dataj=data , type="binary" ,  name=bi_Position )
            
            bi_mid.clear()
            d.arrow( bi_mid , mid  , col="green",text="Shirt High to Mid - 1" ,name=bi_Position)
 
            time.sleep(1.5)
         
            bi_mid.clear()
            
            
            
            return binary_search(arr, low, mid - 1, data , screen)
 

        # Else the element can only be present in right subarray

        else:
         
            bi_low.clear()
            bi_high.clear()
            
            d.Comparator( bi_comparing , mid , n , col="red",datai= arr[mid] , dataj=data , type="binary" ,  name=bi_Position )
            bi_mid.clear()
            d.arrow( bi_mid , mid , col="green",text="Shirt Low to Mid + 1" ,name=bi_Position)
            
            time.sleep(1.5)
       
            bi_mid.clear()
            
            
            
            return binary_search(arr, mid + 1, high, data , screen)
 

    else:
            # Element is not present in the array
       
            bi_low.clear()
            bi_high.clear()
            bi_mid.clear()
        
            d.arrow( bi_mid , midm , col="green",text="Element is Not Found" ,name=bi_Position)
            
            time.sleep(1.5)
          
            bi_mid.clear()
            
            
            return -1
    
  
def  binarySearch(screen):
    try:
        d.setPosition( )
        d.setPosition( -150 , -300)
        bi_Position.clear()
        
        re= binary_search(array, 0 , len(array)-1, 37 , screen) 
        d.setPosition()
        time.sleep(5)
      
    except turtle.Terminator:
        pass  # Catch the Terminator error and do nothing
    except Exception as e:
        pass 
        print("An error occurred:", str(e))  # Handle any other exception and print an error message
  
binarySearch(screen)     