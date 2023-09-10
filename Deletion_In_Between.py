
import Main_ll as ll
import __main as d
import turtle
import time
from turtle import *

screen= None
llist = [5, 2, 4, 3, 1]
data = 3
position = None

def delete_In_Between(screen , data=None, position=None ):
    bgcol="#B9F3FC"
    screen.bgcolor(bgcol)
    d.createObject('dbet_Null', screen,  visibility=False , speed=0, color="black")  
    d.createObject('dbet_title', screen, visibility=False, speed=0, color="black")
    d.createObject('dbet_steps', screen, visibility=False, speed=0, color="black")
    d.createObject('dbet_nodes', screen, visibility=False, speed=0, color="black")
    d.createObject('dbet_links', screen, visibility=False, speed=0, color="black")
    d.createObject('dbet_temp', screen, visibility=False, speed=0, color="black")
    d.createObject('dbet_tempPrev', screen, visibility=False, speed=0, color="black")
    d.createObject('dbet_nodelink', screen, visibility=False, speed=3, color="red")
    d.createObject('dbet_head', screen, visibility=False, speed=0, color="black")
    d.createObject('dbet_tail', screen, visibility=False, speed=0, color="black")
    d.createObject('dbet_head1', screen, visibility=False, speed=0, color="black")
    d.createObject('dbet_tail1', screen, visibility=False, speed=0, color="black")
    d.createObject('dbet_newhead', screen, visibility=False, speed=0, color="black")
    d.createObject('dbet_newtail', screen, visibility=False, speed=0, color="black")
    d.createObject('dbet_extralink', screen, visibility=False, speed=0, color="black")
    d.createObject('dbet_extralinkclear', screen, visibility=False, speed=0, color="black")
    dbet_extralink = d.dbet_extralink
    dbet_extralinkclear = d.dbet_extralinkclear
    dbet_nodes = d.dbet_nodes
    dbet_nodelink = d.dbet_nodelink
    dbet_links = d.dbet_links
    dbet_temp = d.dbet_temp
    dbet_tempPrev = d.dbet_tempPrev
    dbet_head = d.dbet_head
    dbet_tail = d.dbet_tail
    dbet_head1 = d.dbet_head1
    dbet_tail1 = d.dbet_tail1
    dbet_newhead = d.dbet_newhead
    dbet_newtail = d.dbet_newtail
    dbet_title = d.dbet_title
    dbet_steps = d.dbet_steps
    dbet_Null = d.dbet_Null

    if data is None and position is not None:
        index = position - 1
        if index < 0 or index > len(llist):
            raise ValueError("Position is invalid: " + str(position) + ". Please enter a proper position.")

    if position is None and data is not None:
        index = llist.index(data)
        if index < 0 or index > len(llist):
            raise ValueError("Data " + str(data) + " is not available in the linked list.")

    dbet_title.up()
    dbet_steps.up()
    dbet_title.goto(d.horizontal + 50, d.vertical)
    dbet_title.write("Linked List:", font=("normal", 12, "bold"))

    d.setPosition(100, 300)
    ll.LinkedList(dbet_nodes, dbet_links, dbet_head, dbet_tail, llist, length=90, width=100 , null = dbet_Null)

    d.setPosition(0, 200)
    dbet_title.goto(d.horizontal - 50, d.vertical)
    dbet_title.write("Deletion in Between in LL:", font=("normal", 12, "bold"))
    ll.LinkedList(dbet_nodes, dbet_links, dbet_head1, dbet_tail1, llist, yPos=250, length=90, width=100, clear="no" , null = dbet_Null)

    ll.link(dbet_extralinkclear, xcor=ll.arrowPos[index][index - index] + ll.nodelen * 0.799,
            ycor=ll.arrowPos[index][index - index + 1] + ll.nodewid * 0.25, color="#B9F3FC", size=7)
    ll.link(dbet_extralink, xcor=dbet_extralinkclear.xcor() - 60, ycor=dbet_extralinkclear.ycor())

    ll.link(dbet_extralinkclear, xcor=ll.arrowPos[index - 1][index - index] + ll.nodelen * 0.799,
            ycor=ll.arrowPos[index - 1][index - index + 1] + ll.nodewid * 0.25, color="#B9F3FC", size=7)
    ll.link(dbet_extralink, xcor=dbet_extralinkclear.xcor() - 60, ycor=dbet_extralinkclear.ycor())

    dbet_steps.goto(d.horizontal - 50, d.vertical - 390)
    dbet_steps.write("Step 1: Iterate through LL until temp index(" + str(index) + ") and tempPrev index(" + str(
        index - 1) + ")", font=("normal", 5, "bold"))
    time.sleep(1.2)

    for i in range(index):
        dbet_temp.clear()
        dbet_tempPrev.clear()
        ll.head(dbet_temp, pos=i + 1, x=ll.arrowPos[i + 1][i - i],
                 y=ll.arrowPos[i + 1][i - i + 1] + (ll.nodewid * 0.81), col="red", text="temp")
        ll.head(dbet_tempPrev, pos=i, x=ll.arrowPos[i][i - i],
                 y=ll.arrowPos[i][i - i + 1] + (ll.nodewid * 0.81), col="red", text="tempPrev")
        time.sleep(1)

    dbet_steps.goto(dbet_steps.xcor(), dbet_steps.ycor() - 50)
    dbet_steps.write("Step 2: Make tempPrev -> next = temp -> next", font=("normal", 5, "bold"))
    time.sleep(1.2)

    dbet_nodelink.showturtle()
    dbet_nodelink.up()
    dbet_nodelink.goto(ll.arrowPos[index - 1][0] + ll.nodelen+5, y=ll.arrowPos[index - 1][1] + (ll.nodewid * 0.25))
    dbet_nodelink.pencolor("red")
    dbet_nodelink.pensize(5)
    dbet_nodelink.fillcolor("red")
    dbet_nodelink.shape("classic")
    dbet_nodelink.shapesize(5)
    dbet_nodelink.down()

    dbet_nodelink.forward(15)
    dbet_nodelink.right(90)
    dbet_nodelink.forward((ll.nodewid * 1.25))
    dbet_nodelink.left(90)
    dbet_nodelink.forward((ll.nodelen * 2))

    dbet_nodelink.left(90)
    dbet_nodelink.forward((ll.nodewid * 1.25))
    dbet_nodelink.right(90)

    x = ll.nodelen * 0.4
    xx = x / 2 + 2
    ll.link(dbet_nodelink, xcor=dbet_nodelink.xcor() - xx, ycor=dbet_nodelink.ycor(), Gap=20)
    dbet_nodelink.hideturtle()
    dbet_extralink.clear()

    dbet_steps.goto(dbet_steps.xcor(), dbet_steps.ycor() - 50)
    dbet_steps.write("Step 3: Make Node Free which indicates temp", font=("normal", 5, "bold"))
    time.sleep(1.2)

    dbet_temp.clear()
    dbet_temp.up()
    dbet_temp.pencolor("#B9F3FC")
    dbet_temp.goto(ll.arrowPos[index][0] - ll.nodelen * 0.7, ll.arrowPos[index][1] - ll.nodewid * 0.4)

    if index == len(llist) - 1:
        dbet_tail1.clear()

    dbet_temp.fillcolor("#B9F3FC")
    dbet_temp.begin_fill()
    dbet_temp.goto(dbet_temp.xcor(), dbet_temp.ycor() + ll.nodewid * 1.6)
    dbet_temp.goto(dbet_temp.xcor() + ll.nodelen * 1.8, dbet_temp.ycor())
    dbet_temp.goto(dbet_temp.xcor(), dbet_temp.ycor() - ll.nodewid * 1.6)
    dbet_temp.goto(dbet_temp.xcor() - ll.nodelen * 1.8, dbet_temp.ycor())
    dbet_temp.end_fill()

    d.setPosition(0, 700)
    dbet_title.goto(d.horizontal - 50, d.vertical)
    dbet_title.write("After Deletion in LL:", font=("normal", 12, "bold"))
    llist.pop(index)
    ll.arrowPos.clear()
    ll.LinkedList(dbet_nodes, dbet_links, dbet_newhead, dbet_newtail, llist, yPos=250, length=90, width=100 , null = dbet_Null)

# Function to handle the window closing event
def delete_bet(screen):
    try:
        d.setPosition( )
        delete_In_Between(screen , data, position )
        time.sleep(10)
        d.setPosition( )
        #d.screen.bye()  # Close the turtle window
    except turtle.Terminator:
        pass  # Catch the Terminator error and do nothing
    except Exception as e:
        pass
        print("An error occurred:", str(e))  # Handle any other exception and print an error message

# Set the close_window function to handle the window closing event
#d.screen.onkey(close_window_delete_in_bet_LL, "q")
#d.screen.listen()

delete_bet(screen)
