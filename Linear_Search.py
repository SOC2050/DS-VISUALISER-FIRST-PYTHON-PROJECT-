from turtle import*
import turtle 
import time
import __main as d

l_Position=[]      
screen=None          


array=[5,7,12,17,34,42,67]


def linear_search(arr,data , screen):
    
    d.createObject('l_title', screen , visibility=False ,speed=0)
    d.createObject('l_array', screen, visibility=False , speed=0)
    d.createObject('l_arrow', screen , visibility=False ,speed=0)
    d.createObject('l_comparing', screen , visibility=False ,speed=0)
    d.createObject('l_data_arrow', screen , visibility=False ,speed=0)
    l_title = d.l_title
    l_array = d.l_array # Accessing object create by function
    l_arrow = d.l_arrow
    l_comparing = d.l_comparing
    l_data_arrow = d.l_data_arrow
    

    # Check base case
    n=len(arr)
    midm=0
 
    verPos=d.vertical
    horPos=d.horizontal
    l_title.up()
    l_title.goto(horPos+len(arr)/2*100,verPos+250)
    l_title.write("Linear Search ", font=("Lobster" , 12 , 'bold') ,align='center')

    l_Position.clear()
    d.Array(l_array , arr , length=100 , width=100 , xcor=horPos , ycor=verPos  ,IndexArray=True , nameA=l_Position)
    
    d.rect(l_array, x=l_array.xcor() + d.Blen*0.7,y=l_array.ycor() - d.Bwid*0.25 ,length=100,  width=100 , cradius=10 ,data=data ,stroke=1, fill_color="yes" , color="green",Index=False,index=None , name=None ,  Font=6)
    d.arrow( l_data_arrow , None , xcor=l_array.xcor() , ycor=l_array.ycor() + d.Bwid*0.8  , col="green",text="data" )
    
    find=False

    for i in range (n) :
          
        
        d.arrow( l_arrow , i , col="green",text="i" ,name=l_Position)
        
        if arr[i]==data:
               
               find = True
               d.Comparator( l_comparing , i  , n , col="red",datai= arr[i] , dataj=data , type="binary" , insert="find" ,  name=l_Position )      
               l_arrow.clear()        
      
               d.arrow( l_arrow , i , col="green",text="Element Is Found At"+str(i)+"Index" ,name=l_Position)
               
               return i

        d.Comparator( l_comparing , i  , n , col="red",datai= arr[i] , dataj=data , type="binary" , insert="not_find" ,  name=l_Position )      
        l_arrow.clear()
       
    if not find :
        
        l_data_arrow.clear()
        d.arrow( l_arrow , n-1  , col="green",text="Element Is Not Found " ,name=l_Position)
    
    
    return -1
    
    
  
def  linearSearch(screen):
    try:
        d.setPosition( )
        d.setPosition( -150 , -300)
        l_Position.clear()
     
        re= linear_search(array, 2 , screen) 
        d.setPosition()
        time.sleep(5)
        
    except turtle.Terminator:
        pass  # Catch the Terminator error and do nothing
    except Exception as e:
        pass 
        print("An error occurred:", str(e))  # Handle any other exception and print an error message
  
linearSearch(screen)     