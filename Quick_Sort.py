from turtle import*
import turtle 
import time
import __main as d

#d.setPosition( 200 , 100)


screen=None
q_Position=[]

verPos=d.vertical
horPos=d.horizontal
#------------- Function to find the partition position for Quick sort ------------

count=0
def  Partition(arr , lb , ub , screen ) :
      global q_Position
      global horPos
      global verPos 
      global count      
      # arr- Array for Partitioning 
      # lb - Lower Bound of Array or first index
      # ub - Upper Bound of Array or Last index       
     
      d.createObject('txi', screen , visibility=False ,speed=0)
      d.createObject('txj', screen, visibility=False , speed=0)  
      d.createObject('q_title', screen ,  visibility=False ,speed=0)
      d.createObject('q_array', screen ,  visibility=False,speed=0)
      d.createObject('q_lbarrow', screen , visibility=False,speed=0)
      d.createObject('q_ubarrow', screen, visibility=False,speed=0)
      d.createObject('q_startarrow', screen ,  visibility=False,speed=0)
      d.createObject('q_endarrow', screen ,  visibility=False,speed=0)
      d.createObject('q_comparing', screen , visibility=False,speed=0)
      d.createObject('q_swap_start', screen , visibility=False,speed=0)
      d.createObject('q_swap_end', screen , visibility=False,speed=0)
      d.createObject('q_swap_pvt', screen ,  visibility=False,speed=0)
      # Accessing object create by function
      q_title = d.q_title
      q_array = d.q_array 
      q_lbarrow = d.q_lbarrow
      q_ubarrow = d.q_ubarrow
      q_startarrow = d.q_startarrow
      q_endarrow = d.q_endarrow
      q_comparing = d.q_comparing
      q_swap_start = d.q_swap_start
      q_swap_end = d.q_swap_end
      q_swap_pvt = d.q_swap_pvt
      
      if count <=0:
           q_title.up()
           q_title.goto(horPos+len(d.num)/2*100,verPos+250)
           q_title.write("Quick Sort ", font=("Lobster" , 12 , 'bold') ,align='center')
           
      if not isinstance (arr,list):
           raise TypeError ("arr must be List ")
      if not isinstance (lb,int) and lb< 0 :
            raise ValueError ("lb must be positive and <=0")
            
      if not isinstance (ub,int) and ub > n :
             raise ValueError ("ub out of index")
        
      count+=2
      pivot = arr[lb]     
      start = lb
      rstart=lb
      end = ub
      rend= ub

      d.Array(q_array , arr , length=100 , width=100 , xcor=horPos , ycor=verPos,IndexArray=True , nameA=q_Position)
    
      d.arrow( q_lbarrow , lb ,  col="#54B435",text="P==S" , name = q_Position )
      d.arrow( q_ubarrow , ub , col="#289672",text="end" , name = q_Position)
   
      while (start < end ) :
            
            for start in range (rstart, len( arr ) ):
                  
                  d.Comparator( q_comparing ,  lb , start ,col="red", type="quick", insert="lb" , name=q_Position)
                           
                  if ( arr[start ] > pivot ):
                        q_lbarrow.clear()
                        q_startarrow.clear()
                        d.arrow( q_startarrow , start , col="red",text="start" , name=q_Position)
                                     
                        d.arrow( q_lbarrow , lb , col="green",text="Pvt" , name=q_Position)
                        rstart=start
                        break   
              
            for end in range ( rend , -1 ,-1 ):
                  d.Comparator( q_comparing ,  lb , end  ,col="red" , type="quick", insert="ub" , name=q_Position)
                                 
                  if ( arr[end] <= pivot ):
                        
                        q_ubarrow.clear()
                        q_endarrow.clear()
                        d.arrow( q_endarrow , end ,  col="red",text="end", name=q_Position)
                 
                        rend=end
                        break  
            
            if start < end :                 
                  arr[start] , arr[end] = arr[end] , arr[start]
                  
                  d.Comparator( q_comparing ,  start , end  , col="#54B435" , type="quick", insert="start_end" , name=q_Position )
                  d.swapBoxes( q_swap_start , q_swap_end  , start , end  , idata = arr[ end ], jdata = arr[ start ] , name=q_Position )
                  
                  q_startarrow.clear()
                  q_endarrow.clear()
                  
                  d.arrow( q_startarrow , rstart , col="red",text="start" , name=q_Position )
                  d.arrow( q_endarrow , rend , col="red",text="end" , name=q_Position)
                                            
      arr[lb] , arr[end] = arr[end] , arr[lb]
      d.Comparator( q_comparing ,  lb , end , col="green" , type="quick", insert="pvt_end"  , name = q_Position )
      d.swapBoxes( q_swap_pvt , q_swap_end  , lb ,  end , idata = arr[ end ], jdata= arr[ lb ] , name=q_Position )
      q_startarrow.clear()
      q_endarrow.clear()
      verPos=verPos - 250
      q_Position.clear()
      
      return end  
         
#----------Partition function end ---------------
  
#-----------function for quick  sort quick sort Algorithm ----------- 
def Quick_Sort(arr , lb , ub  , screen) :
           
      if lb < ub :
            loc = Partition ( arr , lb ,ub , screen)
            Quick_Sort( arr , lb , loc - 1 , screen)
            Quick_Sort( arr , loc + 1 , ub , screen )
                     

#--------------  Function to handle the window closing event -------------- #

def close_window_quick_sort( screen):
    try:
        d.setPosition( )
        q_Position.clear()
        Quick_Sort(d.num,0,len(d.num)-1 , screen)
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

#d.screen.onkey(close_window_quick_sort, "q")
#d.screen.listen()


close_window_quick_sort(screen  )
