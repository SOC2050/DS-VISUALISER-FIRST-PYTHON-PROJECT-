
import Main_ll as ll
import __main as d
import turtle
import time
from turtle import *

screen = None 
llist = [2, 4, 3, 1]
data = 10
index = 3

# --------- Function for insertion in between and last in the linked list --------- #

def insert_In_Between(data, index, screen):
    
    bgcol="#B9F3FC"
    screen.bgcolor(bgcol)

    d.createObject('ibet_Null', screen,  visibility=False , speed=0, color="black")
    
    d.createObject('ibet_title', screen, visibility=False, speed=0, color="black")
    d.createObject('ibet_steps', screen, visibility=False, speed=0, color="black")
    d.createObject('ibet_nodes', screen, visibility=False, speed=0, color="black")
    d.createObject('ibet_links', screen, visibility=False, speed=0, color="black")
    d.createObject('ibet_newnode', screen, visibility=False, speed=0, color="black")
    d.createObject('ibet_temp', screen, visibility=False, speed=0, color="black")
    d.createObject('ibet_links1', screen, visibility=False, speed=0, color="black")
    d.createObject('ibet_newnodearrow', screen, visibility=False, speed=0, color="black")
    d.createObject('ibet_newnodelink', screen, visibility=False, speed=3, color="red")
    d.createObject('ibet_head', screen, visibility=False, speed=0, color="black")
    d.createObject('ibet_tail', screen, visibility=False, speed=0, color="black")
    d.createObject('ibet_head1', screen, visibility=False, speed=0, color="black")
    d.createObject('ibet_tail1', screen, visibility=False, speed=0, color="black")
    d.createObject('ibet_newhead', screen, visibility=False, speed=0, color="black")
    d.createObject('ibet_newtail', screen, visibility=False, speed=0, color="black")
    d.createObject('ibet_extralink', screen, visibility=False, speed=0, color="black")
    d.createObject('ibet_extralinkclear', screen, visibility=False, speed=0, color="black")

    ibet_extralink = d.ibet_extralink
    ibet_extralinkclear = d.ibet_extralinkclear
    ibet_nodes = d.ibet_nodes
    ibet_newnodearrow = d.ibet_newnodearrow
    ibet_newnodelink = d.ibet_newnodelink
    ibet_links = d.ibet_links
    ibet_newnode = d.ibet_newnode
    ibet_temp = d.ibet_temp
    ibet_links1 = d.ibet_links1
    ibet_head = d.ibet_head
    ibet_tail = d.ibet_tail
    ibet_head1 = d.ibet_head1
    ibet_tail1 = d.ibet_tail1
    ibet_newhead = d.ibet_newhead
    ibet_newtail = d.ibet_newtail
    ibet_title = d.ibet_title
    ibet_steps = d.ibet_steps
    ibet_Null = d.ibet_Null

    ibet_title.up()
    ibet_steps.up()
    ibet_title.goto(d.horizontal + 50, d.vertical)
    ibet_title.write("Linked List:", font=("normal",12,"bold"))

    d.setPosition(250, 300)
    ll.LinkedList(ibet_nodes, ibet_links, ibet_head, ibet_tail, llist, length=90, width=100 , null=ibet_Null)

    d.setPosition(0, 200)
    ibet_title.goto(d.horizontal - 200, d.vertical)
    ibet_title.write("Insertion in Between in LL:", font=("normal",12,"bold"))
    ll.LinkedList(ibet_nodes, ibet_links, ibet_head1, ibet_tail1, llist, yPos=250, length=90, width=100, clear="no", null=ibet_Null)

    ll.link(ibet_extralinkclear, xcor=ll.arrowPos[index-1][index-index] + ll.nodelen * 0.80,
            ycor=ll.arrowPos[index-1][index-index+1] + ll.nodewid * 0.25, color="#B9F3FC", size=7)
    ll.link(ibet_extralink, xcor=ibet_extralinkclear.xcor() - 60, ycor=ibet_extralinkclear.ycor())

    ibet_steps.goto(d.horizontal - 200, d.vertical - 350)
    ibet_steps.write("Step1: Iterate through LL until index(" + str(index) + ") - 1 = " + str(index-1),
                     font=("normal",5,"bold"))
    time.sleep(1.2)

    dist = d.horizontal - ll.arrowPos[index-1][index - index] - ll.nodelen * 0.5 - 14

    for i in range(index):
        ibet_temp.clear()
        ll.head(ibet_temp, pos=i, x=ll.arrowPos[i][i-i], y=ll.arrowPos[i][i-i+1] + (ll.nodewid * 0.81), col="red", text="temp")
        time.sleep(1)

    ll.arrowPos.clear()
    ll.node(ibet_newnode, xcor=-dist, ycor=d.vertical-80 , lengthN=90, widthN=100, cradiusN=10, dataN=data, IndexN=False)

    ibet_newnodearrow.left(180)

    ll.head(ibet_newnodearrow, pos=None, x=ll.arrowPos[0][0], y=ll.arrowPos[0][1] - (ll.nodewid * 0.3),
            col="green", text="newNode", dir="up")

    ibet_steps.goto(ibet_steps.xcor(), ibet_steps.ycor() - 50)
    ibet_steps.write("Step 2 : Make newNode -> next = temp -> next ", font=("normal",5,"bold"))
    time.sleep(1.2)

    ibet_newnodelink.showturtle()
    ibet_newnodelink.up()
    ibet_newnodelink.goto(ll.arrowPos[0][0] + (ll.nodelen), y=ll.arrowPos[0][1] + (ll.nodewid * 0.25))
    ibet_newnodelink.pencolor("red")
    ibet_newnodelink.pensize(5)
    ibet_newnodelink.fillcolor("red")
    ibet_newnodelink.shape("classic")
    ibet_newnodelink.shapesize(5)
    ibet_newnodelink.down()
    ibet_newnodelink.forward((ll.nodewid * 0.5))
    ibet_newnodelink.left(90)
    ibet_newnodelink.forward((ll.nodewid * 0.75))
    ibet_newnodelink.left(90)
    ibet_newnodelink.forward((ll.nodelen * 1.30))
    ibet_newnodelink.right(90)
    ibet_newnodelink.forward((ll.nodewid * 0.92))
    ibet_newnodelink.right(90)

    x = ll.nodelen * 0.4

    xx = x / 2 + 2
    ll.link(ibet_newnodelink, xcor=ibet_newnodelink.xcor() - xx, ycor=ibet_newnodelink.ycor(), Gap=13)
    ibet_newnodelink.hideturtle()

    ibet_steps.goto(ibet_steps.xcor(), ibet_steps.ycor() - 50)
    ibet_steps.write("Step 3 : Make temp -> next = newNode ", font=("normal",5,"bold"))
    time.sleep(1.2)

    ibet_newnodelink.up()
    ibet_newnodelink.goto(ibet_newnodelink.xcor() - 40, ibet_newnodelink.ycor())

    ibet_newnodelink.pencolor("red")
    ibet_newnodelink.pensize(5)
    ibet_newnodelink.fillcolor("red")
    ibet_newnodelink.down()
    ibet_newnodelink.showturtle()
    ibet_newnodelink.forward(10)
    ibet_extralink.clear()
    ibet_newnodelink.right(90)
    ibet_newnodelink.forward((ll.nodewid * 0.92))
    ibet_newnodelink.right(90)
    ibet_newnodelink.forward((ll.nodewid * 0.75))
    ibet_newnodelink.left(90)
    ibet_newnodelink.forward((ll.nodewid * 0.75))
    ibet_newnodelink.left(90)
    ll.link(ibet_newnodelink, xcor=ibet_newnodelink.xcor() - xx, ycor=ibet_newnodelink.ycor(), Gap=20)
    ibet_newnodelink.hideturtle()

    d.setPosition(-150, 700)
    ibet_title.goto(d.horizontal - 50, d.vertical)
    ibet_title.write("After Insertion in LL :", font=("normal",12,"bold"))
    llist.insert(index, data)
    ll.arrowPos.clear()
    ll.LinkedList(ibet_nodes, ibet_links, ibet_newhead, ibet_newtail, llist, yPos=250, length=90, width=100, null=ibet_Null)


#-------------- Function to handle the window closing event -------------- #

def insert_bet(screen):
    try:
        d.setPosition( )       
        insert_In_Between(data, index, screen)
        time.sleep(500)
        d.setPosition( )
        #d.screen.bye()  # Close the turtle window
    except turtle.Terminator:
        pass  # Catch the Terminator error and do nothing
    except Exception as e:
        pass 
        print("An error occurred:", str(e))  # Handle any other exception and print an error message


##### ----------------- Main Driver Program ------------------- #####

# Set the close_window function to handle the window closing event

#d.screen.onkey(close_window_insert_in_bet_LL, "q")
#d.screen.listen()

insert_bet(screen)
