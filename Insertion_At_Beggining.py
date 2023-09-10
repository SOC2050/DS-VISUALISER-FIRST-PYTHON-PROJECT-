
import Main_ll as ll
import __main as d
import turtle
import time 
from turtle import *

screen=None

llist = [2, 4, 3, 1]
data = 10

def insert_At_Beginning(data , screen):
    bgcol="#B9F3FC"
    screen.bgcolor(bgcol)
    d.createObject('ib_Null', screen,  visibility=False , speed=0, color="black")
    
    d.createObject('ib_title', screen, visibility=False, speed=0, color="black")
    d.createObject('ib_steps', screen, visibility=False, speed=0, color="black")
    d.createObject('ib_nodes', screen, visibility=False, speed=0, color="black")
    d.createObject('ib_links', screen, visibility=False, speed=0, color="black")
    d.createObject('ib_newnode', screen, visibility=False, speed=0, color="black")
    d.createObject('ib_links1', screen, visibility=False, speed=0, color="black")
    d.createObject('ib_newnodearrow', screen, visibility=False, speed=0, color="black")
    d.createObject('ib_newnodelink', screen, visibility=False, speed=3, color="red")
    d.createObject('ib_head', screen, visibility=False, speed=0, color="black")
    d.createObject('ib_tail', screen, visibility=False, speed=0, color="black")
    d.createObject('ib_head1', screen, visibility=False, speed=0, color="black")
    d.createObject('ib_tail1', screen, visibility=False, speed=0, color="black")
    d.createObject('ib_newhead', screen, visibility=False, speed=0, color="black")
    d.createObject('ib_newtail', screen, visibility=False, speed=0, color="black")  
    ib_nodes = d.ib_nodes
    ib_newnodearrow = d.ib_newnodearrow
    ib_newnodelink = d.ib_newnodelink
    ib_links = d.ib_links
    ib_newnode = d.ib_newnode
    ib_links1 = d.ib_links1
    ib_head = d.ib_head
    ib_tail = d.ib_tail
    ib_head1 = d.ib_head1
    ib_tail1 = d.ib_tail1
    ib_newhead = d.ib_newhead
    ib_newtail = d.ib_newtail
    ib_title = d.ib_title
    ib_steps = d.ib_steps
    ib_Null=d.ib_Null
    
    ib_title.up()
    ib_steps.up()
    ib_title.goto(d.horizontal + 50, d.vertical)
    ib_title.write("Linked List :", font=("normal", 12, "bold"))

    d.setPosition(200, 300)
    ll.LinkedList(ib_nodes, ib_links, ib_head, ib_tail, llist, length=90, width=100 , null=ib_Null)

    d.setPosition(0, 200)
    ib_title.goto(d.horizontal - 200, d.vertical)
    ib_title.write("Insertion At Beginning in LL :", font=("normal", 12, "bold"))
    ll.LinkedList(ib_nodes, ib_links, ib_head1, ib_tail1, llist, yPos=250, length=90, width=100 , null=ib_Null)

    ib_steps.goto(d.horizontal + 80, d.vertical - 350)
    ib_steps.write("Step 1: Create New Node with given Data", font=("normal", 6, "bold"))
    time.sleep(1.2)
    ll.node(ib_newnode, xcor=d.horizontal + 160, ycor=d.vertical - 80, lengthN=90, widthN=100, cradiusN=10, dataN=data, IndexN=False)

    ib_newnodearrow.left(180)

    ll.head(ib_newnodearrow, pos=None, x=ll.arrowPos[0][0], y=ll.arrowPos[0][1] - (ll.nodewid * 0.3), col="green", text="newNode", dir="up")

    ib_steps.goto(ib_steps.xcor(), ib_steps.ycor() - 50)
    ib_steps.write("Step 2: Make newNode -> next = head", font=("normal", 6, "bold"))
    time.sleep(1.2)
    ib_newnodelink.showturtle()
    ib_newnodelink.up()
    ib_newnodelink.goto(ll.arrowPos[0][0] + (ll.nodelen), y=ll.arrowPos[0][1] + (ll.nodewid * 0.25))
    ib_newnodelink.pencolor("red")
    ib_newnodelink.pensize(5)
    ib_newnodelink.fillcolor("red")
    ib_newnodelink.shape("classic")
    ib_newnodelink.shapesize(5)
    ib_newnodelink.down()
    ib_newnodelink.forward((ll.nodewid * 0.5))
    ib_newnodelink.left(90)
    ib_newnodelink.forward((ll.nodewid * 0.75))
    ib_newnodelink.left(90)
    ib_newnodelink.forward((ll.nodelen * 0.5))
    ib_newnodelink.right(90)
    ib_newnodelink.forward((ll.nodewid * 0.90))
    ib_newnodelink.right(90)
    x = ll.nodelen * 0.4
    xx = x / 2 + 2
    ll.link(ib_newnodelink, xcor=ib_newnodelink.xcor() - xx, ycor=ib_newnodelink.ycor())
    ib_newnodelink.hideturtle()

    ib_steps.goto(ib_steps.xcor(), ib_steps.ycor() - 50)
    ib_steps.write("Step 3: Make head = newNode", font=("normal", 6, "bold"))
    time.sleep(1.2)

    ib_head1.clear()
    ll.head(ib_head1, x=ll.arrowPos[0][0], y=ll.arrowPos[0][1] + (ll.nodewid * 0.80), col="green", text="head")

    ll.arrowPos.clear()
    d.setPosition(-150, 700)
    ib_title.goto(d.horizontal - 50, d.vertical)
    ib_title.write("After Insertion in LL :", font=("normal", 12, "bold"))
    llist.insert(0, data)
    ll.LinkedList(ib_nodes, ib_links, ib_newhead, ib_newtail, llist, yPos=250, length=90, width=100, null=ib_Null)

# Function to handle the window closing event
def insert_beg(screen):
    try:
        d.setPosition( )
        insert_At_Beginning(data , screen)
        time.sleep(5)
        d.setPosition( )
        #d.screen.bye()  # Close the turtle window
    except turtle.Terminator:
        pass  # Catch the Terminator error and do nothing
    except Exception as e:
        pass 
        print("An error occurred:", str(e))  # Handle any other exception and print an error message

# Set the close_window function to handle the window closing event
#d.screen.onkey(close_window_insert

insert_beg(screen)
