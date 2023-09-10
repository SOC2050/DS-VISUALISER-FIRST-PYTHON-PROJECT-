import turtle 
import tkinter as tk
from tkinter import Menu, messagebox
from tkinter import ttk
import random 
from PIL import ImageTk, Image
import importlib
#--> Toggle frame and Button releted Variables 
toggle_menu_frame=None
toggle_btn=None
info_frame=None
appear=False

#--> Animation related Variables 
animation_frame=None
label_frame=None
text_widget = None
scrollbar = None 
canvas  = None
screen=None

#--> Animation frame height and width

animation_frame_height = 0
animation_frame_width = 0

#-------------> Animation and textual section start <------------------


def create_scrollable_window():
    global text_widget , scrollbar , label_frame

    # Create a Text widget
    text_widget = tk.Text(label_frame, bg="black", fg="white", bd=0, highlightthickness=0)
    text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Create a Scrollbar
    scrollbar = ttk.Scrollbar(label_frame, orient="vertical", command=text_widget.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Apply the Scrollbar to the Text widget
    text_widget.configure(yscrollcommand=scrollbar.set)


# Animation pause Play functionality

#-----> function for pause animation function

def pause_animation():
      
    messagebox.showinfo("Message", "Animation is Stoped,  To Continue \n\t Press Ok")

def del_menu():
    
    global animation_frame , canvas , label_frame , text_widget , scrollbar , appear
    
    appear=False

    if canvas is not None:
        canvas.destroy()
    if label_frame is not None:
        label_frame.destroy()
    if text_widget is not None:
        text_widget.destroy()
    if scrollbar is not None :
        scrollbar.destroy()
    if animation_frame is not None:
        animation_frame.destroy()
        
    label_frame = None
    text_widget = None
    scrollbar = None
    
    if  info_frame.winfo_exists() and not appear :
            bottom_frame.pack_forget()
            info_frame.pack(fill="both" , expand=True)




def Animating (type, name, file):
         text_form(type , name)       
         #very important       
         if type == "sort" : 
             text_form(type , name)
             module =  importlib.import_module(file)
             _running_function= getattr(module , "close_window_" + name+"_sort", None) or getattr( module , "close_window_" + name+"_sort" , None)
             _running_function(screen)

         elif type == "linkedlist" : 
             text_form(type , name)
             module =  importlib.import_module(file)
             _running_function= getattr(module ,  name , None) or getattr( module , name , None)
             _running_function(screen)    
                               
         elif type == "stack" : 
             text_form(type , name)
             module =  importlib.import_module(file)
             _running_function= getattr(module ,  name , None) or getattr( module , name , None)
             _running_function(screen)            

         elif type == "search" : 
             text_form(type , name)
             module =  importlib.import_module(file)
             _running_function= getattr(module ,  name , None) or getattr( module , name , None)
             _running_function(screen)            

         elif type == "array" : 
             text_form(type , name)
             module =  importlib.import_module(file)
             _running_function= getattr(module ,  name , None) or getattr( module , name , None)
             _running_function(screen)                                    



 
def create_canvas(frame , type , name, file):
    global canvas , screen 
    canvas = tk.Canvas(frame, bg="blue",width=animation_frame_width*0.88, height=animation_frame_height*0.975)
                  
    canvas.place(x=0,y=0)
    
    button_frame = tk.Frame(frame, width=animation_frame_width*0.1, height=animation_frame_height*0.975 , bg="green")
    button_frame.place( x=animation_frame_width*0.883, y=1)
    tk.Button (button_frame, text="X", bg="green" ,highlightthickness=0 ,command= del_menu, padx=(animation_frame_width*0.10)*0.333, pady=10).place( x=1 , y=1)  
    tk.Button (button_frame, text="P", bg="green" ,highlightthickness=0 ,command= del_menu, padx=(animation_frame_width*0.10)*0.333, pady=10).place( x=1 , y=100)
    tk.Button (button_frame, text="A", bg="green" ,highlightthickness=0 ,command= del_menu, padx=(animation_frame_width*0.10)*0.333, pady=10).place( x=1 , y=80*2+20)   
    tk.Button (button_frame, text="U", bg="green" ,highlightthickness=0 ,command= del_menu, padx=(animation_frame_width*0.10)*0.333, pady=10).place( x=1 , y=80*3+20) 
    tk.Button (button_frame, text="S", bg="green" ,highlightthickness=0 ,command= del_menu, padx=(animation_frame_width*0.10)*0.333, pady=10).place( x=1 , y=80*4+20)   
    tk.Button (button_frame, text="E", bg="green" ,highlightthickness=0 ,command= del_menu, padx=(animation_frame_width*0.10)*0.333, pady=10).place( x=1 , y=80*5+20)       
   
    screen =turtle.TurtleScreen(canvas)  
    
    Animating (type, name, file)

  
      
  
    
   

#------> Function tion for drawing animation in Canvas

def Animation(type , name , file  , extra=None ):
         global p_b_btn, animation_frame , label_frame , canvas , appear , screen 
         
         appear=True
 
  
         collapse_menu()
         # Creating frame
         animation_frame = tk.Frame(bottom_frame, highlightthickness=10 , highlightbackground="red" ,  bg="white"  , relief=tk.SUNKEN, )
         
         label_frame = tk.Frame(bottom_frame, highlightthickness=10 , highlightbackground="red" ,  bg="white"  , relief=tk.SUNKEN, )
        
         animation_frame.pack(side = tk.RIGHT ,  fill=tk.BOTH , expand= True)
         
         label_frame.pack(side = tk.LEFT , fill=tk.BOTH ,  expand=True)
         
         #create_scrollable_window()
         animation_frame.after(100, lambda:create_canvas(animation_frame , type, name, file))
         #create_canvas(animation_frame)
 
        

         


         
#----> Function for Textual Representation <-------

def text_form(type , filename):
       global label_frame 
       global text_widget
       
       def read_file(filename):
              with open(filename, 'r') as file:
                      data = file.read()
              return data
       

       create_scrollable_window()
       # Add text to the text widget
       text_widget.insert(tk.END,read_file(f"{filename}.txt"))

      

#-------> function for collapse menu at left side of window

def collapse_menu():
    global toggle_menu_frame
    global toggle_btn
    
    

    if animation_frame is not None and animation_frame.winfo_exists():
        messagebox.showinfo("Message", "Please close the red frame first.")
    else:
        if  info_frame.winfo_exists() and not appear :
            bottom_frame.pack_forget()
            info_frame.pack(fill="both" , expand=True)
  
        if toggle_menu_frame is not None:
            toggle_menu_frame.destroy()
        toggle_btn.config(text='☰')
        toggle_btn.config(command=toggle_menu)
        toggle_menu_frame = None

    





#------> Function for button of menus


def create_new_button(type,frame ,Row ,menu_list ):
       
       name=type+"_btn"
       name = tk.Menubutton(frame, text=type ,bd=2, bg="#158aff", fg="white", font=('Blod', 13), activebackground="#158aff", highlightthickness=2 , pady=5 , padx=50  )

       menu = Menu(name , tearoff=False, bd=3 , activeborderwidth=0, activeforeground="black", fg="white",                  activebackground="#158aff")
      
       for key, values in menu_list.items():    
       
             #menu.add_command(label="   ")
             """
             str_key = str(key)
             menu.add_command(label=str_key, command=lambda k=str_key: Animation(type , values[0], values[1]))
             menu.add_command(label="   ")
             """
             menu.add_command(label=key , command= lambda : Animation ( type, values [0]   , values [1] ))
             menu.add_command(label="   ")
             
       
       
       menu.config(bg="#158aff")
       name.config(menu=menu )
       
       name.grid(row=Row , column=0 , sticky="ew" )
       
       
       
#------> Function for creating toggle menu at the left side of window

def toggle_menu():
    
    global toggle_menu_frame , toggle_btn , R
    
      
    if info_frame.winfo_exists():
        info_frame.pack_forget()
        bottom_frame.pack(fill="both", expand=True)
        
    if animation_frame is not None and animation_frame.winfo_exists():
        messagebox.showinfo("Message", "Please close the Running Animation first. \n\tPress on Ok")
    elif toggle_menu_frame is not None and toggle_menu_frame.winfo_ismapped():
        collapse_menu()
    else:
       if toggle_menu_frame is not None:
            toggle_menu_frame.destroy()
            
       toggle_menu_frame = tk.Frame(bottom_frame , bg="#B9F3FC")
        # ... Rest of the code for creating the menu buttons ...
        
       toggle_menu_frame.pack( side = tk.LEFT, anchor="w" ,fill=tk.Y, expand= True)
       toggle_menu_frame.pack_propagate(False)
       toggle_menu_frame.configure(width=500)


       # --> For Array and it's Subfields       
        
       array_list = {
    "2D Array": ["two_D_array", "two_Darray"],
    "2D Array Traverse": ["two_D_traversal", "two_Dtraversal"],
    "2D Addition": ["Addition", "Addition_2D"],
    "2D Substraction": ["Substraction", "Substraction_2D"],
    "2D Multiplication": ["Multiplication", "Multiplication_2D"],
    "2D Division": ["Division", "Division_2D"] }
    
       create_new_button("array", toggle_menu_frame , 0  , array_list )
       
       # --> For Sorts and Subfields       
                             
       sort_list = {
    "Bubble Sort": ["bubble", "Bubble_Sort"],
    "Quick Sort": ["quick", "Quick_Sort"],
    "Selection Sort": ["selection", "Selection_Sort"],
    "Insertion Sort": ["insertion", "Insertion_Sort"],
    "Shell Sort": ["shell", "Shell_Sort"],
    "Count Sort": ["count", "Count_Sort"],
    "Radix Sort": ["radix", "Radix_Sort"] }

       create_new_button("sort", toggle_menu_frame , 1 , sort_list )

       # --> for Linked List and Subfields
       
       linked_list = {
    "Insert At Beginning": ["insert_beg", "Insertion_At_Beggining"],
    "Insert In Between": ["insert_bet", "Insertion_In_Between"],
    "Insert At End": ["insert_end", "Insertion_At_End"],
    "Delete At Beginning": ["delete_beg", "Deletion_At_Begginig"],
    "Delete In Between": ["delete_bet", "Deletion_In_Between"],
    "Delete At End": ["delete_bet", "Deletion_At_End"] }
    
       create_new_button("linked_list", toggle_menu_frame , 2 , linked_list )

       # --> For Stack and Subfields        
             
       stack_list = {
    "Create Stack": ["create", "Create_Stack"],
    "Push In Stack": ["Push", "Push_In_Stack"],
    "Pop From Stack": ["Pop", "Pop_In_Stack"] }
    
       create_new_button("stack", toggle_menu_frame , 3 , stack_list )

       # --> For Queue and Subfields     
                 
       queue_list = {
    "Create Queue": ["create", "Create_Queue"],
    "Inqueue in Queue": ["Inqueue", "Inqueue_in_Queue"],
    "Dequeue in Queue": ["Dequeue", "Dequeue_in_Queue"] }

       create_new_button("queue", toggle_menu_frame , 4 , queue_list )
       
       # --> For Searching Algorithms  and Subfields 
              
       search_list = {
    "Linear Search": ["linearSearch", "Linear_Search"],
    "Binary Search": ["binarySearch", "Binary_Search"] }
    
       create_new_button("search", toggle_menu_frame , 5 , search_list )
    
      
       #----> for changing X buttons
     
       toggle_btn.config(text="X")
       toggle_btn.config(command=collapse_menu)





#------------> All Frames Adjecement Function<------------

def adjust_frames(event):
    global animation_frame_height , animation_frame_width , width, height
    
    root.update_idletasks()  # Update window and frame sizes
   
    # Get the available width and height
    width = root.winfo_width()
    height = root.winfo_height()
    
    # Calculate heights for top and bottom frames
    top_frame_height = height // 10
    bottom_frame_height = height - top_frame_height
    
    # Calculate widths for left and right frames
    left_frame_width = width // 3
    right_frame_width = width - left_frame_width
    
    # Adjust frame sizes based on available space
    top_frame.config(height=top_frame_height)
    bottom_frame.config(height=bottom_frame_height)
    
    info_frame.config(height=bottom_frame_height)
    
    if label_frame is not None and animation_frame is not None:
        label_frame.config(width=left_frame_width)
        animation_frame.config(width=right_frame_width)
        
        animation_frame_height = animation_frame.winfo_height()
        animation_frame_width = animation_frame.winfo_width()
        print("Right Frame Height:", animation_frame_height)
        print("Right Frame Width:", animation_frame_width)
        
        """
        if canvas is not None:
            #animation_frame.bind("<Configure>", adjust_canvas_size)
            canvas.config(width=animation_frame_width, height=animation_frame_height)
        """   
    

def del_frame(frame):
    frame.pack_forget()

def DSA_info(frame):
    
    #set_image(frame)

    canvas = tk.Canvas(frame ,highlightthickness=10 , highlightbackground="purple",  relief=tk.SUNKEN )
                  
    canvas.pack(fill="both" , padx=150 ,pady=100 )
        
    screen = turtle.TurtleScreen(canvas)
    
    screen.bgcolor("#B9F3FC")
    width = screen.window_width()
    height = screen.window_height()
    
    t = turtle.RawTurtle(screen)
    t.speed(0)
    
    # Position the turtle
    t.up()
    t.goto(-width//2+80 , height//4)
    t.shape("square")
    t.shapesize(.1,1)
    
    name_list = ["Hi", "I", "am", "Madara", "Uchiha", "and", "I", "am", "Hashirama", "sanju"]
    
    text0="     What is DSA  ?A data structure is a way to organize and store data efficiently, while an algorithm is a step-by-step procedure  to solve a specific problem. Data structures define how data is  arranged in memory. Algorithms are sets of instructions that manipulate data to achieve a desired outcome. They're fundamental concepts in   computer science for developing efficient and optimized  software solutions !..."
    
    text1="what is the importance of DSA? 1. Data structures and algorithms form the backbone of efficient problem-solving in software development.2. They enable optimized storage and retrieval of information, powering the functionality of countless applications.3. Mastery of data structures and algorithms is key to writing scalable and high-performance code.4. Efficient algorithms and well-chosen data structures are the foundation for crafting responsive and user-friendly software.5. In the world of computing, data structures and algorithms are the compass guiding the creation of innovative and impactful solutions."
    
    text2="why we need to use DSA? 1. Data structures organize and manage data for efficient storage and retrieval.2. Algorithms provide systematic steps to solve problems and process data.3. They optimize resource usage, improving program speed and memory efficiency.4. Proper use leads to scalable software, accommodating larger datasets and user bases.5. Together, they empower developers to create effective and responsive applications."
    
    text3="why data structures are created ? Data structures are created to address the need for organizing and managing data in a way that optimizes operations such as insertion, deletion, searching, and sorting. By structuring data effectively, they enhance the efficiency and performance of algorithms that operate on the data. These structures are designed to suit different scenarios and use cases, ensuring that data can be accessed quickly and in an organized manner, leading to more streamlined and effective software development."
    
    text4="what are the advantages of DSA? 1. Data structures enable efficient data organization, enhancing accessibility and management.2. Algorithms provide systematic solutions, optimizing problem-solving processes.3. They improve program performance by reducing time and resource consumption.4. Well-chosen structures and algorithms lead to scalable and adaptable software.5. Mastery empowers developers to create faster, responsive, and innovative applications."
    
    text5="what are the disadvantages of DSA ? 1. Poorly designed data structures can lead to inefficient memory usage and slower operations.2. Complex algorithms might be hard to implement, understand, and maintain.3. Incorrect algorithm selection can result in suboptimal performance and resource waste.4. Developing and optimizing data structures and algorithms can be time-consuming.5. Overemphasis on optimization might sacrifice code readability and maintainability."
    
    text_list = [text0, text1, text2, text3, text4, text5]
    text= random.choice(text_list)
    
    word_list = text.split()
   

    # Loop through each word in the list
    for word in word_list:
          # Loop through each letter in the word
          #t.showturtle()
          for letter in word:
                if letter=='m':
                    t.forward(3)
                    
                if  letter.isdigit():
                    t.speed(0)
                    if letter=='1':
                        
                        t.goto(-width//2+70 , t.ycor())
                    else:
                        
                        t.goto(-width//2+70 , t.ycor()-60)
                    t.pencolor("blue")
                    
                t.write(letter, align='center', font=("Arial", 7, "normal"))
                t.pencolor('black')
                
                if letter=='m':
                    t.forward(3)
                #t.hideturtle()
                
                t.forward(24)  # Adjust the distance between letters
                if t.xcor() > width//2-80  :
                    if letter !='  ':
                        t.write("-", align='center', font=("Arial", 7, "normal"))
                        #pass

                    else:
                        pass
                        #t.write("-", align='center', font=("Arial", 7, "normal"))
                    t.speed(0)
                    t.goto(-width//2+100 , t.ycor()-60)
                    
                    
                if letter=='?':
                    t.speed(0)
                    t.goto(-width//2+200 , t.ycor()-70)
                    

          # Add a space after each word
          t.forward(28)  # Adjust the distance between words
          t.speed(0)
         




def get_bg_col(image_path, x, y):
    image = Image.open(image_path)
    pixel = image.getpixel((x, y))
    return "#%02x%02x%02x" % pixel[:3]
    

#------> function for setting background image of starting frame of app

def set_image(frame ):
    
    label = tk.Label(frame)
    label.place(x=0 ,y=0)
    image = Image.open('bg1.jpg')
    frame_width = frame.winfo_width()
    frame_height = frame.winfo_height()
    resized_image = image.resize((frame_width, frame_height))

    # Keep a reference to the image to avoid garbage collection
    label.image = ImageTk.PhotoImage(resized_image)
    label.configure(image=label.image)
    
#---------------------------------------------------------------------------------------------------    
#------------------------------> Main Application <-----------------------------------
#---------------------------------------------------------------------------------------------------
    
root = tk.Tk()

root.geometry("1920x1080")


#root.attributes("-fullscreen", True)
root.minsize(1920,1080)
root.maxsize(1920,1080)

root.title("DSA")
set_image(root)
# Create top and bottom frames
top_frame = tk.Frame(root, bg="#158aff")
bottom_frame = tk.Frame(root, bg="lightblue")

# Place frames using pack layout
top_frame.pack(fill="both")
#bottom_frame.pack(fill="both", expand=True)


info_frame=tk.Frame(root, bg="lightpink",highlightthickness=10 , highlightbackground="orange",  relief=tk.SUNKEN )



info_frame.pack(fill="both"  , expand=True)

DSA_info(info_frame)


#---> this is the toggle button which can open a frame on the left side of the main window
toggle_btn = tk.Button(top_frame, text='☰', bg="#158aff", fg="white", font=('Bold', 13), bd=0,activebackground="#158aff", command=toggle_menu , activeforeground="white" , highlightthickness=0)
#toggle_btn.pack(side=tk.LEFT)
toggle_btn.place(x=-30,y=-10)


title_label = tk.Label(top_frame, text="D.S.A ", padx=20, bg="#158aff", fg="white",font=('Bold', 13)  )
title_label.place(x=150 , y=5)


# Bind resize event to adjust frames
root.bind("<Configure>", adjust_frames)

bottom_frame.bind("<Configure>", lambda event: set_image(bottom_frame))
#root.bind("<Configure>", lambda event: set_image(root))


root.mainloop()
